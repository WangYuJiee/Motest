from seldom.db_operation import MySQLDB


class ConnectDB(object):

    def __init__(self):
        # mysql
        # self.db = None
        self.db = MySQLDB(host="192.168.31.189",
                          port="3306",
                          user="root",
                          password="Auto12**",
                          database="serve-room-api")
        # sqlite3
        # self.db = SQLiteDB(r"D:\learnAPI\db.sqlite3")
        pass





