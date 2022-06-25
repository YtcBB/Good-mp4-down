import PySimpleGUI as sg
import sys
import you_get

def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()

url = sg.popup_get_text("请输入视频播放地址：",title = "选择地址")
path = sg.popup_get_folder("请输入下载路径：",title = "选择路径")
download(url, path)
