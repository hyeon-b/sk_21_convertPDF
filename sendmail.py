import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def file_sender(file_path,file_name):
    # 발신자, 수신자 및 SMTP서버 정보 설정
    send_email = "zxcv321258@naver.com"
    send_pwd = "rhkdgo585895"
    recv_email = "zxcv321258@naver.com"

    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(send_email,send_pwd)
    # 이메일 메시지 객체 생성 및 구성
    msg = MIMEMultipart()
    msg['Subject'] = f"{file_name}_파일 변환"
    msg['From'] = send_email
    msg['To'] = recv_email
    # 이메일 본문
    text = f"{file_name}_첨부 파일이 포함된 이메일입니다."
    email_body_part = MIMEText(text, 'plain', 'utf-8')
    msg.attach(email_body_part)
    etc_file = rf"{file_name}"
    # 파일 첨부
    with open(file_path, 'rb') as file:
        file_part = MIMEApplication(file.read())
        file_part.add_header('Content-Disposition','attachment', filename=etc_file)
        msg.attach(file_part)
    smtp.sendmail( send_email,recv_email,msg.as_string() )
    smtp.quit()


file_name = input('보내고 싶은 파일 이름 : ')
file_path = os.path.join(os.path.abspath('Save'),file_name)

file_sender(file_path,file_name)
