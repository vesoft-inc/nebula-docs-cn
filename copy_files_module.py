import os
import shutil
from pathlib import Path
import argparse


def copy_markdown_files(src_path: str, dest_path: str) -> None:
    src_path = Path(src_path)
    dest_path = Path(dest_path)

    if not src_path.exists() or not src_path.is_dir():
        raise ValueError(f"源目录 '{src_path}' 不存在或不是一个有效目录")
    
    if not dest_path.exists():
        dest_path.mkdir(parents=True, exist_ok=True)

    for root, _, files in os.walk(src_path):
        root_path = Path(root)
        relative_path = root_path.relative_to(src_path)
        target_path = dest_path / relative_path

        if not target_path.exists():
            target_path.mkdir(parents=True, exist_ok=True)

        for file in files:
            if file.lower().endswith('.md'):
                src_file_path = root_path / file
                dest_file_path = target_path / file
                shutil.copy2(src_file_path, dest_file_path)


def main():
    parser = argparse.ArgumentParser(description='复制所有 Markdown 文件及其目录结构')
    parser.add_argument('src_directory', type=str, help='源目录路径')
    parser.add_argument('dest_directory', type=str, help='输出目录路径')
    args = parser.parse_args()

    try:
        copy_markdown_files(args.src_directory, args.dest_directory)
        print("Markdown 文件复制完成!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
