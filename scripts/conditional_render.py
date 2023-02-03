# Rules for processing the markdown files in the docs-2.0 directory:
# - If database_edition is enterprise, the content between {{ ent.ent_begin }} and {{ ent.ent_end }} is kept and the content between {{ comm.comm_begin }} and {{ comm.comm_end }} is removed. 
# - If database_edition is community, the content between {{ comm.comm_begin }} and {{ comm.comm_end }} is kept and the content between {{ ent.ent_begin }} and {{ ent.ent_end }} is removed. 
# - If database_edition is both, both types of content are kept.

import os
import re
import yaml

def process_files(file_path, database_edition):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('.md'):
                file_full_path = os.path.join(root, file)
                with open(file_full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if database_edition == 'enterprise':
                    content = re.sub(
                        r'{{\s*ent\.ent_begin\s*}}(.*?){{\s*ent\.ent_end\s*}}', 
                        '\\1', content, flags=re.DOTALL)
                    content = re.sub(
                        r'{{\s*comm\.comm_begin\s*}}(.*?){{\s*comm\.comm_end\s*}}', 
                        '', content, flags=re.DOTALL)
                elif database_edition == 'community':
                    content = re.sub(
                        r'{{\s*ent\.ent_begin\s*}}(.*?){{\s*ent\.ent_end\s*}}', 
                        '', content, flags=re.DOTALL)
                    content = re.sub(
                        r'{{\s*comm\.comm_begin\s*}}(.*?){{\s*comm\.comm_end\s*}}', 
                        '\\1', content, flags=re.DOTALL)
                with open(file_full_path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    mkdocs_yml_path = 'mkdocs.yml'
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    database_edition = config.get("extra", {}).get("database_edition", "both")
    if database_edition not in ['community', 'enterprise', 'both']:
        raise ValueError("Invalid value for database_edition: {}".format(database_edition))
    file_path = 'docs-2.0/'
    process_files(file_path, database_edition)