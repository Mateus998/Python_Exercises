def secure_archive(file_name: str, text: str | None) -> tuple[bool, str]:
    try:
        with open(file_name, 'r+') as file:
            if text:
               file.write(text)
            file.seek(0)
            return (True, file.read()) 
    except OSError as err:
        return (False, str(err))


def main():
    print(secure_archive("test.txt", None))
    print(secure_archive("test.txt", "new content"))
    print(secure_archive("test.txt2", None))

if __name__ == "__main__":
    main()