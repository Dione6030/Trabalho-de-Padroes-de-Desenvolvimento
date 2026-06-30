import utilitarios as ui
from interface import SistemaHospitalar
from paciente import Paciente
import time


class Sishos(SistemaHospitalar):

    def buscar_paciente(self, registro):

        print("\n[SISHOS]")
        time.sleep(1)
        ui.aviso(f" [SISHOS] Buscando paciente pelo registro {registro}...")

        paciente = Paciente(
            nome="João Silva",
            registro=registro,
            idade=35
        )

        return paciente