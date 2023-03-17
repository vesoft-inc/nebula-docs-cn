import os
import tiktoken

MAX_TOKENS = 1500

def tokenize_content(content, encoding):
    tokens = encoding.encode(content)
    num_tokens = len(tokens)
    if num_tokens <= MAX_TOKENS:
        return [(content, num_tokens)]
    else:
        sections = []
        # Split content by H2 headings
        parts = content.split('\n## ')
        for part in parts:
            if len(part.strip()) > 0:
                lines = part.strip().split('\n')
                title = lines[0]
                sub_sections = [(f"## {title}", encoding.encode(title))]
                sub_content = '\n'.join(lines[1:])
                sub_sections += tokenize_content(sub_content, encoding)
                # Add sub-sections to sections if total number of tokens <= MAX_TOKENS
                sub_section_tokens = sum([num_tokens for _, num_tokens in sub_sections if isinstance(num_tokens, int)])
                if sub_section_tokens <= MAX_TOKENS:
                    section_content = '\n'.join([section for section, _ in sub_sections])
                    section_num_tokens = sum([num_tokens for _, num_tokens in sub_sections])
                    sections.append((section_content, section_num_tokens))
                else:
                    sections += sub_sections
        return sections

def split_file(file_path, encoding):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    sections = []
    # Split content by H1 heading and the first H2 heading
    parts = content.split('\n## ')
    first_part = parts[0].split('\n# ')
    if len(first_part) > 1:
        sections.append((f"# {first_part[1]}", encoding.encode(first_part[1])))
        sections.append((first_part[0], encoding.encode(first_part[0])))
    else:
        sections.append((first_part[0], encoding.encode(first_part[0])))
    if len(parts) > 1:
        lines = parts[1].strip().split('\n')
        title = lines[0]
        sub_sections = [(f"## {title}", encoding.encode(title))]
        sub_content = '\n'.join(lines[1:])
        sub_sections += tokenize_content(sub_content, encoding)
        sections += sub_sections
    # Handle the rest of the sections with H2 headings
    for part in parts[2:]:
        lines = part.strip().split('\n')
        title = lines[0]
        sub_sections = [(f"## {title}", encoding.encode(title))]
        sub_content = '\n'.join(lines[1:])
        sub_sections += tokenize_content(sub_content, encoding)
        # Save sub-sections to files
        sub_section_tokens = sum([num_tokens for _, num_tokens in sub_sections])
        if sub_section_tokens <= MAX_TOKENS:
            section_content = '\n'.join([section for section, _ in sub_sections])
            section_num_tokens = sum([num_tokens for _, num_tokens in sub_sections])
            sections.append((section_content, section_num_tokens))
        else:
            for sub_section_content, sub_section_num_tokens in sub_sections:
                file_dir = os.path.dirname(file_path)
                file_name, file_ext = os.path.splitext(os.path.basename(file_path))
                rel_dir = os.path.relpath(file_dir, start='docs-2.0')
                new_dir = os.path.join('output', 'docs-2.0', rel_dir)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                new_file_name = f"{file_name}-{title.strip().replace(' ', '-')}{file_ext}"
                new_file_path = os.path.join(new_dir, new_file_name)
                with open(new_file_path, 'w', encoding='utf-8') as new_f:
                    new_f.write(sub_section_content)
    return [(content, num_tokens) for content, num_tokens in sections if num_tokens <= MAX_TOKENS]

def process_directory(root_dir, encoding_name):
    encoding = tiktoken.get_encoding(encoding_name)
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                new_paths = split_file(file_path, encoding)
                if len(new_paths) > 1:
                    print(f"{file_path} was split into {len(new_paths)} files.")
                for i, (content, num_tokens) in enumerate(new_paths):
                    if num_tokens <= MAX_TOKENS:
                        # Save content to original file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                    else:
                        # Save content to a new file
                        file_dir = os.path.dirname(file_path)
                        file_name, file_ext = os.path.splitext(os.path.basename(file_path))
                        rel_dir = os.path.relpath(file_dir, start='docs-2.0')
                        new_dir = os.path.join('output', 'docs-2.0', rel_dir)
                        if not os.path.exists(new_dir):
                            os.makedirs(new_dir)
                        new_file_name = f"{file_name}-part{i+1}{file_ext}"
                        new_file_path = os.path.join(new_dir, new_file_name)
                        with open(new_file_path, 'w', encoding='utf-8') as new_f:
                            new_f.write(content)
                print(f"{file_path} done.")

# Example usage:
root_dir = 'docs-2.0'
encoding_name = 'cl100k_base'  # Change the encoding if necessary
process_directory(root_dir, encoding_name)