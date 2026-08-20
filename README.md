# Projeto de Engenharia de Dados - ETL

## Integrantes do grupo

1. André Felipe da Silva Braga - afsb@cesar.school
2. Dayvid Cristiano - dcvs2@cesar.school
3. Deyvison Conrado - dmc2@cesar.school
4. Jennifer Cristine - jclc2@cesar.school
5. Letícia Gabriella - lgcs@cesar.school
6. Levi Moraes - lmma@cesar.school
7. Luis Henrique Facunde da Silva - lhfs@cesar.school
8. Manuele Macêdo - mmps2@cesar.school
9. Maria Aparecida - maers@cesar.school
10. Peterson Jesus Feitosa de Melo - pjfm@cesar.school
11. Rhaldney Robert - rrcd@cesar.school
12. Victor César Matias da Silva - vcms@cesar.school

---

## Sobre o projeto

Este projeto foi desenvolvido para a disciplina de Engenharia de Dados e Big Data e tem como objetivo implementar um processo de ETL (Extract, Transform and Load) utilizando dados públicos disponibilizados pelo IBGE.

Entre os indicadores utilizados estão:

- Taxa de participação na força de trabalho;
- Taxa de desocupação;
- Taxa de informalidade;
- Dados segmentados por sexo.

---

## Tecnologias utilizadas

- Python
- Requests
- API de dados do IBGE
- JSON
- Ambiente virtual (venv)

---

## Configuração de ambiente

## Windows

Criação do venv
```bash
python -m venv .venv
```

Ativação do venv

```bash
.venv\Scripts\activate
```

## Linux/Mac

Criação do venv
```bash
python3 -m venv .venv
```

Ativação do venv
```bash
source .venv/bin/activate
```

## Instalação de dependências

Com a venv ativada, execute:
```bash
pip install -r requirements.txt
```

## Executar o projeto

Com a venv ativada, execute:
```bash
python run_etl.py
```
