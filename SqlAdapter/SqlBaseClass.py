import pymysql.cursors

class SqlBaseClass:
    def makeConnection(self):
        conn = pymysql.connect(
            host="z37udk8g6jiaqcbx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
            user="g9mkg655manzaloi",
            password="ori01i94r4u8u4ow",
            db="jfzv4qj56bw65xyy",
            port=3306,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    def executeSqlQuery(self, query, data):
        conn = self.makeConnection()
        cur = conn.cursor()
        cur.execute(query, data)
        result = cur.fetchall()
        cur.close()
        conn.close()

        return result

    def insertRecord(self, query, data):
        conn = self.makeConnection()
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
        cur.close()
        conn.close()