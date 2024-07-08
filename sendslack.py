from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_slack(api_token, channel, file_path, message):
    # WebClient 인스턴스 생성
    client = WebClient(token=api_token)
    
    try:
        # 파일을 Slack 채널에 업로드하고, 해당 파일에 메시지를 추가합니다.
        response = client.files_upload_v2(
            channel=channel, 
            file=file_path,
            initial_comment=message
        )
        # 업로드 성공 메시지 출력
        print("File uploaded successfully:", response["file"]["name"])
    except SlackApiError as e:
        # 에러 처리
        print("Error uploading file:", e.response["error"])
