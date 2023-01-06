#modulo resto
print(10 % 3)
#elevado
print(3 ** 2)
#
print((10 - 5) * 2)
print(10 ** 5 * 2)
print(10 ** (5 * 2))
print(10 / 5 * 2)
print("//////////////////////////////////////////")
produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 -  produto_2)
print(produto_1 /  produto_2)
print(produto_1 //  produto_2)
print(produto_1 * produto_2)
print(produto_1 %  produto_2)
print(produto_1 **  produto_2)

##operador de comparação

saldo = 45
saque = 20

print(saldo == saque)#igualdade
print(saldo != saque)#diferença

print(saldo > saque)#maior
print(saldo >= saque)#maior igual

print(saldo < saque)#menor
print(saldo <= saque)#menor igual


##operadores de atribuição

saldo = 500 #atribuição simples valor:500
print (saldo)
saldo += 200 #atribuição com soma valor:700
print (saldo)
saldo -= 100 #atribuição com subtração valor:600
print (saldo)
saldo /= 2 #atribuição com soma valor:300
print (saldo)
saldo //= 2 #atribuição com soma valor:150
print (saldo)
saldo %= 200 #atribuição com soma valor:150
print (saldo)
saldo *= 200 #atribuição com soma valor:30000
print (saldo)
saldo **= 200 #atribuição com soma valor:700
print (saldo)

##Operadores logicos

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite #false ##todos tem que ser verdadeira

saldo >= saque or saque <= limite #true ##so precisa de 1 verdadeiro

#operador de negação
contatos_emergencia = []
not 1000 > 1500 #True ## inverso do resultado

not contatos_emergencia #True ##lista vazia é falso

not "saque 1500;" #False

not "" #True

#Parênteses

saldo = 1000
saque = 200
limite = 100
conta_especial = True

result = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#true
print(result)
result =(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#True
print(result)

##Operadores de identidade

curso = "Curso de pyrhon"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso##True #saber se utiliza o mesmo espço de memoria

curso is not nome_curso##False

saldo is limite#true

##Operadores de associação

curso ="Curso de Python"
frutas = ["laranja","uva","limão"]
saques = [1500,100]

"Python" in curso #esta
##true
"maçã" not in frutas #não esta
##true
200 in saques
##true
