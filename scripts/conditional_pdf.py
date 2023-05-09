import re
import yaml

def process_mkdocs_yml(mkdocs_yml_path, withpdf):
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if withpdf == True:
        content = re.sub(
            r'#\s*nav\.pdf\.begin(.*?)#\s*nav\.pdf\.end', 
            '\\1', content, flags=re.DOTALL)
    elif withpdf == False:
        print("remove pdf")
        content = re.sub(
            r'#\s*nav\.pdf\.begin(.*?)#\s*nav\.pdf\.end', 
            '', content, flags=re.DOTALL)
    with open(mkdocs_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(content)

if __name__ == '__main__':
    pdf_yml_path = 'pdf.yml'
    with open(pdf_yml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    withpdf = config.get("withpdf", "")
    print(withpdf)
    if (withpdf != True) and (withpdf != False):
        raise ValueError("Invalid value for pdf parameter: {}".format(withpdf))
    process_mkdocs_yml('mkdocs.yml', withpdf)
