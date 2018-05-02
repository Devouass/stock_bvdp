# -*- coding: UTF-8 -*-
import os.path
import os
import json
import pandas as pd

def checkExcelExists(filePath):
    if not filePath or filePath == '':
        return False
    return os.path.isfile(filePath)

def saveAsExcel(products, filePath):
    if checkExcelExists(filePath):
        os.remove(filePath)

    productsToConvert = {
        'products' : []
    }
    for name, product in products.items():
        setPackage = True
        if product.getDiv() == 1:
            setPackage = False

        productsToConvert['products'].append({
            'name' : name,
            'achat': product.getAchat() if setPackage else None,
            'cond': product.getDiv(),
            'achat unitaire': product.getUnitaryAchat(),
            'stock': product.getStock() if setPackage else None,
            'stock unitaire': product.getUnitaryStock()
        })

    data = pd.DataFrame(productsToConvert['products'])
    print('data is')
    print('{d}'.format(d = data))

    writer = pd.ExcelWriter(filePath, engine='xlsxwriter')
    data.to_excel(writer, columns = ['name', 'cond', 'achat', 'achat unitaire', 'stock', 'stock unitaire'], sheet_name='Stock')
    worksheet = writer.sheets['Stock']
    workbook = writer.book;
    cell_format = workbook.add_format()
    cell_format.set_center_across()
    worksheet.set_column('B:B', 18)
    worksheet.set_column('E:E', 18, cell_format)
    worksheet.set_column('G:G', 18)
    writer.save()
