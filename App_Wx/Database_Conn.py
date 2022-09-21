import pymysql

def Create_Database(name):
    conn=pymysql.connect(host='localhost',user='root',password='',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP database IF EXISTS `{name}`;"
    cursor.execute(sql)
    sql=f"create database `{name}`;"
    cursor.execute(sql)
    cursor.close()
    conn.close()

def Drop_Database(name):
    conn=pymysql.connect(host='localhost',user='root',password='',charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP database IF EXISTS `{name}`;"
    cursor.execute(sql)
    cursor.close()
    conn.close()
    
def drop_table(DataBasename,name):
    conn=pymysql.connect(host='localhost',user='root',password='',db=DataBasename,charset='utf8')
    cursor=conn.cursor()
    sql=f"DROP table IF EXISTS `{name}`;"
    cursor.execute(sql)
    cursor.close()

# columns="mid varchar(255),name varchar(255),sex VARCHAR(255),fans int,friend int,level int,vip int"
def Create_table(DataBasename,name,columns):
    drop_table(DataBasename,name)
    conn=pymysql.connect(host='localhost',user='root',password='',db=DataBasename,charset='utf8')
    cursor=conn.cursor()
    sql=f"create Table `{name}`({columns})"
    cursor.execute(sql)
    cursor.close()

def up_Sql(List,table):
    conn=pymysql.connect(host='localhost',user='root',password='',db='bilibili_up',charset='utf8')
    cursor=conn.cursor()
    sql=f'insert into `{table}` values({List[0]},"{List[1]}","{List[2]}","{List[3]}","{List[4]}","{List[5]}","{List[6]}");'
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()