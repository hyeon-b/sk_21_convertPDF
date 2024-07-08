import pandas as pd
from spire.xls import *
from spire.xls.common import *
import pythoncom
import openpyxl


def xlsx2pdf(upload_path, result_path, file_name):
    pythoncom.CoInitialize()

    # Sheet names 불러오기
    names = openpyxl.load_workbook(upload_path).sheetnames
    
    # 엑셀파일에서 데이터프레임을 읽은뒤 합치기
    df = pd.DataFrame({})
    for name in names:
        temp_df = pd.read_excel(upload_path, sheet_name=name)
        temp_df['시트이름'] = name #시트이름의 날짜정보를 새로운 열로 생성
        df= pd.concat([df,temp_df])
    
    #파일로 저장
    merged_xlsx = f'uploads/{file_name}_merged.xlsx'
    df.to_excel(merged_xlsx, index=False)
    
    #Create a workbook
    workbook = Workbook()
    #Load an Excel file
    workbook.LoadFromFile(merged_xlsx)

    #Iterate through the worksheets in the file
    for sheet in workbook.Worksheets:
        print(FileExistsError)
        #Save each sheet to a separate PDF
        result_file = os.path.abspath(os.path.join(result_path, file_name)+ '.pdf')
        
        sheet.SaveToPdf(result_file)
    workbook.Dispose()

