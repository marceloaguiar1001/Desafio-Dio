nome = str(input('Digite uma frase: ')).strip().lower()
print('A letra a aparece no total de:', nome.lower().count('a'))
print('A letra a parece a primeira vez na posição:', nome.find('a')+1)
print('E a ùltima vez que ela aparece é na:', nome.rfind('a')+1)
