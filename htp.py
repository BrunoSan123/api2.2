import sys,os
import string,cgi,time
from BaseHTTPServer import  BaseHTTPRequestHandler, HTTPServer

class http(BaseHTTPRequestHandler):

def do_GET(self):
    try:

        if self.path.endswitch(" .html"):
          f = open(DocumentRoot + self.path)
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write(f.read())
          f.close()
          return

         if self.path.endswitch(" .esp"):
          
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          self.wfile.write("Hey hoje é dia"+ str(time.localtime()[7]))
          self.wfile.write("Hey hoje é ano"+ str(time.localtime()[0]))
          return
          
          return
        
         except IOError:
       self.send_error(404, 'Não encontrado %s' % self.path)
      
       def do_POST(self):
       global rootnode
       try:
          ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

           if ctype == 'multipart/form-data':
               query=cgi.parse_multipart(self,rfile,pdict)
            self.send_response(301)


            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontennte", upfilecontent[0]

            self.wfile.write("<html>Post OK. <br /><br />");
            self.wfile.write(upfilecontent[0]);
            self.wfile.write("</html>")

        except:

            pass     
      
