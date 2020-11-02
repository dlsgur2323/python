import pymysql
db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
cursor = db.cursor()

sql = "INSERT INTO mytable (col02,col03) VALUES (%s, %s)"

cursor.execute(sql, ("2", "2"))


db.commit()
db.close()
