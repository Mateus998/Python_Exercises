import argparse

def main():
    parser = argparse.ArgumentParser(
        usage= "pthon3 ft_ancient_text.py <file_name>",
        description= "Lê o conteúdo de um ficheiro"
    )

    parser.add_argument("file", help="file path")

    args = parser.parse_args()
    
    print(f"Accessing file {args.file}")

    f = None
    try:
        f = open(args.file, "r")
    except OSError as err:
        print(err); return
    
    text = f.read()
    print(f"---\n{text}\n---")
    f.close()
    print(f"File {args.file} closed")

if __name__ == "__main__":
    main()