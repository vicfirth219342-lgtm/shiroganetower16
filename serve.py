import http.server, os
os.chdir("/Users/kiyo/Desktop/LP_photo")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=3000, bind="127.0.0.1")
