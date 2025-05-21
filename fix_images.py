#!/usr/bin/env python3
import os
import re

def fix_image_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace invalid image paths with a comment
    if '\\g<' in content:
        content = re.sub(r'!\[\\g<1>\]\(/images/\\g<2>\.split\("/"\)\[-1\]\)', '<!-- Image placeholder -->', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    docs_dir = '/workspace/docs'
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                fix_image_paths(file_path)
                print(f"Fixed {file_path}")

if __name__ == "__main__":
    main()