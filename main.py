import utilitarios as ui
import time

from sishos import Sishos
from adapter.adapter_tasy import TasyAdapter
from adapter.adapter_mv import MVAdapter

while True:

    ui.titulo("PORTAL HOSPITALAR")
    print("Escolha o sistema para buscar o paciente:\n")

    print("1 - SISHOS")
    print("2 - TASY")
    print("3 - MV")
    print("9 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    match opcao:
        case "1":
            sistema = Sishos()
        case "2":
            sistema = TasyAdapter()
        case "3":
            sistema = MVAdapter()
        case "9":
            print("\nEncerrando sistema...")
            break
        case _:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")
            continue

    print("\n" + "-" * 50)
    ui.titulo("Portal Hospitalar")
    print()
    time.sleep(1)
    print("Solicitando método: buscar_paciente() - [Interface do sistema hospitalar]")
    print("-" * 50)
    time.sleep(1)

    paciente = sistema.buscar_paciente(123)

    time.sleep(1)
    print("\n" + "=" * 50)
    ui.sucesso(" PACIENTE ENCONTRADO")
    print("=" * 50)
    time.sleep(1)
    print(paciente)
    time.sleep(1)
    print()
    ui.sucesso(" Paciente devolvido com sucesso para o sistema!")
    print()
    input("\nPressione Enter para continuar...")
    ui.limpar()