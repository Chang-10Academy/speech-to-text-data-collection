from http.server import HTTPServer, BaseHTTPRequestHandler
import random, os

class textgen(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('context-type', 'text/json')
        self.end_headers()
        files = os.listdir('../data/texts/')
        textfile = files[random.randint(0,len(files)-1)]
        try:
            text_coll = open(f"../data/texts/{textfile}", 'r', encoding="utf-8")
        except FileNotFoundError:
            logging.error('txt file not found')

        texts = list(map(lambda x: x.strip(), text_coll.readlines()))
        data = texts[random.randint(0, len(texts)-1)]

        self.wfile.write(data.encode('utf-8'))

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), textgen)
    print('Server running on port {}'.format(PORT))
    server.serve_forever()

if __name__ == '__main__':
    main()
