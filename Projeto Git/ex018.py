from math import sin, cos, tan, radians
num = int(input('Digite o ângulo desejado:'))
se = sin(radians(num))
co = cos(radians(num))
ta = tan(radians(num))
print('O seno do ângulo é {:.2f}.' .format(se))
print('O coseno do ângulo é {:.2f}.' .format(co))
print('A tangente do ângulo é {:.2f}' . format(ta))
