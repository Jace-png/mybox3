from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

engine1 = create_engine('mysql+pymysql://root:jace111@localhost:3306/pythonclass')  # 创建连接

# 映射
Base = declarative_base()


# 类
class Students(Base):
    __tablename__ = 'student_table'
    id = Column(String(10), primary_key=True)
    name = Column(String(20))
    age = Column(String(10))


# 创建表
Base.metadata.create_all(engine1)
# 获取连接对象
DBsession = sessionmaker(bind=engine1)
dbsession = DBsession()

# 添加数据

s1 = Students(id='1', name='Jace', age='10')
s2 = Students(id='2', name='Make', age='20')
s3 = Students(id='3', name='Tom', age='30')
# dbsession.add(s1)
# dbsession.add_all([s2,s3])
# dbsession.commit()
# dbsession.close()


#修改数据

# res = dbsession.query(Students).filter(Students.id == '1').one()
# res.name = 'Alice'
# dbsession.commit()
# dbsession.close()

#删除数据

dbsession.query(Students).filter(Students.id == '3').delete()
dbsession.commit()
dbsession.close()