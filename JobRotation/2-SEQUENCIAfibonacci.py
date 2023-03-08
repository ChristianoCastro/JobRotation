# Define a função para calcular a sequência de Fibonacci
def fibonacci(n):
    # Define as condições para os primeiros dois termos
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso contrário, aplica a fórmula de Fibonacci recursivamente
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Solicita ao usuário que informe um número
num = int(input("Informe um número inteiro: "))

# Verifica se o número informado pertence à sequência de Fibonacci
pertence = False
i = 0
while fibonacci(i) <= num:
    if fibonacci(i) == num:
        pertence = True
        break
    i += 1

# Exibe a mensagem de acordo com o resultado da verificação
if pertence:
    print(f"\nO número {num} pertence à sequência de Fibonacci!")
else:
    print(f"\nO número {num} NÃO pertence à sequência de Fibonacci!")
