r = float(input('Digite quanto reais você deseja usar para compra de dólares: '))
d = float(input('Digite a cotação do dóla atualmente: '))
print('Com R${} você conseguirar comprar US${:.2f}' .format(r, r/d))