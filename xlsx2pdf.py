from spire.xls import *
from spire.xls.common import *

def xlsx2pdf(upload_path, result_path, file_name):
    #Create a workbook
    workbook = Workbook()
    #Load an Excel file
    workbook.LoadFromFile(upload_path)

    #Iterate through the worksheets in the file
    for sheet in workbook.Worksheets:
        FileName =  sheet.Name + ".pdf"
        #Save each sheet to a separate PDF
        result_path = os.path.join(result_path, f'{FileName}.pdf')
        sheet.SaveToPdf(result_path)
    workbook.Dispose()
