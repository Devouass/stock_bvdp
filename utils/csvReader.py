# -*- coding: UTF-8 -*-
import os.path
import json
import pandas as pd

def checkCSVExists(filePath):
    if not filePath or filePath == '':
        return False
    return os.path.isfile(filePath)

def formatJson(jsonToFormat):
    if not jsonToFormat:
        return {}

    formattedJson = {}
    for index, product in jsonToFormat.items():
        if product['Désignation'] and product['Désignation'] != 'Total':
            formattedJson[product['Désignation']] = int(product['Quantité'])

    return formattedJson


def getSellProductsArray(sellFilePath):
    if not checkCSVExists(sellFilePath):
        #TODO log erreur
        print('csv file path {p} is not valid'.format(p = achatsFilePath))
        return {}

    sellData = pd.read_csv(sellFilePath, encoding = "ISO-8859-1", delimiter = ';')
    dataToFormat = sellData.to_json(orient = 'index')

    return formatJson(json.loads(dataToFormat))
