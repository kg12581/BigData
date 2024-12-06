import os
import tempfile
import tkinter as tk
# coding=utf-8
import sys
import re
from collections import Counter

if sys.version_info[0] == 2:
    import Tkinter
else:
    import tkinter as Tkinter
    from tkinter import *
import random
import operator

# data = ["单慧鑫", "马振淇", "孙帅豪", "刘江华", "王彦东", "刘德凯", "聂克", "田沛雨", "马帅岩", "李汉玉",
#     "高棋", "赵正阳","冯好龙", "张六一", "张自力", "李保龙",
#     "刘锕娟", "孙胜赛", "朱伟臻", "孙梦儒", "林世文"]

data = []
streamFile = open("data.txt", "r", encoding="utf8")
while True:
    str1 = streamFile.readline()
    data.append(str1)
    if str1 == "":
        break
streamFile.close()

going = True
is_run = False

##音乐部分
import pygame.mixer


def taizou():
    pygame.mixer.init()  # 初始化音乐播放器
    pygame.mixer.music.load("抬走.mp3")  # 加载音乐文件
    pygame.mixer.music.play()  # 开始播放音乐


def lottery_roll(var1, var2):
    data = []
    streamFile = open("data.txt", "r", encoding="utf8")
    while True:
        str1 = streamFile.readline()
        data.append(str1)
        if str1 == "":
            break
    streamFile.close()

    global going
    show_member = random.choice(data)
    var1.set(show_member)
    if going:
        window.after(20, lottery_roll, var1, var2)
    else:
        var2.set('倒霉蛋是 {} ！！！'.format(show_member))
        going = True
        return


def lottery_start(var1, var2):
    global is_run
    if is_run:
        return
    is_run = True
    var2.set('幸运儿是你吗。。。')
    lottery_roll(var1, var2)
    pygame.mixer.init()  # 初始化音乐播放器
    pygame.mixer.music.load("1938.wav")  # 加载音乐文件
    pygame.mixer.music.play()  # 开始播放音乐


def lottery_end():
    global going, is_run
    if is_run:
        going = False
        is_run = False
    pygame.mixer.music.pause()


def add_name():
    name = Engye
    name = Engye.get()
    if operator.contains(name, "*"):
        # pattern = r'\d+'
        # # 匹配字符串中的数字
        # match_obj = re.findall(pattern, name)
        # t = match_obj[0]
        myname = str(name).split("*")[0]
        ti = str(name).split("*")[1]
        print(ti)
        i = 0
        while i < int(ti):
            streamFile = open("data.txt", "ab")
            lin = "\n" + myname
            streamFile.write(lin.encode("utf-8"))
            i = i + 1
            streamFile.close()
        Engye.delete(0, tk.END)
    else:

        if name:
            streamFile = open("data.txt", "ab")
            lin = "\n" + name
            streamFile.write(lin.encode("utf-8"))
            streamFile.close()
            Engye.delete(0, tk.END)


def delete_name():
    name = Engye
    name = Engye.get()
    # 创建一个临时文件
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    with open("data.txt", 'r', encoding='utf-8') as file, temp_file as temp:
        for line in file:
            if name in line:
                break
            else:
                temp.write(line.encode("utf-8"))
        # 将文件剩余的部分复制到临时文件
        for line in file:
            temp.write(line.encode("utf-8"))

    # 将临时文件重命名为原始文件
    os.rename(temp_file.name, "data2.txt")
    # 删除原始文件
    os.remove("data.txt")
    os.rename("data2.txt", "data.txt")
    Engye.delete(0, tk.END)


def show_name_list():
    root = tk.Tk()
    app = NameCounterApp(root)
    root.mainloop()


class NameCounterApp:
    def __init__(self, master):
        self.master = master
        master.title("人名检测工具")

        # 创建控件

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=20)
        self.choose_file()

        # 初始化变量
        self.file_path = None
        self.names = []

    def choose_file(self):
        # 弹出文件选择对话框，获取文件路径
        self.file_path = "data.txt"

        # 读取文件，统计人名出现次数
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.names = self.extract_names(content)
            name_counts = Counter(self.names)
            result_text = "人名出现次数：\n"
            for name, count in name_counts.items():
                result_text += f"{name}: {count}\n"

        # 显示结果
        self.result_label.config(text=result_text)

    def extract_names(self, text):
        # 从文本中提取人名，这里假设人名是由中文字符组成的
        # 你可以根据实际需求修改这个函数来提取人名
        names = []
        words = text.split()
        for word in words:
            if word.isalpha():  # 只统计字母组成的人名，你可以根据需求调整条件
                names.append(word)
        return names


if __name__ == '__main__':
    window = Tkinter.Tk()
    window.geometry('405x390+250+15')
    window.title('      随机点名')

    bg_label = Label(window, width=70, height=24, )
    bg_label.place(anchor=NW, x=0, y=0)

    var1 = StringVar(value='即 将 开 始')
    show_label1 = Label(window, textvariable=var1, justify='left', anchor=CENTER, width=17, height=3, bg='#BFEFFF',
                        font='楷体 -40 bold', foreground='black')
    show_label1.place(anchor=NW, x=21, y=20)
    var2 = StringVar(value='幸运儿是你吗。。。')
    show_label2 = Label(window, textvariable=var2, justify='left', anchor=CENTER, width=38, height=3, bg='#ECf5FF',
                        font='楷体 -18 bold', foreground='red')
    show_label2.place(anchor=NW, x=21, y=240)

    button1 = Button(window, text='开始', command=lambda: lottery_start(var1, var2), width=14, height=2, bg='#A8A8A8',
                     font='宋体 -18 bold')
    button1.place(anchor=NW, x=20, y=175)
    button2 = Button(window, text='暂停', command=lambda: lottery_end(), width=14, height=2,
                     font='宋体 -18 bold')
    button2.place(anchor=NW, x=232, y=175)

    button3 = Button(window, text='抬走', command=lambda: taizou(), width=3, height=1,
                     font='宋体 -18 bold')
    button3.place(anchor=NW, x=180, y=175)

    Engye = Entry(window, width=30)
    Engye.place(anchor=tk.NW, x=95, y=310)
    button3 = Button(window, text="添加", command=add_name)
    button3.place(anchor=tk.NW, x=21, y=310)
    button4 = Button(window, text="删除", command=delete_name)
    button4.place(anchor=tk.NW, x=350, y=310)

    button5 = Button(window, text="查看人名列表", command=show_name_list)
    button5.place(anchor=tk.NW, x=80, y=350)

    window.mainloop()
