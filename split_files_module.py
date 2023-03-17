import os
import re
from pathlib import Path

def read_to_be_split_files(output_dir):
    token_counts_file = os.path.join(output_dir, 'token_counts.txt')
    to_be_split_files = []

    with open(token_counts_file, 'r', encoding='utf-8') as f:
        content = f.readlines()
        start = False
        for line in content:
            if 'Files to be split:' in line:
                start = True
                continue
            if start:
                to_be_split_files.append(line.strip())

    return to_be_split_files

def split_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_code_blocks(match):
        return match.group(0).replace("#", "\ufeff#")

    code_block_pattern = r'```.*?```'
    content = re.sub(code_block_pattern, replace_code_blocks, content, flags=re.DOTALL)

    section_pattern = r"(^#{1,6} .*)"
    sections = re.split(section_pattern, content, flags=re.MULTILINE)

    split_file_paths = []
    for idx in range(1, len(sections), 2):
        title = sections[idx].strip()
        body = sections[idx + 1].strip()
        split_content = f"{title}\n\n{body}".replace("\ufeff#", "#")
        
        split_file_path = f"{file_path[:-3]}_{idx//2+1}.md"
        with open(split_file_path, 'w', encoding='utf-8') as split_f:
            split_f.write(split_content)
        split_file_paths.append(split_file_path)

    return split_file_paths

def write_split_files_to_file(split_files, output_dir):
    split_files_file = os.path.join(output_dir, 'split_files.txt')
    with open(split_files_file, 'w', encoding='utf-8') as f:
        for file_path in split_files:
            f.write(f"{file_path}\n")

def process_split_files(output_dir):
    to_be_split_files = read_to_be_split_files(output_dir)
    split_files = []

    for file_path in to_be_split_files:
        split_file_paths = split_file(file_path)
        split_files.extend(split_file_paths)
        os.remove(file_path)  # Remove the original file after splitting

    write_split_files_to_file(split_files, output_dir)

# Example usage:
output_dir = 'output'
process_split_files(output_dir)
