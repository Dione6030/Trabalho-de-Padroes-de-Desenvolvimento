from mv import MV
from interface import SistemaHospitalar

class MVAdapter(SistemaHospitalar):

    def __init__(self):
        self.mv = MV()

    def buscar_paciente(self, registro):

        print("[Adapter] Traduzindo buscar_paciente() -> localizar()")

        return self.mv.localizar(registro)