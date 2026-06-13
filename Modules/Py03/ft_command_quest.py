import sys

if __name__ == "__main__":
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    print(f"Program name: {program_name}")
    if not arguments:
        print("No arguments provided!")
    else:
        for i, arg in enumerate(arguments, start=1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(sys.argv)}")

    '''
    sys.argv - lista str de argumentos do programa
    len() - devolve o tamanho do container
    not - identifica se a condição é falsa
    enumerate() - numera os elementos da lista para acessar no loop
    start=1 - faz o enumerate começar no 1
    '''