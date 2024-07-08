from docx2pdf import convert
import os

# docx파일을 pdf 파일로 변환하는 함수
def word2pdf(upload_path, result_path, file_name):
    print(upload_path, file_name)
    print(result_path)
    print("--------------------------")
    docx_path = os.path.join(upload_path, file_name)
    pdf_path = os.path.join(result_path, file_name)

    return convert(docx_path, pdf_path)
