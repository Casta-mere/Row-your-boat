import pymysql
    
# columns="mid varchar(255),name varchar(255),sex VARCHAR(255),fans int,friend int,level int,vip int"
colunms="id int,start_time int,end_time int"
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

class mysql():
    def __init__(self,name):
        self.database_name=name

    def Create_Database(self):
        conn=pymysql.connect(host='localhost',user='root',password='',charset='utf8')
        cursor=conn.cursor()
        sql=f"DROP database IF EXISTS `{self.database_name}`;"
        cursor.execute(sql)
        sql=f"create database `{self.database_name}`;"
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def Drop_Database(self):
        conn=pymysql.connect(host='localhost',user='root',password='',charset='utf8')
        cursor=conn.cursor()
        sql=f"DROP database IF EXISTS `{self.database_name}`;"
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def Drop_table(self,table_name):
        conn=pymysql.connect(host='localhost',user='root',password='',db=self.database_name,charset='utf8')
        cursor=conn.cursor()
        sql=f"DROP table IF EXISTS `{table_name}`;"
        cursor.execute(sql)
        cursor.close()

    def Create_table(self,table_name,columns):
        self.Drop_table(table_name)
        conn=pymysql.connect(host='localhost',user='root',password='',db=self.database_name,charset='utf8')
        cursor=conn.cursor()
        sql=f"create Table `{table_name}`({columns})"
        cursor.execute(sql)
        cursor.close()

    def update_table(self,table_name,item):
        conn=pymysql.connect(host='localhost',user='root',password='',db='bilibili_up',charset='utf8')
        cursor=conn.cursor()
        values=""
        for i in item:
            values+=f'"{i}",'
        sql=f'insert into `{table_name}` values({values});'
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        cursor.close()
        conn.close()