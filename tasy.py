import utilitarios as ui
import time
from paciente import Paciente


class Tasy:

    def consultar(self, cpf):

        print()
        time.sleep(1)
        print("Sistema: TASY")
        time.sleep(1)
        print()
        time.sleep(1)
        ui.aviso(f"Consultando paciente pelo CPF {cpf}...")


        paciente = Paciente(
            nome="Maria Oliveira",
            registro=cpf,
            idade=42
        )

        return paciente
    
    