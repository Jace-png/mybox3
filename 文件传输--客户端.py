from socket import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def main():
    try:
        cip = ent.get()
        if len(cip) == 0:  # 限制ip
            error4()  # 提示
            ent.delete(0, len(cip))

        port = ent2.get()
        if len(port) == 0:  # 限制port
            error5()
            ent2.delete(0, len(port))
        address = (cip, int(port))

        file_name = ent3.get()
        if len(file_name) == 0:
            error6()
            ent3.delete(0, len(file_name))
        file_size = 4096  # 4k

        tcp_client = socket(AF_INET, SOCK_STREAM)  # 创建套接字
        tcp_client.connect(address)  # 连接
        # 数据交互
        tcp_client.send(file_name.encode('utf8'))  # 为文件名编码 并发送到服务器
        new_file = open(file_name, 'wb')  # 新建一个文件 来存放接收到的文件
        time = 0  # 计算读取的字节数  标志位
        while True:
            res = tcp_client.recv(file_size)  # 接收文件
            print(res)
            if res:
                new_file.write(res)
                time += len(res)  # 计算接收到的字节
                # print(time)
            else:  # 如果字节数为空  表示接收失败
                if time == 0:
                    new_file.close()
                    error()
                else:
                    succeed()

                    break
                tcp_client.close()
    except:
        error3()


# -------------------------------------messagebox

def succeed():
    messagebox.showinfo('接收成功!!', message='文件接收成功!')


def error():
    messagebox.showinfo('接收失败!!', message='文件接收失败')


def error2():
    messagebox.showinfo('输入错误', message='输入有误,请检查!')


def error3():
    messagebox.showinfo('ERROR', message='404')


def error4():
    messagebox.showinfo('ERROR', message='ip为空')


def error5():
    messagebox.showinfo('ERROR', message='port为空')


def error6():
    messagebox.showinfo('ERROR', message='filename为空')


x = 0

win = Tk()  # 窗口
win.resizable(0, 0)  # 固定窗口大小不可变
win.title('文件传输')
win.geometry('400x300')

# 标签
path = Image.open('1000366.jpg')
image1 = ImageTk.PhotoImage(path)

lab0 = Label(win, image=image1, height=300, width=400)
lab1 = Label(win, text='ip', height=1, width=7)
lab2 = Label(win, text='port', height=1, width=7)
lab3 = Label(win, text='filename', height=1, width=7)

lab0.pack()
lab1.place(relx=0.2, rely=0.2)
lab2.place(relx=0.2, rely=0.3)
lab3.place(relx=0.2, rely=0.4)


# # -----------------------------------------------------------------------------------------------


def check_file():  # 窗口2

    agr = Toplevel(win)
    agr.geometry('800x300')
    agr.title('查看文件')

    cip = ent.get()
    port = 7895
    address = (cip, port)
    size = 4096

    cilent = socket(AF_INET, SOCK_STREAM)  # 创建套接字  tcp协议
    cilent.connect(address)
    # 交互
    x = str(1)
    cilent.send(x.encode('utf8'))  # 发送

    r = cilent.recv(size)  # 接收
    res = r.decode('utf8')
    with open('1.txt', 'w+', encoding='utf8')as f:
        f.write(res)
    with open('1.txt', 'r+', encoding='utf8')as f:
        a = f.read()
    # frame1 = Frame(agr,height = 100,width = 400)
    # frame1.pack()
    lab1 = Label(agr, text=a, height=4, width=100, relief='ridge')
    lab1.pack()


def check_file2():  # 窗口3

    agr = Toplevel(win)
    agr.geometry('800x300')
    agr.title('查看文件')
    cip = ent.get()
    port = 7895
    address = (cip, port)
    size = 4096

    cilent = socket(AF_INET, SOCK_STREAM)  # 创建套接字  tcp协议
    cilent.connect(address)
    # 交互
    x = str(2)
    cilent.send(x.encode('utf8'))  # 发送

    r = cilent.recv(size)  # 接收
    res = r.decode('utf8')
    with open('2.txt', 'w+', encoding='utf8')as f:
        f.write(res)
    with open('2.txt', 'r+', encoding='utf8')as f:
        a = f.read()
    lab1 = Label(agr, relief='ridge', text=a, height=4, width=100)

    lab1.pack()


def check_file3():  # 窗口4

    agr = Toplevel(win)
    agr.geometry('800x300')
    agr.title('查看文件')
    cip = ent.get()
    port = 7895
    address = (cip, port)
    size = 4096

    cilent = socket(AF_INET, SOCK_STREAM)  # 创建套接字  tcp协议
    cilent.connect(address)
    # 交互
    x = str(3)
    cilent.send(x.encode('utf8'))  # 发送

    r = cilent.recv(size)  # 接收
    res = r.decode('utf8')
    with open('3.txt', 'w+', encoding='utf8')as f:
        f.write(res)
    with open('3.txt', 'r+', encoding='utf8')as f:
        a = f.read()
    lab1 = Label(agr, text=a, relief='ridge', height=4, width=100)
    lab1.pack()


# ------------------------------------------------------------------------------------------
# 按钮
bat = Button(win, text='确定:', command=main, bg='#FFFACD')
bat.place(relx=0.2, rely=0.49, height=50, width=261)

bat3 = Button(win, text='查看图片', bg='#FFFACD', command=check_file)
bat3.place(relx=0.2, rely=0.7, height=50, width=55)

bat4 = Button(win, text='查看视频', bg='#FFFACD', command=check_file2)
bat4.place(relx=0.45, rely=0.7, height=50, width=55)

bat5 = Button(win, text='查看音频', bg='#FFFACD', command=check_file3)
bat5.place(relx=0.71, rely=0.7, height=50, width=55)

# 文本框
n = StringVar()
n.set('请输入ip地址..')
ent = Entry(win, width='25', textvariable=n)
ent.place(relx=0.4, rely=0.2)

m = StringVar()
m.set('请输入端口号..')
ent2 = Entry(win, width='25', textvariable=m)
ent2.place(relx=0.4, rely=0.3)

j = StringVar()
j.set('请输入文件名..')
ent3 = Entry(win, width='25', textvariable=j)
ent3.place(relx=0.4, rely=0.4)

win.mainloop()
# 192.168.1.29
# 2.jpg
