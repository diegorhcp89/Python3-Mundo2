nome = str(input('Qual é o seu nome? '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Aline':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))