#!/bin/bash

# Set the directory you want to start from
TARGET_DIR="./books"

# Find and delete files that don't have the .md extension
find "$TARGET_DIR" -type f ! -name "*.md" -exec rm -v {} \;
