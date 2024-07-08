# PDF로 변환 완료된 PDF파일 영어로 번역
from flask import Flask, render_template, request, send_file
import os
import fitz  # PyMuPDFimport io
import io
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('uploads', file.filename))

        # PDF 파일을 로드
        pdf_path = os.path.join('uploads', file.filename)
        document = fitz.open(pdf_path)
        translator = Translator()

        # 번역된 PDF를 저장할 버퍼 생성
        output_pdf_buffer = io.BytesIO()
        pdf_canvas = canvas.Canvas(output_pdf_buffer, pagesize=letter)

        # 각 페이지의 텍스트를 번역
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text = page.get_text("text")

            translated_text = translator.translate(text, dest='en').text

            # 초기 위치 설정
            width, height = letter
            x = 40
            y = height - 40

            # 번역된 텍스트를 줄 단위로 나누어 PDF에 작성
            lines = translated_text.split('\n')
            for line in lines:
                pdf_canvas.drawString(x, y, line)
                y -= 12
                if y < 40:
                    pdf_canvas.showPage()
                    y = height - 40

            pdf_canvas.showPage()  # 각 페이지를 올바르게 저장

        pdf_canvas.save()
        output_pdf_buffer.seek(0)

        # 번역된 PDF를 파일로 저장
        with open('result_en.pdf', 'wb') as output_pdf_file:
            output_pdf_file.write(output_pdf_buffer.getbuffer())

        return render_template('result.html', file_name=file.filename)

@app.route('/download_report')
def download_report():
    return send_file('result_en.pdf', as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)