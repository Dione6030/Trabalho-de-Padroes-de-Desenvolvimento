import utilitarios as ui
import time

from paciente import Paciente

class MV:

    def localizar(self, codigo):

        print()
        time.sleep(1)
        print("Sistema: MV")
        time.sleep(1)
        print()
        time.sleep(1)
        ui.aviso(f" [MV] Localizando paciente pelo código {codigo}...")
       
        return Paciente(
            "Pedro Souza",
            codigo,
            28
        )