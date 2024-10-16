Here is a `README.md` file for the given code:

---

# MOBI to Markdown Converter

This Python script converts all `.mobi` files in a specified directory (and its subdirectories) to Markdown format. The script uses the `mobi` package to extract content from `.mobi` files and `markdownify` to convert the extracted HTML content to Markdown.

## Features

- Recursively scans through directories and subdirectories for `.mobi` files.
- Converts `.mobi` files to `.md` (Markdown) format.
- Automatically cleans up temporary extracted files after conversion.

## Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install mobi markdownify
```

## Usage

1. Clone this repository or copy the script.

2. Set the target directory by modifying the `books_directory` variable in the script. This is the directory where your `.mobi` files are stored.

```python
books_directory = 'path/to/your/books_directory'
```

3. Run the script:

```bash
python convert_mobi_to_md.py
```

The script will find all `.mobi` files within the specified directory and its subdirectories and convert them to `.md` files.

## How It Works

1. **Extracting MOBI Files**:  
   The script uses the `mobi.extract()` function to extract the content of the `.mobi` file. It looks for an HTML file inside the extracted content.

2. **Converting to Markdown**:  
   Once the HTML content is found, the script uses `markdownify` to convert the HTML content to Markdown format.

3. **Saving the Markdown File**:  
   The resulting Markdown content is saved with the same file name as the original `.mobi` file but with a `.md` extension.

4. **Cleanup**:  
   Use the included delete_non_md_files.sh to clean the old mobi files (and all others aswell)

## Example

If the directory contains the following structure:

```
books/
├── subdir1/
│   └── book1.mobi
├── subdir2/
│   └── book2.mobi
```

After running the script, the structure will look like:

```
books/
├── subdir1/
│   ├── book1.mobi
│   └── book1.md
├── subdir2/
│   ├── book2.mobi
│   └── book2.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like further customizations!
