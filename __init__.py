import sys
from DiagnosticoRapido import login, doenca
if __name__ == '__main__':
    while True:
        login.cadastrar()
        print(" --------< DIAGNOSTICO RÁPIDO >------- ")
        print("=-="*13)
        print("1.Busca Por Sintoma \n2.Ver Todas Doenças\n3.Adicionar Doença\n0.Exit/Quit")
        print("=-="*13)
        opcao = int(input("Escolha Uma Opção: "))
        while opcao > 3 or opcao < 0:
            opcao = int(input("Escolha Uma Opção Novamente: "))
        if opcao == 1:
            sintoma = input("Qual o sintoma:")
            doenca.busca_doenca(sintoma)
        elif opcao == 2:
            doenca.mostrar_doenca()
        elif opcao == 3:
            doenca.add_doenca()
        elif opcao == 0:
            print("---Programa finalizado---")
            sys.exit()
        #Parado do programa
        resp = input('Continua Sistema: [S/N]').upper()
        if resp == 'N':
            print("---Programa finalizado---")
            break
