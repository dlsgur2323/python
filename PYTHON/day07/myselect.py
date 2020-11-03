import pymysql
db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
cursor = db.cursor()

sql = "select * from mytable"

cursor.execute(sql)
res = cursor.fetchall()

for data in res:
    print(data)

db.close()
