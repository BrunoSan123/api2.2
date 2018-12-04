import BaseHTTPServer
import time


host_name = 'localhost'
port_number = 8080

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Meu Server</title></head><body><h1>O server funcionou</h1></body></html>")
if  __name__ == '__main__':
     server_class = BaseHTTPServer.HTTPServer
     httpd = server_class((host_name, port_number), MyHandler)
     print time.asctime(), "server starts - %s:%s" %(host_name, port_number)
    
     try:
         httpd.serve_forever()
     except KeyboardInterrupt:
         pass   
        
     httpd.server_close()
     print time.asctime(), "Server Stop - %s: %s" (host_name, port_number)
