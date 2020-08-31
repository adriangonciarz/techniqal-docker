### Zadanie 1
1. Stwórz nowy folder `src`
2. Stwórz w nim katalog `api`, kopiując do niego `Dockerfile` do serwera api `json-server`. Zmień nazwę pliku na `Dockerfile-api`
3. Skopiuj do `src/api` plik `db.json`
```json
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}
``` 
4. W `src` utwórz `docker-compose.yml` zawierający informację o obrazie (kontekst, dockerfile)
```yml
version: '3.0'
services:
  api:
    image: twojanazwa:twojtag
    build: 
        context: api/
        dockerfile: Dockerfile-api
```
5. Zbuduj obraz z użyciem `docker-compose`

### Zadanie 2 
1. Do pliku `docker-compose` z poprzedniego zadania:
	- Dodaj wystawienie portów
2. Uruchom obraz z uzyciem `docker-compose up`
3. Zatrzymaj obraz z uzyciem `docker-compose down`

### Zadanie 3
1. Dodaj nowy plik `big_db.json`
```json
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "alysson3" },
    { "id": 2, "title": "json-server2", "author": "john" },
    { "id": 3, "title": "json-server3", "author": "mike" },
    { "id": 4, "title": "json-server4", "author": "marry" },
    { "id": 5, "title": "json-server5", "author": "kate" },
    { "id": 6, "title": "json-server6", "author": "typicode3" },
    { "id": 7, "title": "json-server7", "author": "typicode" },
    { "id": 8, "title": "json-server7", "author": "typicode" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "typicode" }
}
```
2. W pliku Dockerfile ustaw zmienną środowiskową `PORT=3131` i skorzystaj z niej przy wystawianiu api (dodaj do komendy `--port $PORT`)
3. Do pliku `docker-compose` z poprzedniego zadania:
	- Dodaj podmontowanie volume z nowym `big_db.json` pomieniającym istniejącą bazę
4. Uruchom serwer i sprawdź, że słucha na `http://localhost:3131`
5. Do pliku `docker-compose` z poprzedniego zadania:
	- Dodaj ustawianie zmiennej środowiskowej `PORT` na wartość 3333
6. Uruchom serwer i sprawdź, że słucha na `http://localhost:3333`
7. Zatrzymaj serwer `docker-compose down`

### Zadanie 4
1. W `src` utwórz katalog `test`.
2. Utwórz w nim pliki `requirements.txt`:
```
pytest
requests
```
oraz `test_api.py`
```python
import requests
import random

base_uri = 'http://localhost'
port = 3000
posts_uri = f'{base_uri}:{port}/posts'


def test_api_get_posts():
	r = requests.get(posts_uri)
	assert r.status_code == 200

def test_creating_post():
	marker = random.randint(1, 100000)
	body = {'title': 'test post', 'author': 'ag'}
	r = requests.post(posts_uri, json=body)
	assert r.status_code == 201
```

3. Stwórz nowy plik `Dockerfile-test`:
* Bazując na obrazie Python
* ustaw workdir na folder `/test-src`
* skopiuj `requirements.txt` oraz `test_api.py` do folderu `/test-src`
* Uruchom `pip install -r requirements.txt`
4. Zbuduj obraz
5. Odpal obraz w trybie interaktywnym
6. Uruchom polecenie `pytest`

### Zadanie 5
1. W pliku `test_api.py` z poprzedniego zadania zmodyfikuj linijki na 

```python
import requests
import random
import os

base_uri = os.getenv('API_HOST', 'http://localhost')
port = os.getenv('API_PORT', 3000)
```
2. W docker-compose dodaj nowy serwis `api-test`
3. Dodaj w nim informacje o buildzie i zmienne
```
API_PORT=3333
API_HOST=http://api
```
4. Uruchom build za pomocą `docker-compose`
5. Odpal obraz za pomocą `docker-compose run --rm --use-aliases test`
6. Uruchom test

