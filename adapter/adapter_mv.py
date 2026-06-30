import utilitarios as ui
from mv import MV
from interface import SistemaHospitalar

class MVAdapter(SistemaHospitalar):

    def __init__(self):
        self.mv = MV()

    def buscar_paciente(self, registro):

        ui.aviso(" [Adapter] Traduzindo buscar_paciente() -> localizar() - [Método do sistema MV]")

        return self.mv.localizar(registro)