#!/bin/bash

# Directory containing your Typst files
SOURCE_DIR="./typ"

# Directory where the compiled files will be moved
DESTINATION_DIR="./pdf"

# File extension you want to compile (e.g., ".typ")
EXTENSION=".typ"

# Compile command for Typst
COMPILE_COMMAND="typst compile"

# Ensure the destination directory exists
mkdir -p "$DESTINATION_DIR"

# Loop through each file with the specified extension in the source directory
for FILE in "$SOURCE_DIR"/*"$EXTENSION"; do
  # Check if the file exists to avoid errors
  if [ -f "$FILE" ]; then
    BASENAME=$(basename "$FILE" "$EXTENSION")
    OUTPUT_FILE="$BASENAME.pdf"
    echo "Compiling $FILE..."

    # Run the compilation command and capture the output file path
    $COMPILE_COMMAND "$FILE" "$DESTINATION_DIR/$OUTPUT_FILE"
  fi
done
