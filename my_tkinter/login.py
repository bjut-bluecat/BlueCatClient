#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python3.x 导入方法
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import my_tkinter.chat
import tcp_client.client

# 创建客户端界面
root = Tk()  # 创建窗口对象的背景色


# 定义登陆Button的回调函数
def usr_log_in(name, passwd):
    # todo
    # 1.建立tcp连接 验证账号+密码
    # 2.验证失败提示信息
    # 3.验证成功显示消息 好友信息列表 我的信息
    # 3.1点击好友 进入聊天
    # 参考 ：https://www.cnblogs.com/forforever/p/12894343.html

    # 连接成功后 推出登陆界面
    client = tcp_client.client.TcpClient()
    client.send_meg(name, passwd)
    usr_sign_quit()
    my_tkinter.chat.chat()
    print('hello button')


# 注册信息的回掉函数
def usr_sign_up():
    # 新建注册窗口
    window_sign_up = tk.Toplevel(root)
    window_sign_up.geometry('400x300')
    window_sign_up.title('sign_up')

    # 注册编辑框
    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    pwd_comfirm = tk.StringVar()

    tk.Label(window_sign_up, text='账户名：').place(x=90, y=50)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=160, y=50)

    tk.Label(window_sign_up, text='密码：').place(x=90, y=100)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=160, y=100)

    tk.Label(window_sign_up, text='确认密码：').place(x=90, y=150)
    tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*').place(x=160, y=150)
    # 确认注册
    bt_confirm = tk.Button(window_sign_up, text='确定', command=signtowcg).place(x=180, y=220)


# 推出蓝猫chat
def usr_sign_quit():
    root.destroy()


def bluecat_chat():
    root.title("超越疼讯的即时通信，蓝猫聊1.0！")
    root.geometry("1000x800")  # 设置窗口大小 注意：是x 不是*
    # 增加背景图片
    # 背景 https://blog.csdn.net/weixin_39833509/article/details/88743267
    image2 = Image.open(r'../pic/bluecat2.gif')
    background_image = ImageTk.PhotoImage(image2)
    w = background_image.width()
    h = background_image.height()
    root.geometry('%dx%d+0+0' % (w, h))

    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 登陆界面 https://www.cnblogs.com/walkwaters/p/12169217.html
    tk.Label(root, text='账户：', width=4, height=1).place(x=130, y=330)
    tk.Label(root, text='密码：', width=4, height=1).place(x=130, y=370)
    var_usr_name = tk.StringVar()
    enter_usr_name = tk.Entry(root, textvariable=var_usr_name)
    enter_usr_name.place(x=170, y=330)

    var_usr_pwd = tk.StringVar()
    enter_usr_pwd = tk.Entry(root, textvariable=var_usr_pwd, show='*')
    enter_usr_pwd.place(x=170, y=370)

    # 登录 注册按钮 https://www.cnblogs.com/walkwaters/p/12169217.html
    bt_login = tk.Button(root, text='登录', command=lambda: usr_log_in(var_usr_name.get(), var_usr_pwd.get()))
    bt_login.place(x=150, y=440)

    bt_signup = tk.Button(root, text='注册', command=usr_sign_up)
    bt_signup.place(x=220, y=440)

    bt_logquit = tk.Button(root, text='退出', command=usr_sign_quit)
    bt_logquit.place(x=290, y=440)

    root.mainloop()  # 进入消息循环


if __name__ == "__main__":
    bluecat_chat()
