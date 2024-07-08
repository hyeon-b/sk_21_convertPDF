from flask import Flask, render_template, request, send_file
import os
from txt2pdf import txt2pdf
from hwp2pdf import hwp2pdf
from ppt2pdf import ppt2pdf
from word2pdf import word2pdf
from xlsx2pdf import xlsx2pdf
from image2pdf import image2pdf

UPLOAD_DIR = 'uploads'
RESULT_DIR = 'converts'

# 객체 생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_DIR, file.filename))

    only_file_name, file_type = os.path.splitext(file.filename)    

    upload_path = os.path.join(UPLOAD_DIR, file.filename)
    
    convert_file(file_type, upload_path, only_file_name)
    print("파일 변환이 완료되었습니다.")

    result_path = os.path.join(RESULT_DIR, only_file_name)
    return send_file(f'{result_path}.pdf', as_attachment=True)


def convert_file(file_type, upload_path, file_name):
    match file_type:
        case '.txt':
            txt2pdf(upload_path, RESULT_DIR, file_name)
        case '.hwp':
            hwp2pdf(upload_path, RESULT_DIR, file_name)
        case '.docx':
            word2pdf(upload_path, RESULT_DIR, file_name)
        case '.ppt' | '.pptx':
            ppt2pdf(upload_path, RESULT_DIR, file_name)
        case '.xlsx':
            xlsx2pdf(upload_path, RESULT_DIR, file_name)
        case '.png' | 'jpg':
            image2pdf(upload_path, RESULT_DIR, file_name)


if __name__ == '__main__':
    app.run(debug=True)
