
import os

try:
    # Ask user for the README file path
    file_path = input("Enter the full path of your README.md file: ").strip()

    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError

    # Read the original content
    with open(file_path, "r", encoding="utf-8") as file:
        original_content = file.read()

    # Print the original content
    print("\n📖 Original README.md content:\n")
    print(original_content)

    # Extra info to add
    extra_info = """
----------------------------------------
🚀 Outcomes

By completing this assignment, you will:

- Understand how to use Python’s open() function.
- Learn the difference between "r", "w", "a" modes.
- Handle common file errors using try...except.
- Build robust Python scripts that won’t crash unexpectedly.
"""

    # Prevent adding extra info multiple times
    if extra_info not in original_content:
        combined_content = original_content + extra_info
    else:
        combined_content = original_content
        print("\n Extra info already present in the file.")

    # Write back to the same file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(combined_content)

    # Print updated content
    print("\n📖 Updated README.md content:\n")
    print(combined_content)

    print(f"\n✅ File processed successfully! '{file_path}' has been updated.")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied to read/write the file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
