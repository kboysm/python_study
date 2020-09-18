import os
import win32com.client as win32
import win32gui
os.chdir('./파이썬한글관련/한글파일/')
print(os.getcwd())
# for i in os.listdir():
#     os.rename(i , i.replace(" ","")) # 한글 파일 이름 변경

#한글파일을 열어서 pdf로 실행

hwp = win32.Dispatch('HWPFrame.HwpObject')
# # hwnd = win32gui.FindWindow(None,'빈 문서 1 - 한글')

hwp.RegisterModule('FilePathCheckDLL','FilePathCheckerModule') # 보안관련 질문을 생략
print(os.listdir())

BASE_DIR = "C:/Users/USER/Documents/python/python_study/파이썬한글관련/한글파일/"

# hwp.Open(BASE_DIR+'test(0).hwp',"HWP",None)
for i in os.listdir():
    hwp.Open(BASE_DIR+i,"HWP",None)
    hwp.HAction.GetDefault('FileSaveAsPdf',hwp.HParameterSet.HFileOpenSave.HSet)
    hwp.HParameterSet.HFileOpenSave.filename=os.path.join(BASE_DIR , i.replace('.hwp','.pdf'))
    hwp.HParameterSet.HFileOpenSave.Format='PDF'
    hwp.HAction.Execute('FileSaveAsPdf',hwp.HParameterSet.HFileOpenSave.HSet)