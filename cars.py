import requests
import cloudscraper
from bs4 import BeautifulSoup

class info:
    def __init__(self, marca, modelo, importado, ano, cor, potencia, combustivel, chassi, motor, passageiros, uf, municipio, segmento, especie_veiculo, local_emissao):
        self.marca = marca
        self.modelo = modelo
        self.importado = importado
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.combustivel = combustivel
        self.chassi = chassi
        self.motor = motor
        self.passageiros = passageiros
        self.uf = uf
        self.municipio = municipio
        self.segmento = segmento
        self.especie_veiculo = especie_veiculo
        self.local_emissao = local_emissao

ls_old = []
bars = "-" * 40


scraper = cloudscraper.create_scraper()

sign = str(input("Digite a placa do veículo: ")).upper()

r = scraper.get(f'https://www.keplaca.com/placa?placa-fipe={sign}')
soup = BeautifulSoup(r.text, 'html.parser')

lines = soup.find_all('td')
for line in lines:
    line = str(line)
    ls_old.append(line)

marca = '-'
modelo = '-'
importado = '-'
ano = '-'
cor = '-'
potencia = '-'
combustivel = '-'
chassi = '-'
uf = '-'
municipio = '-'
segmento = '-'

for item in ls_old:
    if "Marca:" in item:
        marca = ls_old[ls_old.index(item) + 1][4:-5]
    elif "b>Modelo:" in item:
        modelo = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Importado:" in item:
        importado = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Ano:" in item:
        ano = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Cor:" in item:
        cor = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Potencia:" in item:
        potencia = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Combustível:" in item:
        combustivel = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Chassi:" in item:
        chassi = ls_old[ls_old.index(item) + 1][4:-5]
    elif "UF:" in item:
        uf = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Município:" in item:
        municipio = ls_old[ls_old.index(item) + 1][4:-5]
    elif "Segmento:" in item:
        segmento = ls_old[ls_old.index(item) + 1][4:-5]

auto = info(marca, modelo, importado, ano, cor, potencia, combustivel, chassi, None, None, uf, municipio, segmento, None, None)

print(f"""{bars}
Info sobre veículo com a placa '{sign}':
|Marca: {auto.marca}
|Modelo: {auto.modelo}
|Importado?: {auto.importado}
|Ano: {auto.ano}
|Cor: {auto.cor}
|Potência: {auto.potencia}
|Tipo de Combustível: {auto.combustivel}
|Chassi: {auto.chassi}
|UF: {auto.uf}
|Município: {auto.municipio}
|Tipo: {auto.segmento}
{bars}""")
