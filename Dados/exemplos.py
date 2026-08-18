import requests

url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201|201202|201203|201204|201301|201302|201303|201304|201401|201402|201403|201404|201501|201502|201503|201504|201601|201602|201603|201604|201701|201702|201703|201704|201801|201802|201803|201804|201901|201902|201903|201904|202001|202002|202003|202004|202101|202102|202103|202104|202201|202202|202203|202204|202301|202302|202303|202304|202401|202402|202403|202404|202501|202502|202503|202504|202601|202602/variaveis/4099?localidades=N3[26]&classificacao=2[all]"

r = requests.get(url)

data = r.json()  # serialização: transforma a resposta em formato que o python entende

print(data[0]["id"], "-", data[0]["variavel"])

# print(data[0]['resultados'][1]['classificacoes'][0]['categoria'])
# print(data[0]['resultados'][1]['series'][0]['serie'])

# for _ in range(len(data[0]['resultados'])):
#     print(data[0]['resultados'][_]['classificacoes'][0]['categoria'])
#     print(data[0]['resultados'][_]['series'][0]['serie'])

for _ in range(len(data[0]["resultados"])):
    dt = data[0]["resultados"][_]["series"][0]["serie"]
    with open(f"ibge_{_}.json", "w", encoding="utf-8") as f:
        f.write(str(dt))
