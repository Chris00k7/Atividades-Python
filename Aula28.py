'''
Exercício
peça ao usuário para digitar o seu nome
peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    Exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultimá letra do seu nome é {}
se nada for digitado em nome ou idade:
    exiba "desculpe, você deixou campos vazios.
'''

Nome = input('Digite o seu nome ')
if Nome:
    Idade = input('Agora digite a sua idade ')
    if Idade:
        numero_de_letras = len(Nome)
        ultima_letra_nome = (Nome[::-numero_de_letras])
        primeira_letra_do_nome = (Nome[0:1])
        print(f'O seu nome é {Nome}')
        print(f'a sua idade é {Idade}')
        print(f'Seu nome invertido é {Nome[::-1]}')
        print(f'O seu nome contem {numero_de_letras} letras')
        print(f'a primeira letra do seu nome é {primeira_letra_do_nome}')
        print(f'a ultima letra do seu nome é {ultima_letra_nome}')
        if ' ' in Nome:
            print('Seu nome contem espaços')
        else:
            print('seu nome não contem espaços')
    else:
        print('Você não preencheu a sua idade')
else:
    print('desculpe, você não colocou o seu nome')