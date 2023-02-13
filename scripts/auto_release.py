import re

def replace_line(file_path, search_text, new_line):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        new_content = re.sub(search_text, new_line, file_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def update_github_actions(doc_version):
    if doc_version == 'master':
        replace_line('.github/workflows/deploy.yaml', r'branches:\s+-.*', f'branches:\n      - {doc_version}')
        replace_line('.github/workflows/deploy.yaml', r'mike deploy .* -p --rebase\n          mike set-default .* -p --rebase', f'mike deploy {doc_version} -p --rebase')
        replace_line('.github/workflows/deploy.yaml', r'tar -vczf nebula-docs.tar.gz.*', f'tar -vczf nebula-docs.tar.gz {doc_version} versions.json *.html')
        replace_line('.github/workflows/deploy.yaml', r'cp -f /usr/web/nebula-docs/.*/pdf/NebulaGraph-CN.pdf', f'cp -f /usr/web/nebula-docs/{doc_version}/pdf/NebulaGraph-CN.pdf')
    else:
        replace_line('.github/workflows/deploy.yaml', r'branches:\s+-.*', f'branches:\n      - v{doc_version}')
        replace_line('.github/workflows/deploy.yaml', r'mike deploy .* -p --rebase', f'mike deploy {doc_version} -p --rebase\n          mike set-default {doc_version} -p --rebase')
        replace_line('.github/workflows/deploy.yaml', r'tar -vczf nebula-docs.tar.gz.*', f'tar -vczf nebula-docs.tar.gz {doc_version} versions.json *.html')
        replace_line('.github/workflows/deploy.yaml', r'cp -f /usr/web/nebula-docs/.*/pdf/NebulaGraph-CN.pdf', f'cp -f /usr/web/nebula-docs/{doc_version}/pdf/NebulaGraph-CN.pdf')

def update_mkdocs_yml(doc_version):
    if doc_version == 'master':
        replace_line('./mkdocs.yml', r'cover_subtitle:.*', f'cover_subtitle: {doc_version}')
        replace_line('./mkdocs.yml', r'https://github.com/vesoft-inc/nebula-docs-cn/edit/.*/docs-2.0/', f'https://github.com/vesoft-inc/nebula-docs-cn/edit/{doc_version}/docs-2.0/')
    else:
        replace_line('./mkdocs.yml', r'cover_subtitle:.*', f'cover_subtitle: v{doc_version}')
        replace_line('./mkdocs.yml', r'https://github.com/vesoft-inc/nebula-docs-cn/edit/.*/docs-2.0/', f'https://github.com/vesoft-inc/nebula-docs-cn/edit/v{doc_version}/docs-2.0/')

if __name__ == "__main__":
    with open('./mkdocs.yml', 'r', encoding='utf-8') as f:
        file_content = f.read()
    doc_version_match = re.search(r'doc_version:.*', file_content)
    if doc_version_match:
        doc_version = doc_version_match.group().split(':')[1].strip()
        if not isinstance(doc_version, str):
            raise TypeError("The value of doc_version should be a string")
    else:
        raise Exception("The value of doc_version is not found in mkdocs.yml")
    update_github_actions(doc_version)
    update_mkdocs_yml(doc_version)
