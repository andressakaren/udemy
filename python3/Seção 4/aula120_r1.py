pessoa = {}


chave = 'nome_completo'
pessoa[chave] = 'andressa'
pessoa['sobrenom'] = 'miranda'

del pessoa['sobrenom']
print(pessoa)
print(pessoa['sobrenome'])

# chaves dinamincas
# metodo get