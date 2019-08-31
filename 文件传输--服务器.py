from socket import *
import pymysql
from threading import Thread


def file_server(file_name):  # 读取文件
    try:
        files = open(file_name, 'rb')  # 读取二进制文件
        mes = files.read()
        files.close()
        return mes
    except:
        print('hello')


# 初始化
myname = getfqdn(gethostbyname(''))
xip = gethostbyname(myname)  # 获取本地ip
cip = xip
port = 7895
address = (cip, port)
size = 4096

tcp_socket = socket(AF_INET, SOCK_STREAM)  # 创建套接字  tcp协议
tcp_socket.bind(address)  # 绑定ip,端口
x = tcp_socket.listen(128)  # 开始监听


def accept1():
    while True:
        con, cip = tcp_socket.accept()  # 等待数据
        file_name = con.recv(size)  # 接收数据
        res = file_name.decode('utf8')
        print(res)
        print('----------------------------------------------')
        mes = file_server(res)  # 调用读取文件的函数,读取用户下载的文件
        # print(mes)
        if mes:
            con.send(mes)  # 不为空的情况发送
            con.close()
        if res == str(1) or str(2) or str(3):
            break


# accept1()

def accept2():
    while True:
        con, cip = tcp_socket.accept()  # 等待数据
        file_type = con.recv(size)
        res = file_type.decode('utf8')
        if res == '1':
            y = image_file()
            con.send(y.encode('utf8'))
        elif res == '2':
            z = video_file()
            con.send(z.encode('utf8'))
        elif res == '3':
            j = music_file()
            con.send(j.encode('utf8'))
        else:
            con.close()


def image_file():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='jace111', db='file')
    cur = conn.cursor()

    cur.execute('select * from picture_file')

    row = cur.fetchall()
    a = str(tuple(row))

    cur.close()
    conn.close()
    return a


def video_file():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='jace111', db='file')
    cur = conn.cursor()

    cur.execute('select * from video_file')

    row = cur.fetchall()
    a = str(tuple(row))

    cur.close()
    conn.close()
    return a


def music_file():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='jace111', db='file')
    cur = conn.cursor()

    cur.execute('select * from music_file')

    row = cur.fetchall()
    a = str(tuple(row))
    cur.close()
    conn.close()
    return a


accept1()
accept2()
try:
    if __name__ == '__main__':
        t1 = Thread(target=accept1)
        t2 = Thread(target=accept2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

except:
    pass
