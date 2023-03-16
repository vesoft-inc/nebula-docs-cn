import os
import tiktoken

def count_tokens_in_files(root_dir, encoding_name):
    encoding = tiktoken.get_encoding(encoding_name)

    def count_tokens_in_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            num_tokens = len(encoding.encode(content))
            return num_tokens

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                num_tokens = count_tokens_in_file(file_path)
                print(f"{file_path}: {num_tokens} tokens")

# Example usage:
root_dir = 'docs-2.0/3.ngql-guide/7.general-query-statements'
encoding_name = 'cl100k_base'  # Change the encoding if necessary
count_tokens_in_files(root_dir, encoding_name)