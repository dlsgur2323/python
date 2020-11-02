import pymysql
db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
cursor = db.cursor()

sql = "DELETE FROM mytable WHERE col01 = %s"

cursor.execute(sql, (3))


db.commit()
db.close()
