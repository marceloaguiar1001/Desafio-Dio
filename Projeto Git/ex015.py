dia = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos quilômetros foram pecorridos?'))
diaria = dia * 60
Kilometragem = km * 0.15
print('O total a pagar é R${:.2f}'.format(diaria + Kilometragem))
