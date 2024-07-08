from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

def txt2pdf(upload_path, result_path, file_name):
    # file_path = os.path.join(upload_path, file_name)
    
    # 텍스트 파일 읽기
    with open(upload_path, 'r', encoding='utf-8') as txt_file:
        text = txt_file.read()
    
    result_path = os.path.join(result_path, f'{file_name}.pdf')
    # 캔버스 개체 만들기
    pdf_canvas = canvas.Canvas(result_path, pagesize=letter)
    
    # 한글 글꼴 등록하기
    pdfmetrics.registerFont(TTFont('NanumGothic', 'NanumGothic.ttf'))
    pdf_canvas.setFont('NanumGothic', 12)
    
    # 초기 위치 설정
    width, height = letter
    x = 40
    y = height - 40
    
    # 텍스트를 행으로 분할합니다
    lines = text.split('\n')
    
    for line in lines:
        # PDF에 선 긋기
        pdf_canvas.drawString(x, y, line)
        y -= 12  # 다음 줄로 이동(12포인트 아래)
        
        # 페이지가 꽉 찼는지 확인하고 필요한 경우 새 페이지 만들기
        if y < 40:
            pdf_canvas.showPage()
            pdf_canvas.setFont('NanumGothic', 12)
            y = height - 40
    
    # PDF 파일 저장
    pdf_canvas.save()