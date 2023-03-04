import pickle
import cor
from time import sleep


def menu():
    print('=' * 40)
    print(f'{cor.cor(4)}MENU{cor.cor(0)}'.center(49))
    print('=' * 40)
    print(f'1 - Ver pessoas cadastradas '
          f'\n2 - Dados Detalhados '
          f'\n3 - Cadastrar novas pessoas'
          f'\n4 - Apagar pessoa'
          f'\n5 - Excluir dados'
          f'\n6 - Sair do programa')


def main():
    while True:
        menu()
        print('=' * 40)
        try:
            x = int(input('Opção: '))
            if x == 1:
                sleep(0.5)
                cadastrados()
                sleep(1)
            if x == 2:
                sleep(0.5)
                especifico()
                sleep(1)
            if x == 3:
                sleep(0.5)
                novo()
                sleep(1)
            if x == 4:
                sleep(0.5)
                apagar()
                sleep(1)
            if x == 5:
                sleep(0.5)
                excluir()
                sleep(1)
            if x == 6:
                sleep(0.5)
                sair()
                break
        except(KeyboardInterrupt, TypeError):
            print(f'{cor.cor(1)}ERRO! NAO HOUVE COMANDO{cor.cor(0)}')
        except(ValueError):
            print(f'{cor.cor(1)}VALOR INVALIDO{cor.cor(0)}')


def cadastrados():
    print('=' * 40)
    print(f'{cor.cor(2)}VER PESSOAS CADASTRADAS{cor.cor(0)}'.center(49))
    with open('dados.pickle', 'rb') as f:
        lista = pickle.load(f)
    for c in range(0, len(lista)):
        x = len(lista[c]['Nome'])
        print(f'{c + 1} - {lista[c]["Nome"]}', end='')
        print(f'{lista[c]["Idade"]} Anos'.rjust(36 - x))


def novo():
    print('=' * 40)
    print(f'{cor.cor(2)}CADASTRAR NOVAS PESSOAS{cor.cor(0)}'.center(49))
    print('=' * 40)
    with open('dados.pickle', 'rb') as f:
        lista = pickle.load(f)
    while True:
        dados = {}
        while True:
            nome = input("Nome: ")
            if nome.isalpha():
                dados['Nome'] = nome
                break
            else:
                print(f'{cor.cor(1)}Por favor, insira um Nome valido.{cor.cor(0)}')
        while True:
            idade = input('Idade: ')
            if idade.isnumeric():
                dados['Idade'] = int(idade)
                break
            else:
                print(f'{cor.cor(1)}Por favor, insira uma Idade valida.{cor.cor(0)}')
        dados['CPF'] = input('CPF: ')
        dados['Email'] = input('Email: ')
        dados['Telefone'] = input('Telefone: ')
        lista.append(dados)
        opcao = input('Deseja cadastrar outra pessoa? [S/N] ').strip().lower()
        if opcao == 'n':
            break
    with open('dados.pickle', 'wb') as f:
        pickle.dump(lista, f)


def especifico():
    with open('dados.pickle', 'rb') as f:
        lista = pickle.load(f)
    print('=' * 40)
    print(f'{cor.cor(2)}Dados Detalhados{cor.cor(0)}'.center(49)) 
    for c in range(0, len(lista)):
        x = len(lista[c]['Nome'])
        print(f'{c + 1} - {lista[c]["Nome"]}', end='')
        print(f'{lista[c]["Idade"]} Anos'.rjust(36 - x))
    print('=' * 40)
    while True:
        try:
            escolha = int(input('Dados de quem deve ser mostrado? [999 para cancelar] '))
            if escolha == 999:
                break
            if escolha > len(lista):
                print(f'{cor.cor(1)}ERRO, PESSOA NÃO ENCONTRADA.{cor.cor(0)}')
                continue
        except(ValueError, TypeError, KeyboardInterrupt, IndexError):
            print(f'{cor.cor(1)}ERRO, DIGITE UM VALOR CORRESPONDENTE A UMA PESSOA CADASTRADA.{cor.cor(0)}')
        else:
            print('=' * 40)
            print(f'{cor.cor(2)}DADOS DE {(lista[escolha - 1]["Nome"])}{cor.cor(0)}'.center(49))
            for c, i in lista[escolha - 1].items():
                print(f'{c}', end='')
                print(f'{i}'.rjust(40 - len(c)))
            break


def excluir():
    while True:
        confim = input(f'{cor.cor(1)}OS DADOS SERÃO EXCLUIDOS PERMANENTEMENTE, DESEJA DELETA-LOS? [S/N]{cor.cor(0)} ').strip()[0].upper()
        if confim == 'S':
            print(f'{cor.cor(3)}Dados Excluidos com sucesso!{cor.cor(0)}'.center(49))
            with open('dados.pickle', 'rb') as f:
                lista = pickle.load(f)
            del lista
            with open('dados.pickle', 'wb') as f:
                pickle.dump([], f)
            break
        if confim == 'N':
            print(f'{cor.cor(3)}Ação cancelada.{cor.cor(0)}')
            break
        else:
            print(f'{cor.cor(3)}DIGITE APENAS SIM OU NÃO.{cor.cor(0)}')
            continue


def apagar():
    print('=' * 40)
    print(f'{cor.cor(2)}APAGAR PESSOA{cor.cor(0)}'.center(49))
    with open('dados.pickle', 'rb') as f:
        lista = pickle.load(f)
    while True:
        for c in range(0, len(lista)):
            x = len(lista[c]['Nome'])
            print(f'{c + 1} - {lista[c]["Nome"]}', end='')
            print(f'{lista[c]["Idade"]} Anos'.rjust(36 - x))
        dell = input('Quem deseja apagar? [999 para cancelar]')
        if not dell.isdigit():
            print(f'{cor.cor(1)}ERRO! Digite um número válido.{cor.cor(0)}')
            continue
        dell = int(dell)
        if dell == 999:
            print(f'{cor.cor(3)}Ação cancelada.{cor.cor(0)}')
            break
        try:
            print(f'Os dados de: {lista[dell - 1]["Nome"]} foram apagados')
            lista.pop(dell - 1)
        except(IndexError, KeyboardInterrupt):
            print(f'{cor.cor(1)}Nao foi possivel encontrar essa pessoa.{cor.cor(0)}')
            continue
        p = input('Parar? [S/N]').strip()[0].lower()
        if p == 's':
            print(f'{cor.cor(3)}Ação cancelada.{cor.cor(0)}')
            break
    with open('dados.pickle', 'wb') as f:
        pickle.dump(lista, f)


def sair():
    print('=' * 40)
    print('PROGRAMA ENCERRADO'.center(40))
    print('=' * 40)
