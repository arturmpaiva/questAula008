catetoOp = float(input("Digite o valor do cateto oposto do triangulo retangulo: "))
catetoAd = float(input("Digite o valor do cateto adjacente do triangulo retangulo: "))
hipotenusa = ((catetoOp ** 2) + (catetoAd ** 2)) ** (1/2)

print("O valor da hipotenusa do triangulo é {}".format(hipotenusa))