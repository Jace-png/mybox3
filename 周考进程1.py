from multiprocessing import Process

#进程的第一种写法

# def Number():
#     for i in range(11):
#         print(i)
#
# if __name__ == '__main__':
#     p1 = Process(target=number)
#     p1.start()

#进程的第二种写法:
class Number(Process):
    def __init__(self,x,y):
        Process.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        for i in range(self.x,self.y):
            print(i)

if __name__ == '__main__':
    n1 = Number(10,50)
    n1.start()
