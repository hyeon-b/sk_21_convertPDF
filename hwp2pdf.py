import win32com.client as win
import os

def hwp2pdf(upload_path, result_path, file_name):
    # 변환한 파일을 저장하는 경로
    File_save_path = os.path.join(result_path, file_name)

    # 한글 프로그램 실행
    hwp = win.gencache.EnsureDispatch("HWPFrame.HwpObject")

    # 변환할 파일 열기
    hwp.Open(upload_path)
    

    #HWP변수에 한글 보안 모듈 적용
    hwp.RegisterModule('FilePathCheckDLL', 'SecurityModule')

    # 파일 저장 액션의 파라미터
    hwp.HAction.GetDefault("FileSaveAs_S", hwp.HParameterSet.HFileOpenSave.HSet)
    
    # 파일 저장시 확장자를 pdf로 지정
    hwp.HParameterSet.HFileOpenSave.filename = os.path.join(File_save_path , file_name + ".pdf")
    # 파일 저장시 포맷을 pdf로 설정
    hwp.HParameterSet.HFileOpenSave.Format = "PDF"
    
    # 설정한 값으로 프로그램 실행
    hwp.HAction.Execute("FileSaveAs_S", hwp.HParameterSet.HFileOpenSave.HSet)
    hwp.Quit()# 종료