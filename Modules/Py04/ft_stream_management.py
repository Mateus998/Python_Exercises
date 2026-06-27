import sys
from typing import IO

def open_file(file_name: str, op: str) -> IO[str] | None:
    f = None
    try:
        f = open(file_name, op)
    except OSError as err:
        sys.stderr.write(str(err) + '\n')
    return f

def main():
    if len(sys.argv) != 2:
        print("Error: Usage: python3 ft_archive_creation.py <file_name>"); return
    
    print(f"Accessing file {sys.argv[1]}")

    f = open_file(sys.argv[1], 'r')
    if not f: return
    
    text = f.read()
    print(f"---\n{text}\n---")
    f.close()
    print(f"File {sys.argv[1]} closed")

    lines = text.splitlines()
    new_text = "\n".join(line + '#' for line in lines)

    print("\nTransform data:")
    print(f"---\n{new_text}\n---")

    sys.stdout.write("Enter file name to save (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline()
    if not new_name: print("New data not saved"); return

    new_file = open_file(new_name, 'w')
    if not new_file: return

    new_file.write(new_text)
    print(f"New data saved on {new_name}")
    new_file.close()

if __name__ == "__main__":
    main()