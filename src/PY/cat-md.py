import os
import glob

def create_code_block_file(filename, output_filename="./output.md"):
    """
    Reads the content of a file and appends it to another file
    enclosed in a Markdown code block.  Uses '>>' (append mode).
    """
    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    try:
        with open(output_filename, 'a', encoding='utf-8') as outfile:  # 'a' for append
            outfile.write("```\n")
            outfile.write(file_content)
            outfile.write("\n```\n")  # Add an extra newline for separation
        print(f"Successfully appended code block from '{filename}' to '{output_filename}'")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")

def append_text_to_file(text, output_filename="./output.md"):
    """
    Appends the given text to the specified output file.
    """
    try:
        with open(output_filename, 'a', encoding='utf-8') as outfile:  # 'a' for append
            outfile.write(text)
            outfile.write("\n") # add a newline after the appended text
        print(f"Successfully appended text to '{output_filename}'")
    except Exception as e:
        print(f"An error while appending text to '{output_filename}': {e}")


def clear_output_file(output_filename="./output.md"):
    """
    Clears the content of the specified output file.
    """
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write("")
        print(f"Successfully cleared the content of '{output_filename}'")
    except Exception as e:
        print(f"An error occurred while clearing '{output_filename}': {e}")


def process_parent_po_file(output_filename="./output.md"):
    """
    Finds and processes the 'zh-kawaii.po' file in the parent directory.
    """
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    target_file_path = os.path.join(parent_dir, "zh-kawaii.po")

    if os.path.exists(target_file_path):
        create_code_block_file(target_file_path, output_filename)
    else:
        print(f"Error: 'zh-kawaii.po' not found in the parent directory: {parent_dir}")


def process_gcc_files(output_filename="./output.md"):
    """
    Finds and processes files matching 'gcc*zh*' in the current directory.
    """
    current_dir = os.getcwd()
    pattern = os.path.join(current_dir, "gcc*.pot")
    matching_files = glob.glob(pattern)

    if matching_files:
        for file_path in matching_files:
            create_code_block_file(file_path, output_filename)
    else:
        print("No files matching 'gcc*zh*' found in the current directory.")



# --- Main execution flow ---

clear_output_file()  # Clear output.md (important when using append mode)

# Add some introductory text
append_text_to_file("## 这是样例\n", "./output.md")
append_text_to_file("你需要仔细阅读下面文件，然后了解其风格进行翻译。\n", "./output.md")
process_parent_po_file()

append_text_to_file("## 这是待处理文件\n", "./output.md")
append_text_to_file("你需要将msgid进行翻译，然后文本输出到msgstr。", "./output.md")
append_text_to_file("请注意翻译风格与案例相似。", "./output.md")
append_text_to_file("除此之外，你应该使用格式符去控制输出。如%<__fpreg%>等等。\n", "./output.md")
process_gcc_files()
