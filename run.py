import os
import mobi
from markdownify import markdownify as md
from pathlib import Path

# Function to convert MOBI file to markdown
def convert_mobi_to_md(mobi_file, output_md_file):
    # Extract the mobi file using mobi package
    extracted_info = mobi.extract(mobi_file)

    # Extracted info is a tuple, we need the first element (the extraction folder path)
    temp_folder = extracted_info[0]

    # Look for HTML content in the extracted files
    html_file = None
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                break

    if html_file:
        try:
            # Try reading the file with UTF-8 encoding
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except UnicodeDecodeError:
            # If there is a UnicodeDecodeError, try a different encoding or ignore errors
            print(f"Warning: UTF-8 decoding failed for {html_file}. Trying a fallback encoding.")
            with open(html_file, 'r', encoding='ISO-8859-1', errors='ignore') as f:
                html_content = f.read()

        # Convert HTML to markdown
        md_content = md(html_content)

        # Save markdown content
        with open(output_md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Converted {mobi_file} to {output_md_file}")
    else:
        print(f"No HTML file found in extracted {mobi_file}")

    # Clean up temporary folder
    os.system(f'rm -rf {temp_folder}')

# Traverse directories to find MOBI files and convert them
def convert_all_mobi_to_md(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mobi'):
                mobi_file = os.path.join(root, file)
                md_file = Path(mobi_file).with_suffix('.md')
                try:
                    convert_mobi_to_md(mobi_file, md_file)
                except:
                    print(f"Failed to convert {mobi_file}")

# Replace 'books_directory' with your target directory
books_directory = 'books'
convert_all_mobi_to_md(books_directory)
