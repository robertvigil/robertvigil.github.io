#!/usr/bin/env python3
# sudo dos2unix build.py

import re
import argparse
import sys

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: File {filename} not found", file=sys.stderr)
        return f"<!-- {filename} not found -->"

def process_includes(input_file):
    # Read the main file
    try:
        with open(input_file, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found", file=sys.stderr)
        return None

    # Pattern to match {{ include "filename" }}
    pattern = r'{{\s*include\s*"([^"]+)"\s*}}'
    
    # Function to replace matches with file contents
    def replacer(match):
        filename = match.group(1)
        return read_file_content(filename)

    # Replace all instances of the pattern with the contents of the referenced files
    processed_content = re.sub(pattern, replacer, content)
    
    return processed_content

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process file includes in a text file.')
    parser.add_argument('input_file', help='Input file to process')
    parser.add_argument('output_file', help='Output file to write results to')
    
    # Parse arguments
    args = parser.parse_args()
    
    processed_content = process_includes(args.input_file)
    
    if processed_content is not None:
        # Write the processed content to the output file
        try:
            with open(args.output_file, 'w') as file:
                file.write(processed_content)
            print(f"Processing complete. Output written to {args.output_file}")
        except IOError as e:
            print(f"Error writing to output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
