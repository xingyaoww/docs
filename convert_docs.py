#!/usr/bin/env python3
import os
import re
import shutil
import sys

def sanitize_content(content):
    # Replace Docusaurus tags with Mintlify callouts
    content = re.sub(r':::note(.*?):::', r'<Note>\1</Note>', content, flags=re.DOTALL)
    content = re.sub(r':::tip(.*?):::', r'<Tip>\1</Tip>', content, flags=re.DOTALL)
    content = re.sub(r':::info(.*?):::', r'<Info>\1</Info>', content, flags=re.DOTALL)
    content = re.sub(r':::warning(.*?):::', r'<Warning>\1</Warning>', content, flags=re.DOTALL)
    content = re.sub(r':::danger(.*?):::', r'<Danger>\1</Danger>', content, flags=re.DOTALL)
    
    # Replace Docusaurus imports
    content = re.sub(r'import\s+(\w+)\s+from\s+\'@theme/(\w+)\';', r'/* Removed Docusaurus import: \1 from @theme/\2 */', content)
    
    # Replace HTML comments with JS comments
    content = re.sub(r'<!--(.*?)-->', r'/* \1 */', content, flags=re.DOTALL)
    
    # Fix image paths
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', lambda m: f'![\g<1>](/images/\g<2>.split("/")[-1])' if '/' in m.group(2) else f'![\g<1>](/images/\g<2>)', content)
    
    return content

def convert_file(source_path, dest_path):
    print(f"Converting {source_path} to {dest_path}")
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sanitize content for Mintlify
    content = sanitize_content(content)
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

def copy_images(source_dir, dest_dir):
    # Copy images from static directory to images directory
    if os.path.exists(os.path.join(source_dir, 'static')):
        for root, dirs, files in os.walk(os.path.join(source_dir, 'static')):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_dir, 'images', file)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied image: {source_path} to {dest_path}")

def main():
    source_dir = '/workspace/OpenHands/docs'
    dest_dir = '/workspace/docs'
    
    # Copy images first
    copy_images(source_dir, dest_dir)
    
    # Process markdown files
    for root, dirs, files in os.walk(os.path.join(source_dir, 'modules')):
        for file in files:
            if file.endswith('.md') or file.endswith('.mdx'):
                source_path = os.path.join(root, file)
                
                # Determine destination path
                rel_path = os.path.relpath(source_path, os.path.join(source_dir, 'modules'))
                
                # Change extension to .mdx
                base_name = os.path.splitext(rel_path)[0]
                dest_path = os.path.join(dest_dir, base_name + '.mdx')
                
                convert_file(source_path, dest_path)

if __name__ == "__main__":
    main()