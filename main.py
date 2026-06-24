from sishos import Sishos
from adapter.adapter_tasy import TasyAdapter
from adapter.adapter_mv import MVAdapter


while True:
    
    print("Escolha o sistema hospitalar para buscar paciente:")

    print("1 - SISHOS")
    print("2 - TASY")
    print("3 - MV")
    print("9 - Sair")

    opcao = input("Digite o sistema desejado: ")

    match opcao:
        case "1":
            sistema = Sishos()
        case "2":
            sistema = TasyAdapter()
        case "3":
            sistema = MVAdapter()
        case "9":
            print("Saindo...")
            exit()
        case _:
            print("Opção inválida!")
            continue

    sistema.buscar_paciente(123)
    input("Pressione Enter para continuar...")