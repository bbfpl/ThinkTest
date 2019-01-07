# coding=utf-8
from tinydb import TinyDB
from config import Config

# DB Class
class DB:
    def __init__(self,dirname='db',dbname=''):
        if not dbname.strip():
            project_name = Config.get_config('main')
        else:
            project_name = dbname

        self.db = TinyDB(Config.base_dir+'/runtime/'+ dirname +'/' + project_name + '.json')

    def inster(self,data):
        return self.db.insert(data)

    def select(self):
       return self.db.all()

    def delete(self):
        self.db.remove()

if __name__ == '__main__':
    # DB()
    DB('temp', 'complete').inster({
        'status': 1,
        'method_name': 2
    })