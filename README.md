# techniqal-docker  - Szkolenie online Docker

## Komendy Unix - ściągawka
### System plików
`ls` wylistuj pliki

`cd` przejdź do folderu

`cd -` przejdź do poprzedniego folderu

`mkdir` stwórz folder

`rm nazwa_pliku` usuń plik `nazwa_pliku`

`rm -rf nazwa_folderu` usuń folder `nazwa_folderu` z zawartością

### Edycja
`touch nazwa_pliku` stwórz pusty plik o nazwie `nazwa_pliku`

`cat nazwa_pliku` wyświetl zawartość pliku `nazwa_pliku`

`nano nazwa_pliku` edytuj zawartość pliku `nazwa_pliku` z użyciem edytora `nano`

### Instalacja paczek
`apt update` aktualizuj biblioteki paczek

`apt install nano` zainstaluj edytor `nano`

### Tryby
`chown username file_path` zmiana właściciela pliku pod ścieżką `file_path` na `username`

`chmod +x script.sh` zmiana trybu na wykonawczy dla skryptu `script.sh`

### Zmienne środowiskowe
`export MOJA_ZMIENNA=123` ustawienie zmiennej środowiskowej `MOJA_ZMIENNA` na wartość `123` (zniknie po zamknięciu sesji)

`echo $MOJA_ZMIENNA` wydrukowanie zawartości zmiennej środowiskowej `MOJA_ZMIENNA`

***

## Docker - ogólnie
**Dockerfile** - plik tekstowy opisujący jak stworzyć obraz krok po kroku

**Obraz** - plik binarny reprezentujący "wzorzec" zbudowany na podstawie pliku Dockerfile

**Kontener** - uruchomiony obraz

Jak nasz obraz ma wyglądać opisujemy w _Dockerfile_. Następnie budujemy (`docker build`) obraz z podaniem wybranego taga. Obraz zbudowany znajdzie się na naszej maszynie (listujemy `docker images`). Możemy na jego podstawie uruchomić dowolną ilość _kontenerów_ (podglądamy `docker ps`).

Nazwa obrazu `python:3.6.10-alpine`  to tak zwany **tag**. Zawiera on nazwę "aplikcji" (`python`) i jej wersję (`3.6.10-alpine`) oddzielone dwukropkiem. To standardowa konwencja.


## Komendy Dockera - notatki
### Ściąganie obrazów z Dockerhub
**`docker pull ubuntu:18.04`** - ściagnij obraz Ubuntu 18.04 

### Obrazy
**`docker build -t tag_name dokerfile/path`** - zbuduj obraz z tagiem `tag_name` z użyciem pliku Dockerfile pod ścieżką `dockerfile/path`. Jeśli Dockerfile jest w bieżącym katalogu, `dockerfile/path` to po prostu kropka `.`

**`docker images`** - wylistuj wszytskie obrazy na maszynie

**`docker rmi ubuntu:18.04`** - usuń obraz `ubuntu:18.04` z maszyny

**`docker rmi ubuntu:18.04 --force`** - wymuś usunięcie obrazu `ubuntu:18.04` z maszyny

### Kontenery
##### Uruchamianie kontenra
**`docker run ubuntu:18.04`** - uruchom kontener z obrazu Dockera `ubuntu:18.04`

**`docker run -d serverimage`** - uruchom kontener z obrazu Dockera `serverimage` jako demon (w tle)

**`docker run -p3000:3001 ubuntu:18.04`** - uruchom kontener z obrazu Dockera  `ubuntu:18.04` z przekierowanym portem 3001 na port 3000 lokalnej maszyny

**`docker run -v /my/local/path:/container/path ubuntu:18.04`** - uruchom kontener z obrazu Dockera  `ubuntu:18.04` z podmontowaniem lokalnego folderu `/my/local/path` do kontenera w `/container/path`

**`docker run -it ubuntu:18.04 bash`** - uruchom kontener z obrazu Dockera  `ubuntu:18.04` w trybie interaktywnym z uruchomieniem basha (nadpisanie domyślnej komendy)

##### Listowanie kontenerów
**`docker ps`** - Wylistuj wszystkie żyjące kontenery

**`docker ps -a`** - Wylistuj wszystkie kontenery (martwe też)

##### Zabijanie i usuwanie konetenerów
**`docker stop containerID`** - zatrzymaj pracujący kontener o id `containerID`

**`docker rm containerID`** - usuń martwy kontener o id `containerID`

**`docker rm $(docker ps -q -f status=exited)`** usuń wszystkie martwe kontenery


### Dockerfile - słowa kluczowe
**`FROM`** z jakiego obrazu będziemy budować, np `FROM ubuntu:18.04`

**`RUN`** uruchom polecenie unix, np. `RUN echo $PATH`

**`WORKDIR`** ustawia kontenst kolejnych poleceń na folder z podanej ścieżki, np `WORKDIR /api` (tworzy go jeśli nie istnieje)

**`COPY`** skopiuj plik/folder z hosta do obrazu, np. `COPY script.sh /data/script.sh` albo `COPY ["<src>", ... "<dest>"]`

**`MAINTAINER`** kto jest autorem obrazu, np. `MAINTAINER adrian.gonciarz@gmail.com`
* [`MAINTAINER` (deprecated)]() => `LABEL maintainer="adrian.gonciarz@gmail.com"`

**`CMD`** domyślna komenda odpalana przy starcie kontenera z obazu, np. `CMD ls` albo `CMD ["ls", "la"]`

**`EXPOSE`** porty jakie wystawia kontener, np `EXPOSE 3000`

**`ENV`** ustawia zmienną środowisko, np `ENV host 127.0.0.1` 

**`VOLUME`** podmontowuje zasoby dyskowe z hosta do kontenera automatycznie `VOLUME /my/path /external/path`

### Docker Compose
#### Słowa kluczowe
**`image`** Nazwa budowanego obrazu

**`build`** Info o budowaniu obrazu: jaki Dockerfile i kontext (folder w którym budujemy)

**`ports`** Lista wystawionych portów

**`environment`** Lista zmiennych środowiskowych

**`volumes`** List podmontowanych zasobów dyskowych

**`depends_on`** Czekanie na start innegoserwisu (lista nazw serwisów na które ma czekać)

#### Komendy
**`docker-compose build service`** - zbuduj serwis za pomocą informacji z `docker-compose.yml`

**`docker-compose up`** - uruchom kompozycję zgdnie z plikiem `docker-compose.yml` (domyślna nazwa pliku, którego DC szuka w bieżacym folderze)

**`docker-compose up service`** - uruchom kompozycję `service` zgodnie z `docker-compose.yml`

**`docker-compose up -d`** - uruchom kompozycję w trybie demona (w tle)

**`docker-compose down`** - zatrzymaj i wyczyść artefakty kompozycji z pliku  `docker-compose.yml`

**`docker-compose run image`** - uruchom obraz w kontekście docker-compose (podobnie jak `docker run`)

### Czyszczenie
**`docker rmi $(docker images --quiet --filter "dangling=true")`** usuń wiszące obrazy z maszyny (raczej nie używane, bo jest poniższa komenda)

**`docker system prune`** - wyczyść wszystkie "śmieci" (wiszące kontenery, sieci, procesy, etc.)

**`docker container prune`** - wyczyść martwe kontenery
