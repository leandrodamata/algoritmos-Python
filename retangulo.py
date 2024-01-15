import math

base: float
altura: float
area: float
perim: float
diag: float

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perim = (2 * base) + (2 * altura)
diag = math.sqrt(pow(base, 2.0) + pow(altura, 2.0))

print(f"Area = {area:.4f}")
print(f"Perimetro = {perim:.4f}")
print(f"Diagonal = {diag:.4f}") 
