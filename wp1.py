import sys
from pathlib import Path

def get_input():
    directory = "."
    text_input = input("Enter file names: ").split()
    print()

    original_file_path = Path(directory) / text_input[0]
    encrypted_file_path = Path(directory) / text_input[1]

    return original_file_path, encrypted_file_path

def reverse_lines(text):
    reversed_lines = []
    for line in text:
        reversed_lines.append(line[::-1])

    reversed_lines.reverse()

    return "".join(reversed_lines)

def write_to_encrypted_file(original_text, encrypted_text):
    try:
        with open(original_text, "r") as source:
            content = source.readlines()

        reverse_text = reverse_lines(content)

        with open(encrypted_text, "w") as encryption:
            encryption.write(reverse_text)

        return encrypted_text
    except FileNotFoundError as e:
        print(f"{e}")

def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python wp1.py file.txt file.txt")
            sys.exit(1) 

        original_text_filename = sys.argv[1]
        encrypted_text_filename = sys.argv[2]

        original_text = Path(original_text_filename)
        encrypted_text = Path(encrypted_text_filename)

        encryption = write_to_encrypted_file(original_text, encrypted_text)

        with open(encryption, "r") as file:
            for line in file:
                print(line.strip())
    except:
        print("Error: Please try again")

if __name__ == "__main__":
    main()
