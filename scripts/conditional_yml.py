# Rules for processing the mkdocs.yml file:
# - When `database_edition` is `community`, keep all content between tags `# ent.begin` and `# ent.end`, and delete all content between tags `# comm.begin` and `# comm.end`.
# - When `database_edition` is `enterprise`, keep all content between `# comm.begin` and `# comm.end`, and delete all content between `# ent.begin` and `# ent.end`
# - When `database_edition` is `both`, delete all content between `# ent.begin` and `# ent.end`, and between `# comm.begin` and `# comm.end`.
# - Always keep the tags.

import os
import re
import yaml

mkdocs_yml_path = 'mkdocs.yml'

def process_mkdocs_yml(mkdocs_yml_path, database_edition):
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if database_edition == 'enterprise':
        content = re.sub(
            r'#\s*ent\.begin(.*?)#\s*ent\.end', 
            '', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*comm\.begin(.*?)#\s*comm\.end', 
            '\\1', content, flags=re.DOTALL)
    elif database_edition == 'community':
        content = re.sub(
            r'#\s*ent\.begin(.*?)#\s*ent\.end', 
            '\\1', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*comm\.begin(.*?)#\s*comm\.end', 
            '', content, flags=re.DOTALL)
    elif database_edition == 'both':
        content = re.sub(
            r'#\s*ent\.begin(.*?)#\s*ent\.end', 
            '', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*comm\.begin(.*?)#\s*comm\.end', 
            '', content, flags=re.DOTALL)
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    mkdocs_yml_path = 'mkdocs.yml'
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    database_edition = config.get("extra", {}).get("database_edition", "both")
    if database_edition not in ['community', 'enterprise', 'both']:
        raise ValueError("Invalid value for database_edition: {}".format(database_edition))
    process_mkdocs_yml(mkdocs_yml_path, database_edition)