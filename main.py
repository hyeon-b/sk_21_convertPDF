from flask import Flask, render_template, request, send_file
import os
from txt2pdf import txt2pdf
from hwp2pdf import hwp2pdf
from ppt2pdf import ppt2pdf
from word2pdf import word2pdf
from xlsx2pdf import xlsx2pdf
from image2pdf import image2pdf

UPLOAD_PATH = 'uploads'
RESULT_PATH = 'converts'

# 객체 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_PATH, file.filename))

    file_type = os.path.splitext(file.filename)[1]
    
    pdf_file = convert_file(file.filename)
    print("파일 변환이 완료되었습니다.")

    return send_file(pdf_file, as_attachment=True)


def convert_file(file_name):
    match file_name:
        case '.txt':
            txt2pdf(UPLOAD_PATH, RESULT_PATH, file_name)
        case '.hwp':
            hwp2pdf(UPLOAD_PATH, RESULT_PATH, file_name)
        case '.docx':
            word2pdf(UPLOAD_PATH, RESULT_PATH, file_name)
        case '.ppt' | '.pptx':
            ppt2pdf(UPLOAD_PATH, RESULT_PATH, file_name)
        case '.xlsx':
            xlsx2pdf(UPLOAD_PATH, RESULT_PATH, file_name)
        case '.png' | 'jpg':
            image2pdf(UPLOAD_PATH, RESULT_PATH, file_name)


if __name__ == '__main__':
    app.run(debug=True)
