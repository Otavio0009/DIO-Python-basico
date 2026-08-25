cargo = input("Informe seu cargo: ").lower()
salario = float(input("Informe seu salario: "))

if cargo == "programador de sistemas":
    percentualDeAlmento = salario * .30 / 100
    aumentoSalariao = salario + percentualDeAlmento

    print(f"O seu salário teve um aumento de 30%, e passou a ser {aumentoSalariao:.2f}")

elif cargo == "analista de sistemas":

    percentualDeAlmento = salario * .20 / 100
    aumentoSalariao = salario + percentualDeAlmento

    print(f"O seu salário teve um almento de 20%, e passou a ser {aumentoSalariao:.2f}")

elif cargo == "analista de banco de dados":

    percentualDeAlmento = salario * .15 / 100
    aumentoSalariao = salario + percentualDeAlmento

    print(f"O sue salário terve uma almento de 20%, e passou a ser {aumentoSalariao:.2f}")

else:
    print("Cargo inválido!")