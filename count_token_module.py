import os
import tiktoken
from pathlib import Path
def get_encoding(encoding_name='cl100k_base'):
    return tiktoken.get_encoding(encoding_name)
def count_tokens_in_file(file_path, encoding):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        num_tokens = len(encoding.encode(content))
        return num_tokens
def count_tokens_in_files(root_dir, encoding):
    token_counts = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                num_tokens = count_tokens_in_file(file_path, encoding)
                token_counts.append((file_path, num_tokens))
    return token_counts
def write_token_counts_to_file(token_counts, output_dir, max_token_count=1500):
    output_file = os.path.join(output_dir, 'token_counts.txt')
    to_be_split = []
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path, num_tokens in token_counts:
            f.write(f"{file_path}: {num_tokens} tokens\n")
            if num_tokens > max_token_count:
                to_be_split.append(file_path)
        f.write("\nFiles to be split:\n")
        for file_path in to_be_split:
            f.write(f"{file_path}\n")
def process_directory(output_dir, encoding_name='cl100k_base', max_token_count=1500):
    encoding = get_encoding(encoding_name)
    token_counts = count_tokens_in_files(output_dir, encoding)
    write_token_counts_to_file(token_counts, output_dir, max_token_count)
# Example usage:
output_dir = 'output'
process_directory(output_dir)