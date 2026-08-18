class Load:
    def __init__(self):
        pass

    def load_json(self, nome_arquivo: str, data: list):
        """
        Método de extração de dados do PNAPC

        Atributos:
            nome_arquivo: string
            data: list (resultada do request da API do IBGE)
        """
        with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
            f.write(str(data))
