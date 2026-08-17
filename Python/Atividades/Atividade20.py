usuario = input("Digite o nome do usuário: ")
senha = int(input("Digite sua senha: "))

if usuario == "procopio" and senha == 12345:
    print("Seja bem vindo!")

elif usuario == "paiva" and senha == 54321:
    print("Seja bem vindo!")

else:
    print("Usuário e senha não conferem")