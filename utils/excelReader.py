# -*- coding: UTF-8 -*-
import os.path
import json
import pandas as pd

def checkExcelExists(filePath):
    if not filePath or filePath == '':
        return False
    return os.path.isfile(filePath)

def formatJson(jsonToFormat):
    if not jsonToFormat:
        return {}

    formattedJson = {}
    for index, product in jsonToFormat.items():
        data = {}
        name = ''
        data['quantity'] = 0;
        for key, value in product.items():
            if key == 'Unnamed: 0':
                name = value
            elif key == 'cond.':
                data['cond'] = value
            else:
                if value:
                    data['quantity'] += int(value)
        formattedJson[name] = data

    return formattedJson


def getBuyProductsArray(achatsFilePath):
    if not checkExcelExists(achatsFilePath):
        #TODO log erreur
        print('excel file path {p} is not valid'.format(p = achatsFilePath))
        return {}

    sheetNames = pd.ExcelFile(achatsFilePath).sheet_names
    productsArray = []

    for sheetName in sheetNames:
        buyData = pd.read_excel(achatsFilePath, sheet_name = sheetName, skiprows = 4 )
        dataToFormat = buyData.to_json(orient = 'index')
        productsArray.append(formatJson(json.loads(dataToFormat)))

    return productsArray
