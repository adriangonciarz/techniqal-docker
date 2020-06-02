### Zadanie 1
1. Wejdź na https://hub.docker.com/
1. Odszukaj obraz Python 3.8.3-slim-buster
1. Pobierz ten obraz na swoją maszynę
1. Wylistuj wszystkie obrazy na swojej maszynie i upewnij się, że został pobrany Python 3.8.3-slim-buster
1. Pobierz nowy obraz Python 3.8.3-buster
1. Wylistuj wszystkie obrazy na swojej maszynie i upewnij się, że masz oba obrazy z Python
1. Usuń obraz Python 3.8.3-slim-buster
1. Wylistuj wszystkie obrazy na swojej maszynie i upewnij się, że masz tylko obraz obrazy Python 3.8.3-buster

### Zadanie 2 
1. Uruchom shell bash w obrazie python:3.8.3-buster w trybie interaktywnym z wystawionym portem 8000 na kontenerze
1. Zaktualizuj paczki apt
1. Zainstaluj edytor nano
1. Utwórz plik `srv.py` i umieść w nim 
```
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

```
1. Wstaw prosty html w plik `index.html` w folderze ze skryptem
1. Uruchom skrypt
1. Wejdź na `http://localhost:3000` na swojej maszynie

### Zadanie 3 
1. Wykonaj to samo co w zadaniu 2, tyle że z użyciem podmontowanych zasobów dyskowych