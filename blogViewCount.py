import webbrowser
import time

list1 = [
    "blogUrl","blogUrl","blogUrl","blogUrl","blogUrl",
]

for url in list1:
    webbrowser.open(url)
    time.sleep(2)