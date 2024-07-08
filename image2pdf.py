from fpdf import FPDF
from flask import Flask, render_template, request, send_file
import os


def image2pdf(upload_path, result_path, file_name):
    save_fileName = os.path.join(upload_path, file_name)

    # 파일명이 .jpg 또는 .png일 경우 실행
    files = os.listdir()
    
    # pdf 불러오기
    pdf = FPDF()
                
    # pdf 페이지 추가
    pdf.add_page()
                
    # 디렉토리 파일을 가로 크기 210에 맞춤
    pdf.image(save_fileName,0,0,210)
                
    # .pdf로 저장
    pdf.output(os.path.join(result_path, f'{file_name}.pdf'), "F")
        
    convert_file = os.path.join(result_path, f'{file_name}.pdf')
    
    return send_file(convert_file, as_attachment=True)
    
