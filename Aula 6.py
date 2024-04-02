
class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_string(input_string):
    pilha = Pilha()
    for char in input_string:
        pilha.push(char)

    reversed_string = ""

    while not pilha.is_empty():
        reversed_string += pilha.pop()

    return reversed_string


# Testes
strings = [
    "Olá, meu nome é Diana",
    "1234567890",
    "Estrutura de dados",
    
]

for string in strings:
    print(f"Original: {string}")
    print(f"Reversed: {reverse_string(string)}")
    print()
