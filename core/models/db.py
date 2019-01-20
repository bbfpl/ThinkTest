# coding=utf-8
from tinydb import TinyDB
from tool import Tool
from globals import g_get,base_dir
# DB Class
class DB:
    def __init__(self,dirname='db',dbname=''):
        if not dbname.strip():
            project_name = g_get('main')
        else:
            project_name = dbname
        self.db_path = base_dir() + '/runtime/'+ dirname +'/' + project_name + '.json'

    def __db_init(self):
        return TinyDB(self.db_path)

    def inster(self,data):
        return self.__db_init().insert(data)

    def select(self):
       return self.__db_init().all()

    # def delete(self):
    #     self.__db_init().remove()

    def remove_db(self):
        Tool().remove_file(self.db_path)

if __name__ == '__main__':
    # DB()
    # DB('temp', 'complete').inster({
    #     'status': 1,
    #     'method_name': 2
    # })
    DB().remove_db()