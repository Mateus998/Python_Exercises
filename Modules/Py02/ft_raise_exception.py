def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if 0 <= temp_int <= 40:
        return temp_int
    else:
        raise ValueError("Temperature out of limits")

def test_temperature() -> None:
    print(f"temperature: {input_temperature("25")}º")
    try:
        print(f"temperature: {input_temperature("100")}º")
    except ValueError as err:
        print(err)
    print("end program")

if __name__ == "__main__":
    test_temperature()

'''
# Exceção genérica
raise Exception("Algo deu errado")

# ValueError - quando o valor é inválido
raise ValueError("O valor deve ser um número")

# TypeError - quando o tipo é errado
raise TypeError("Esperado string, recebido int")

# KeyError - chave não existe
raise KeyError("A chave 'nome' não foi encontrada")

# IndexError - índice fora do alcance
raise IndexError("Índice 5 não existe na lista")

# ZeroDivisionError - divisão por zero
raise ZeroDivisionError("Não é possível dividir por zero")
'''