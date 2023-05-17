# This script processes the 'mkdocs.yml' file based on the value of 'database_edition' in the following manner:

# 1. If the value of 'database_edition' is 'enterprise':
#    - Remove the text between '# exclude.ent.begin' and '# exclude.ent.end'
#    - Keep the text between '# exclude.comm.begin' and '# exclude.comm.end'
#    - Keep the text between '# nav.ent.begin' and '# nav.ent.end'
#    - Remove the text between '# nav.comm.begin' and '# nav.comm.end'

# 2. If the value of 'database_edition' is 'community':
#    - Keep the text between '# nav.ent.begin' and '# nav.ent.end'
#    - Remove the text between '# nav.comm.begin' and '# nav.comm.end'
#    - Remove the text between '# nav.ent.begin' and '# nav.ent.end'
#    - Keep the text between '# nav.comm.begin' and '# nav.comm.end'

# 3. If the value of 'database_edition' is 'both', no changes are made to the file content.

import re
import yaml

mkdocs_yml_path = 'mkdocs.yml'

def process_mkdocs_yml(mkdocs_yml_path, database_edition):
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print("************before**************")
        print(content)
    if database_edition == 'enterprise':
        content = re.sub(
            r'#\s*exclude\.ent\.begin(.*?)#\s*exclude\.ent\.end', 
            '', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*exclude\.comm\.begin(.*?)#\s*exclude\.comm\.end', 
            '\\1', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*nav\.ent\.begin(.*?)#\s*nav\.ent\.end', 
            '\\1', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*nav\.comm\.begin(.*?)#\s*nav\.comm\.end', 
            '', content, flags=re.DOTALL)
    elif database_edition == 'community':
        content = re.sub(
            r'#\s*exclude\.ent\.begin(.*?)#\s*exclude\.ent\.end', 
            '\\1', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*exclude\.comm\.begin(.*?)#\s*exclude\.comm\.end', 
            '', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*nav\.ent\.begin(.*?)#\s*nav\.ent\.end', 
            '', content, flags=re.DOTALL)
        content = re.sub(
            r'#\s*nav\.comm\.begin(.*?)#\s*nav\.comm\.end', 
            '\\1', content, flags=re.DOTALL)
    else:
        raise ValueError("Invalid input for database_edition: {}".format(database_edition))
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)
        print("************after**************")
        print(content) 

if __name__ == '__main__':
    yml = 'database_edition.yml'
    with open(yml, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    database_edition = config.get("database_edition", "")
    if database_edition not in ['community', 'enterprise', 'both']:
        raise ValueError("Invalid value for database_edition: {}".format(database_edition))
    process_mkdocs_yml(mkdocs_yml_path, database_edition)
