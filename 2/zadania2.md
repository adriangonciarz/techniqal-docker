### Zadanie 1
Stwórz nowy plik Dockerfile:
* Bazując na obrazie ubuntu 18.04 
* ustaw `LABEL maintainer` na siebie
* w trakcie budowania obrazu wykonaj `RUN apt-get update && apt-get install procps -y`
* ustaw zmienną środowiskową `NAME` na swoje imię
* w trakcie startu kontenera wykonaj:
    * `ps aux`
    * `echo $NAME`

### Zadanie 2 
1. Stwórz plik `db.json` o zawartości
```
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
2. Stwórz nowy plik Dockerfile:
* Bazując na obrazie node JS
* ustaw workdir na folder `/api`
* skopiuj `db.json` do folderu `/api`
* zainstaluj w obrazie paczkę https://www.npmjs.com/package/json-server
* wystaw port 3000
* przy starcie kontenera uruchom Json server poleceniem `json-server --watch /api/db.json --host 0.0.0.0`
3. Uruchom obraz z podmontowanym portem do hosta portem 3000
4. Sprawdź że api działa na `http://localhost:3000/posts/1`
