import win32com.client as win32
import win32gui
import win32con

# excel = win32.Dispatch('Excel.Application')
# excel.Visible = True
# print(excel.Visible)
hwp = win32.Dispatch('HWPFrame.HwpObject')
# print(hwp)
# hwnd = win32gui.FindWindow(None, '빈 문서 1- 한컴오피스 ㅎㆍㄴ글')
# print(hwnd)
# win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
# win32gui.ShowWindow(hwnd, win32con.SW_SHOW) # 두번째 파라미터는 정수값을 갖고 있다 즉 숫자를 넣어도 됌
# hwp.InitScan()
# hwp.GetText()
# hwp.GetText()
# hwp.GetText()
# hwp.GetText()