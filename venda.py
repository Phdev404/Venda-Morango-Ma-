peso_morango = input('Quantos quilos de morango você deseja ? :')
peso_morango = int(peso_morango)
mult_morango1 = 4.5
mult_morango2 = 3.2
mult_maca1 = 2.8
mult_maca2 = 1.8


if peso_morango <=5:
  peso_morango = int(peso_morango * mult_morango1)
  
else:
  peso_morango = int(peso_morango * mult_morango2)

peso_maca = input('Quantos quilos de maçã você deseja ? :')
peso_maca = int(peso_maca)

if peso_maca <=5:
  peso_maca = int(peso_maca * mult_maca1)
else:
  peso_maca = int(peso_maca * mult_maca2)
  
valor_total = int(peso_maca + peso_morango)
peso_total = int(peso_maca + peso_morango)
valor_cobrado = valor_total - (valor_total * 10/100)
if valor_total > 25 or peso_total >8:
  print("Valor da Compra: "+"R$" '{:.2f}'.format(valor_total ) )
  print("Valor do desconto:" '{:.2f}'.format(valor_total * 10/100  ))
  print("Valor cobrado " '{:.2f}'.format(valor_cobrado))
  print("Voce está pagando R$"+ str(peso_maca) +" por kg de maçã e R$"+ str(peso_morango)+" por kg de morango ")
   