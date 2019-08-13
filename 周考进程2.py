from multiprocessing import Process




#读取
def read():
    f1 = open('a.txt', mode='r', encoding='utf8')
    res = f1.read()
    print(res)
    f1.close()

#写入

def write(x):
    f2 = open('a.txt', mode='a+', encoding='utf8')
    f2.write(x)
    f2.close()

# print(read())


if __name__ == '__main__':   #写
    r2 = Process(target=write,args=('Hello,word',))
    r2.start()

if __name__ == '__main__':#读
    r1 = Process(target=read)
    r1.start()



