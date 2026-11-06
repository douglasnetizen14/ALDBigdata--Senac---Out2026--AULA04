ano_nascimento = int(input('informe o ano de nascimento:  '))

idade = 2026 - ano_nascimento

if idade >= 18:
    print('voce e maior!')
else:
    print("voce e menor!")