import requests


class Extract:

    SEXO = {
        "total": "6794",
        "homens": "4",
        "mulheres": "5",
        "todos": "all",
        "all": "all",
    }

    VARIAVEIS = {
        "desocupacao": "4099",
        "participacao": "4096",
        "informalidade": "12466",
        "todas": "4096|4099|12466",
    }

    def __init__(self):
        self.base_url = "https://servicodados.ibge.gov.br/api/v3/agregados"

    def _tratar_variaveis(self, variaveis):
        """
        Converte strings, listas ou nomes do dicionário no formato esperado pela URL (ex: '4096|4099').
        """
        if isinstance(variaveis, list):
            codigos = [self.VARIAVEIS.get(str(v).lower(), str(v)) for v in variaveis]
            return "|".join(codigos)

        var_str = str(variaveis).lower()
        return self.VARIAVEIS.get(var_str, str(variaveis))

    def _tratar_sexo(self, sexo):
        """
        Converte código ou nome amigável para o formato do IBGE.
        """
        sexo_str = str(sexo).lower()
        return self.SEXO.get(sexo_str, str(sexo))

    def pnadc(self, variaveis, sexo, localidade="N3[26]", periodos=None):
        """
        Extrai dados da tabela 4093 da PNAD Contínua do IBGE.
        Parâmetros:
            variaveis: código(s) da variável (ex: '4099', ['4096', '4099'] ou 'desocupacao')
            sexo: categoria de sexo ('total', 'homens', 'mulheres', 'all' ou códigos '6794', '4', '5')
            localidade: código de localidade (default 'N3[26]' - Pernambuco)
            periodos: string com os períodos desejados (default: série histórica de 2012 a 2026)
        """
        if periodos is None:
            periodos = (
                "201201|201202|201203|201204|201301|201302|201303|201304|"
                "201401|201402|201403|201404|201501|201502|201503|201504|"
                "201601|201602|201603|201604|201701|201702|201703|201704|"
                "201801|201802|201803|201804|201901|201902|201903|201904|"
                "202001|202002|202003|202004|202101|202102|202103|202104|"
                "202201|202202|202203|202204|202301|202302|202303|202304|"
                "202401|202402|202403|202404|202501|202502|202503|202504|"
                "202601|202602"
            )

        var_formatada = self._tratar_variaveis(variaveis)
        sexo_formatado = self._tratar_sexo(sexo)

        url = f"{self.base_url}/4093/periodos/{periodos}/variaveis/{var_formatada}?localidades={localidade}&classificacao=2[{sexo_formatado}]"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
