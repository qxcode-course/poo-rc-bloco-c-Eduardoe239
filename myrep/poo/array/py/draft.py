import random


listinha = []
listinha_nova = []

listitinha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = len(listitinha)

listitinha.append(10)
u = listitinha.pop()

listitinha.insert(3, 79)
r = listitinha.pop(6)

listonha = [0, 34, 56]
form = ", ".join(str(z) for z in listonha)
print(form)

j = 23
seq = list(range(j+1))

aleatorio = [random.randint(0, 25) for _ in range(5)]


p = listitinha[0]
ult = listitinha[-1]

for element in listitinha:
    print(element)

for i in range(len(listitinha)):
    print(i, listitinha[i])

z = 367
achou = False
for i in listitinha:
    if i == z:
        achou = True
        break


if z in listinha:
    print("ta na lista")


pares = [e for e in listitinha if e % 2 == 0]

quadradin = [z*z for z in listitinha]


x = 9
if x in listitinha:
    listitinha.remove(x)


x = 2
listitinha = [e for e in listitinha if e != x]




