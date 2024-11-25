#!/usr/bin/env python3
# sudo dos2unix process_templates.py

import re
import os
import sys
from pathlib import Path

def read_file_content(filename, base_dir):
    try:
        # Construct full path relative to the template file's location
        full_path = base_dir / filename
        with open(full_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: File {filename} not found", file=sys.stderr)
        return f"<!-- {filename} not found -->"

def process_includes(template_file):
    base_dir = template_file.parent
    
    # Read the template file
    try:
        with open(template_file, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found", file=sys.stderr)
        return None

    # Pattern to match {{ include "filename" }}
    pattern = r'{{\s*include\s*"([^"]+)"\s*}}'
    
    # Function to replace matches with file contents
    def replacer(match):
        filename = match.group(1)
        return read_file_content(filename, base_dir)

    # Replace all instances of the pattern with the contents of the referenced files
    processed_content = re.sub(pattern, replacer, content)
    
    return processed_content

def process_directory():
    # Get the current working directory
    current_dir = Path.cwd()
    
    # Find all .tmpl files recursively
    template_files = list(current_dir.rglob("*.tmpl"))
    
    if not template_files:
        print("No .tmpl files found in the directory structure.", file=sys.stderr)
        return
    
    print(f"Found {len(template_files)} template files to process.")
    
    # Process each template file
    for template_file in template_files:
        print(f"Processing {template_file}")
        
        # Generate output filename (change extension from .tmpl to .html)
        output_file = template_file.with_suffix('.html')
        
        # Process the template
        processed_content = process_includes(template_file)
        
        if processed_content is not None:
            try:
                # Write the processed content to the output file
                with open(output_file, 'w') as file:
                    file.write(processed_content)
                print(f"Created {output_file}")
            except IOError as e:
                print(f"Error writing to {output_file}: {e}", file=sys.stderr)
                continue

def main():
    print("Starting template processing...")
    process_directory()
    print("Template processing complete.")

if __name__ == "__main__":
    main()
