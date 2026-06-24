from interface import SistemaHospitalar

class Sishos(SistemaHospitalar):

    def buscar_paciente(self, registro):
        print(f"[SISHOS] Buscando registro {registro}")

        return {
            "registro": registro,
            "nome": "João Silva"
        }