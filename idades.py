nome1: str
nome2: str
idade1: int
idade2: int
media: float

print("Dados da primeira pessoa: ")
nome1 = input("Nome : ")
idade1 = float(input("Idade: "))
print("Dados da segunda pessoa: ")
nome2 = input("Nome: ")
idade2 = float(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome1} e sexo {nome2} eh de {media:.1f} anos")                                                                          