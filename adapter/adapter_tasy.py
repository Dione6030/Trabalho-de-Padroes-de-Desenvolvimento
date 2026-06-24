from tasy import Tasy
from interface import SistemaHospitalar

class TasyAdapter(SistemaHospitalar):

    def __init__(self):
        self.tasy = Tasy()

    def buscar_paciente(self, registro):

        print("[Adapter] Traduzindo buscar_paciente() -> consultar()")

        return self.tasy.consultar(registro)