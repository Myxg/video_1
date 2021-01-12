import pymysql


db = pymysql.connect('localhost', 'root', '000000', 'video')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS video_user")

video_user = """CREATE TABLE video_user (
         id int(11) NOT NULL AUTO_INCREMENT,
         username CHAR(128),
         password  CHAR(128),
         PRIMARY KEY (`id`)
         )character set utf8"""

cursor.execute(video_user)

db.close()

