from docx2pdf import convert
import os
import pythoncom

# docx파일을 pdf 파일로 변환하는 함수
def word2pdf(upload_path, result_path, file_name):
    pythoncom.CoInitialize()

    docx_path = os.path.abspath(upload_path)
    pdf_path = os.path.abspath(os.path.join(result_path, file_name)+'.pdf')

    return convert(docx_path, pdf_path)