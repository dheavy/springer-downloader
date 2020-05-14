#!/usr/bin/env python
import xlrd
import requests
import shutil

wb = xlrd.open_workbook('./springer.xlsx')
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    if i > 253:
        name = sheet.cell_value(i, 0).replace('/', '-')
        url = sheet.cell_value(i, 17)
        suffix = url[url.find('org/') + 4:] + '.pdf'
        url = 'https://link.springer.com/content/pdf/' + suffix
        print(str(i) + ' - ' + name + ' - ' + url)
        r = requests.get(url, stream=True)
        with open('./downloads/' + name + '.pdf', 'wb') as f:
            shutil.copyfileobj(r.raw, f)
