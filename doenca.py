def busca_doenca(sintoma):
    manipulador = open("doencas.txt", "r")
    for i in manipulador:
        if (sintoma in i):
            print(i)
    manipulador.close()

def add_doenca():
    while True:
        name = input("Nome da doença: ")
        descricao = input("Descricao doença: ")
        tratamento = input("Qual Tratamento:")
        sintomas = input("Qual sintoma: (Separados po vírgula)")
        f = open("doencas.txt", "r")
        content = f.readlines()
        content.append(name + ';' + descricao + ';' + sintomas + ';' + tratamento + '\n')
        f.close()
        f = open("logins.txt", "w")
        f.writelines(content)
        f.close()
        resp = input('Continua Sistema: [S/N]').upper()
        if resp == 'N':
            break
    return print('\033[43;1m'+"Doenças Adicionadas "+'\033[0;0m')

def mostrar_doenca():
    manipulador = open("doencas.txt", "r")
    for i in manipulador:
        print(i)
    manipulador.close()

