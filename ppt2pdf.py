import os
import win32com.client
from os.path import abspath
import pythoncom

def ppt2pdf(upload_path, result_path, file_name): 
    IN_PATH = upload_path 
    OUT_PATH = os.path.join(result_path, file_name)

    #파워포인트 열기
    powerpoint = win32com.client.Dispatch("Powerpoint.Application", pythoncom.CoInitialize()) 

    ppt_file = powerpoint.Presentations.Open(upload_path)
    ppt_file.SaveAs(f'{OUT_PATH}.pdf', 32)   #저장할 폴더에 .pdf 확장자로 저장(32: pdf파일을 의미하는 formatType)
    ppt_file.Close()

    powerpoint.Quit()   #파워포인트 종료
    