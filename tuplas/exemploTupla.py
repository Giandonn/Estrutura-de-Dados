tupla = (0, [1,2,3], (4,5,6), 7.0)

print(f"{tupla[1]}, tipo da variavel {type(tupla)}")

print(f"exemplo fatiamento: {tupla[:3]}")

#sobreescrevendo tupla
t1 = (1,2,3)
t2 = (4,5,6)
t1 = t1 + t2
print(t1)

#troca de 2 variaveis
var1 = 34 
var2 = 60
var2 = var2 + var1
var1 = var2 - var1
var2= var2 - var1