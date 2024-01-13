# xls_parser.py

import xlrd

def parse_xls(file_path, sheet_name):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_name(sheet_name)
    data = []
    for row_idx in range(1, sheet.nrows):  
        row_data = {}
        for col_idx in range(sheet.ncols):
            cell = sheet.cell(row_idx, col_idx)
            row_data[sheet.cell(0, col_idx).value] = cell.value
        data.append(row_data)
    return data
