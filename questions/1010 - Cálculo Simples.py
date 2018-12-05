codigo1, numero1, peca1 = input().split()
codigo1 = int(codigo1)
numero1 = int(numero1)
peca1 = float(peca1)
codigo2, numero2, peca2 = input().split()
codigo2 = int(codigo2)
numero2 = int(numero2)
peca2 = float(peca2)

totalPecas1 = peca1 * numero1
totalPecas2 = peca2 * numero2
totalDeGastos = totalPecas1 + totalPecas2

print("VALOR A PAGAR: R$ {:.2f}".format(totalDeGastos))