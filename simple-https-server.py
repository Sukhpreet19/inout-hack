# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443
# here we are importing three files BaseHTTPServer,SimpleHTTPServer,ssl form other program or system which is stored somewhere
import BaseHTTPServer, SimpleHTTPServer
import ssl
#here the three imported files are used to input and manipulate server data
httpd = BaseHTTPServer.HTTPServer(('localhost', 4785), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
