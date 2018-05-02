# -*- coding: UTF-8 -*-
#!/usr/bin/python
import sys

class StockReporter(object):

    def __init__(self):
        self._text = ""
        self._stringVar = None

    def setStringVar(self, stringVar):
        self._stringVar = stringVar

    def addReport(self, value):
        if self._stringVar:
            tmp = self._stringVar.get()
            tmp += (value + '\n')

            self._stringVar.set(tmp)

        sys.stdout.flush()
