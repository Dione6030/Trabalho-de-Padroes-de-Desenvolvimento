import utilitarios as ui

from tasy import Tasy
from interface import SistemaHospitalar


class TasyAdapter(SistemaHospitalar):

    def __init__(self):
        self.tasy = Tasy()

    def buscar_paciente(self, registro):

        ui.aviso(" [Adapter] Traduzindo buscar_paciente() -> consultar() - [Método do sistema Tasy]")

        return self.tasy.consultar(registro)