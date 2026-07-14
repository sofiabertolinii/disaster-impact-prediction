# calculates the somatory of the power of two for river basins
# dataset v2

dicionario = {
    "Bacia Hidrográfica do Rio Gravataí": 2,
    "Bacia Hidrográfica do Rio dos Sinos": 4,
    "Bacia Hidrográfica do Rio Caí": 8,
    "Bacia Hidrográfica do Rio Taquari-Antas": 16,
    "Bacia Hidrográfica do Alto Jacuí": 32,
    "Bacia Hidrográfica dos Rios Vacacaí – Vacacaí Mirim": 64,
    "Bacia Hidrográfica do Baixo Jacuí": 128,
    "Bacia Hidrográfica do Lago Guaíba": 256,
    "Bacia Hidrográfica do Rio Pardo": 512,
    "Bacia Hidrográfica do Rio Tramandaí": 1024,
    "Bacia Hidrográfica do Litoral Médio": 2048,
    "Bacia Hidrográfica do Rio Camaquã": 4096,
    "Bacia Hidrográfica da Lagoa Mirim e do Canal São Gonçalo": 8192,
    "Bacia Hidrográfica do Rio Mampituba": 16384,
    "Bacia Hidrográfica dos Rios Apuaê – Inhandava": 32768,
    "Bacia Hidrográfica do Rio Passo Fundo": 65536,
    "Bacia Hidrográfica dos Rios Turvo – Santa Rosa – Santo Cristo": 131072,
    "Bacia Hidrográfica do Rio Piratinim": 262144,
    "Bacia Hidrográfica do Rio Ibicuí": 524288,
    "Bacia Hidrográfica do Rio Quaraí": 1048576,
    "Bacia Hidrográfica do Rio Santa Maria": 2097152,
    "Bacia Hidrográfica do Rio Negro": 4194304,
    "Bacia Hidrográfica do Rio Ijuí": 8388608,
    "Bacia Hidrográfica do Rio da Várzea": 16777216,
    "Bacia Hidrográfica dos Rios Butuí – Icamaquã": 33554432
}

import csv
import re

municipios = {}

with open("dados.txt", "r", encoding="utf-8") as f:
    bacia_atual = None

    for linha in f:
        linha = linha.strip()

        if not linha:
            continue

        if linha in dicionario:
            bacia_atual = linha
        else:
            match = re.match(r"(.+?) \(\d+%\)", linha)
            if match:
                municipio = match.group(1)

                valor = dicionario[bacia_atual]

                if municipio not in municipios:
                    municipios[municipio] = 0

                municipios[municipio] += valor

with open("saida.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["municipio", "codigo"])

    for municipio, codigo in municipios.items():
        writer.writerow([municipio, codigo])



