import pymysql.cursors

connection = pymysql.connect(
  host="127.0.0.1",
  user='root',
  password='root',
  db='middleware',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor) 
  
print ("connect successful!!")
