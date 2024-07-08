import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv


def mail_sender(file_path,file_name):
    load_dotenv()
    SEND_EMAIL = os.getenv("SEND_EMAIL")
    SEND_PWD = os.getenv("SEND_PWD")
    
    # 발신자, 수신자 및 SMTP서버 정보 설정
    send_email = SEND_EMAIL
    send_pwd = SEND_PWD
    recv_email = SEND_EMAIL

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
    email_body_part = MIMEText(text)
    msg.attach(email_body_part)
    etc_file = rf"{file_name}"+".pdf"

    # 파일 첨부
    with open(file_path, 'rb') as file:
        file_part = MIMEApplication(file.read())
        file_part.add_header('Content-Disposition','attachment', filename=etc_file)
        msg.attach(file_part)
        email_string = msg.as_string()

    smtp.sendmail( send_email,recv_email,email_string)
    smtp.quit()