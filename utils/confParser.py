# -*- coding: UTF-8 -*-

import json

class ConfParser(object):

    __instance = None
    def __new__(cls):
        if ConfParser.__instance is None:
            ConfParser.__instance = object.__new__(cls)
        return ConfParser.__instance

    def __init__(self):
        self._buyConfigPath = 'config/import.json'
        self._sellConfigPath = 'config/vente.json'
        self._formattageConfigPath = 'config/formattageResult.json'
        self._importConfigFile = None
        self._sellConfigFile = None
        self._formattageProperties = None

    def getBuyProductProperties(self, productName):
        if not self._importConfigFile:
            with open(self._buyConfigPath, encoding='utf-8') as f:
                self._importConfigFile = json.load(f)

        return self._importConfigFile[productName] if productName in self._importConfigFile  else {}

    def getSellProductProperties(self, productName):
        if not self._sellConfigFile:
            with open(self._sellConfigPath, encoding='utf-8') as f:
                self._sellConfigFile = json.load(f)

        return self._sellConfigFile[productName] if productName in self._sellConfigFile  else {}

    def getFormattageProperties(self, productName):
        if not self._formattageProperties:
            with open(self._formattageConfigPath, encoding='utf-8') as f:
                self._formattageProperties = json.load(f)

        return self._formattageProperties[productName] if productName in self._formattageProperties  else {}
