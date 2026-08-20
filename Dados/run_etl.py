from src.extract import Extract
from src.load import Load

ext = Extract()
ld = Load()

dados_gerais = ext.pnadc(variaveis="todas", sexo="all")
ld.load_json("pnadc_dados_completos", dados_gerais)

dados_mulheres_desocupacao = ext.pnadc(variaveis="4099", sexo="5")
ld.load_json("pnadc_desocupacao_mulheres", dados_mulheres_desocupacao)

dados_homens_informalidade = ext.pnadc(variaveis="informalidade", sexo="homens")
ld.load_json("pnadc_informalidade_homens", dados_homens_informalidade)

dados_participacao_total = ext.pnadc(variaveis=["4096", "4099"], sexo="total")
ld.load_json("pnadc_participacao_desocupacao_total", dados_participacao_total)
