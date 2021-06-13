import xlwt
from xlwt import Workbook
import script3

def excel_database():  
    # Workbook is created
    wb = Workbook()

    path="location "

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    sheet1.write(0,1, 'Mobile No')
    sheet1.write(0,2, 'Email-ID')
    sheet1.write(0,3, 'FilePath Location')
    sheet1.write(1, 1, script3.mobile_selector())
    sheet1.write(1, 2, script3.email_selector())
    sheet1.write(1, 3, path)
    #sheet1.write(0, 4, 'RAJPUR ROAD')
    #sheet1.write(0, 5, 'CLOCK TOWER')
    
    wb.save('CVdatabase.xls')