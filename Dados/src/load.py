from pathlib import Path
import json


class Load:
    def __init__(self, output_dir="json"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_json(self, nome_arquivo, data):
        """
        Método responsável por salvar os dados em arquivo json

        Atributos:
            nome_arquivo: str
            data: dict
        """
        caminho_arquivo = self.output_dir / f"{nome_arquivo}.json"

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
