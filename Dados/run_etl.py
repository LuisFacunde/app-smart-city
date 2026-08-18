from Dados.src.extract import Extract
from Dados.src.load import Load

ext = Extract()
data = ext.pnadc()

ld = Load()
ld.load_json("pnadc", data)
