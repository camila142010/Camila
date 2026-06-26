idade = int(input("Digite sua idade: "))

habilitacao = input("Possui habilitação? (S/N): ").upper()

if idade >= 18 and habilitacao == "S":

    print("Pode dirigir")

else:

    print("Não pode dirigir")
