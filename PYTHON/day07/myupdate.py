import pymysql
db = pymysql.connect(host='localhost', port=3306,user='root',passwd='java', db='python_k', charset='utf8')
cursor = db.cursor()

sql = "UPDATE mytable SET col02 = %s, col03 = %s WHERE col01 = %s"

cursor.execute(sql, ("2", "2", 1))


db.commit()
db.close()
