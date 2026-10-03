from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

class InvitacionHandler(SimpleHTTPRequestHandler):
    pass

if __name__ == "__main__":
    servidor = ThreadingHTTPServer(("0.0.0.0", 8000), InvitacionHandler)
    print("Invitación disponible en: http://127.0.0.1:8000")
    servidor.serve_forever()
