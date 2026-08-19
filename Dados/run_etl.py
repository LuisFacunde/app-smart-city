from src.extract import Extract
from src.load import Load

ext = Extract()
data = ext.pnadc()

ld = Load()
ld.load_json("pnadc", data)
