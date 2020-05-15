from datetime import datetime, timedelta
import math

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]


def calcular_preco(inicial, final):
    inicial = datetime.fromtimestamp(inicial)
    final = datetime.fromtimestamp(final)

    if inicial.hour >= 22 or final.hour <= 6:
        return 0.36

    if final.hour >= 22:
        final = datetime(final.year, final.month, final.day, 22)

    if inicial.hour < 6:
        inicial = datetime(inicial.year, inicial.month, inicial.day, 6)

    duracao = math.floor((final - inicial).seconds / 60)
    preco_final = duracao * 0.09 + 0.36
    return preco_final


def listar(records):

    resultados = []

    for registro in records:
        i = 0
        for resultado in resultados:
            if resultado['source'] == registro['source']:
                i = 1
                valor_anterior = resultado['total']
                preco = calcular_preco(registro['start'], registro['end'])
                preco_atualizado = round((valor_anterior + preco), 2)
                resultado['total'] = preco_atualizado

        if i == 0:
            preco = calcular_preco(registro['start'], registro['end'])
            preco_arredondado = round(preco, 2)
            resultados.append(
                {'source': registro['source'], 'total': preco_arredondado})

    return resultados


def classify_by_phone_number(records):

    resultado_final = sorted(
        listar(records), key=lambda resultado: resultado['total'], reverse=True)

    return resultado_final


print(classify_by_phone_number(records))