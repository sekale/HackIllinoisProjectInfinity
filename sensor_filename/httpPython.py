import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("172.17.15.199", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
