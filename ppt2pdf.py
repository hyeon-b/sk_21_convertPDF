import os
import win32com.client
from os.path import abspath

def ppt2pdf(upload_path, result_path, file_name): 
    IN_PATH = os.path.join(upload_path, file_name) 
    OUT_PATH = os.path.join(result_path, file_name)

    #파워포인트 열기
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    
    #static 경로에 존재하는 파일 리스트
    files = os.listdir(IN_PATH)

    for file in files:
        if file.lower().endswith((".ppt", ".pptx")):    #ppt, pptx일 경우, 
            ppt_file = powerpoint.Presentations.Open(os.path.join(IN_PATH, file))   #해당 파일을 열어줌
            pre, ext = os.path.splitext(file)   #pptx.pdf로 저장되는 것을 방지하기 위해 파일이름과 확장자 분리
            ppt_file.SaveAs(os.path.join(OUT_PATH, pre + ".pdf"), 32)   #저장할 폴더에 .pdf 확장자로 저장(32: pdf파일을 의미하는 formatType)
            ppt_file.Close()
    powerpoint.Quit()   #파워포인트 종료