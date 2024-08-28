casa = float(input('Valor: R$'))
salario = float(input('Salário do Comprador: R$'))
anos = int(input('Anos de financiamento: '))
prestação = casa / (anos*12)
finan = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, anos, prestação))
if prestação <= finan:
    print('Emprestimo PODE ser concedido')
else:
    print('Emprestimo NÂO pode ser concedido')