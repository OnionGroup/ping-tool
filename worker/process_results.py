# -*- coding: utf-8 -*-

from pyping.core import Response
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

from datetime import datetime
from string import ascii_uppercase


headers = ["כינוי", "שם השרת", "סטטוס", "זמן ממוצע (ms)", "זמן מינימלי (ms)", "זמן מקסימלי (ms)"]
header_font = Font(bold=True, size=20)
cell_font = Font(size=16)
centered = Alignment(horizontal="center")


def process_results(nicknames, responses):
    export_to_excel(nicknames, responses)


def set_header(cell):
    cell.font = header_font
    cell.alignment = centered


def set_success(cell):
    cell.font = Font(color="00FF00", size=16)


def set_failure(cell):
    cell.font = Font(color="FF0000", size=16)


def export_to_excel(nicknames, responses):
    wb = Workbook()
    sheet = wb.active

    for i in range(len(headers)):
        current_cell = ascii_uppercase[i] + "1"
        sheet[current_cell] = headers[i]
        set_header(sheet[current_cell])
        sheet.column_dimensions[ascii_uppercase[i]].width = 30

        for j in range(2, len(responses) + 2):
            styled_cell = sheet[ascii_uppercase[i] + str(j)]
            styled_cell.font = cell_font
            styled_cell.alignment = centered

    for i in range(len(responses)):
        row = str(i + 2)
        res = responses[i]

        sheet["A" + row] = nicknames[i][0]
        sheet["B" + row] = nicknames[i][1]

        if not isinstance(res, Response):
            sheet["C" + row] = "השרת אינו קיים/פועל"
            set_failure(sheet["C" + row])
            continue

        if res.ret_code != 0:
            sheet["C" + row] = "השרת אינו מגיב"
            set_failure(sheet["C" + row])
            continue

        sheet["C" + row] = "פעיל"
        set_success(sheet["C" + row])

        sheet["D" + row] = res.avg_rtt
        sheet["E" + row] = res.min_rtt
        sheet["F" + row] = res.max_rtt

    date_string = datetime.now().date().strftime("%d-%m-%Y")
    wb.save("../output/{}.xlsx".format(date_string))
