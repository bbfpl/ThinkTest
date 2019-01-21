from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse
from base import base_dir
from config import Config
from tool import Tool
# 创建web静态服务器
class HttpServer(BaseHTTPRequestHandler):
    # MIME-TYPE
    mimedic = [
        ('.html', 'text/html'),
        ('.htm', 'text/html'),
        ('.js', 'application/javascript'),
        ('.css', 'text/css'),
        ('.json', 'application/json'),
        ('.png', 'image/png'),
        ('.jpg', 'image/jpeg')
    ]
    # GET
    def do_GET(self):
        sendReply = False
        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query

        if filepath.endswith('/'):
            filepath += 'index.html'
        filename, fileext = path.splitext(filepath)
        for e in self.mimedic:
            if e[0] == fileext:
                mimetype = e[1]
                sendReply = True

        if sendReply == True:
            try:
                with open(path.realpath(base_dir() + '/runtime/html' + filepath), 'rb') as f:
                    content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(content)
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)

def server_run():
    html_dir = base_dir() + '/runtime/html/'
    # 是否启用server
    open_http_server = Config.get_config('openHttpServer')
    # http server 端口
    server_port = Config.get_config('serverPort')
    # 判断配置文件是否启动http server
    if open_http_server == 'True':
        # 如果端口启动成功 说明http已经运行成功
        if Tool().net_is_used(int(server_port)) is False:
            print('启动Http服务，端口', server_port)
            # Server 设置
            httpd = HTTPServer(('', int(server_port)), HttpServer)
            print('Http服务运行中...')
            httpd.serve_forever()


if __name__ == '__main__':
    server_run()
    # net_is_used = Tool().net_is_used(5000)
    # print(net_is_used)