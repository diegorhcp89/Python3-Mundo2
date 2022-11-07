frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] *Fatiamento alternativa para fazer sem o for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

