import requests

r = requests.get('https://www.filmaffinity.com/es/film615789.html')
# r = requests.get('https://www.filmaffinity.com/es/film612331.html')

html = r.text


class filmaffinity:

    url = ""
    html = ""

    def __init__(self, url):
        self.url = url

    def set_url(self, url):
        self.url = url

    def do_request(self):
        temp = requests.get(self.url)
        self.html = temp.text

    def procesar(self):
        self.resultado = {
            "Título original": self.titulo_original(),
            "Año": self.anio_original(),
            "Duración": self.duracion(),
            "País": self.pais(),
            "Dirección": self.direccion(),
            "Guión": self.guion(),
            "Música": self.musica(),
            "Fotografía": self.dir_fotografia(),
            "Reparto": self.cast(),
            "Productora": self.produccion(),
            "Género": self.tipo(),
            "Sinopsis": self.argumento()}

    def get_result(self):
        return self.resultado


def titulo_original(self):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = self.html.find(etiqueta_titulo)
    titulo = self.html[pos_etiqueta_titulo:]
    titulo = titulo[:titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    return titulo


def anio_original(self):
    etiqueta_anio = "<dt>Año</dt>"
    pos_etiqueta_anio = self.html.find(etiqueta_anio)
    anio = self.html[pos_etiqueta_anio:]
    anio = anio[:anio.find("</dd>")].splitlines()[1]
    anio = anio[anio.find(">")+1:]
    return anio


def duracion(self):
    etiqueta_duracion = "<dt>Duración</dt>"
    pos_etiqueta_duracion = self.html.find(etiqueta_duracion)
    duracion = self.html[pos_etiqueta_duracion:]
    duracion = duracion[:duracion.find("</dd>")].splitlines()[1]
    duracion = duracion[duracion.find(">")+1:]
    return duracion


def pais(self):
    etiqueta_pais = "<dt>País</dt>"
    pos_etiqueta_pais = self.html.find(etiqueta_pais)
    pais = self.html[pos_etiqueta_pais:]
    pais = pais[:pais.find("</dd>")].splitlines()[1]
    pais = pais[pais.find(";")+1:]
    return pais


def direccion(self):
    etiqueta_direccion = "<dt>Dirección</dt>"
    pos_etiqueta_direccion = self.html.find(etiqueta_direccion)
    direccion = self.html[pos_etiqueta_direccion:]
    direccion = direccion[:direccion.find("</dd>")]
    etiqueta_directores = '<span itemprop="name">'
    etiqueta_cierre = "</span>"
    directors = ""
    while(direccion.find(etiqueta_directores) != -1):
        direccion = direccion[direccion.find(
            etiqueta_directores)+len(etiqueta_directores):]
        directors += direccion[:direccion.find(etiqueta_cierre)] + ", "

    return directors.rstrip().rstrip(',')


def guion(self):
    etiqueta_guion = "<dt>Guion</dt>"
    pos_etiqueta_guion = self.html.find(etiqueta_guion)
    guion = self.html[pos_etiqueta_guion:]
    guion = guion[:guion.find("</dd>")]
    etiqueta_guionistas = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    guiones = ""
    while(guion.find(etiqueta_guionistas) != -1):
        guion = guion[guion.find(etiqueta_guionistas) +
                      len(etiqueta_guionistas):]
        guiones += guion[:guion.find(etiqueta_cierre)] + ", "

    return guiones.rstrip().rstrip(',')


def musica(self):
    etiqueta_musica = "<dt>Música</dt>"
    pos_etiqueta_musica = self.html.find(etiqueta_musica)
    musica = self.html[pos_etiqueta_musica:]
    musica = musica[:musica.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    bso = ""
    while(musica.find(etiqueta_inicio) != -1):
        musica = musica[musica.find(etiqueta_inicio)+len(etiqueta_inicio):]
        bso += musica[:musica.find(etiqueta_cierre)] + ", "

    return bso.rstrip().rstrip(',')


def dir_fotografia(self):
    etiqueta_fotografia = "<dt>Fotografía</dt>"
    pos_etiqueta_fotografia = self.html.find(etiqueta_fotografia)
    fotografia = self.html[pos_etiqueta_fotografia:]
    fotografia = fotografia[:fotografia.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    photo = ""
    while(fotografia.find(etiqueta_inicio) != -1):
        fotografia = fotografia[fotografia.find(
            etiqueta_inicio)+len(etiqueta_inicio):]
        photo += fotografia[:fotografia.find(etiqueta_cierre)] + ", "

    return photo.rstrip().rstrip(',')


def cast(self):
    etiqueta_reparto = "<dt>Reparto</dt>"
    pos_etiqueta_reparto = self.html.find(etiqueta_reparto)
    reparto = self.html[pos_etiqueta_reparto:]
    reparto = reparto[:reparto.find("</dd>")]
    etiqueta_inicio = '<span itemprop="name">'
    etiqueta_cierre = "</span>"
    all_cast = ""
    while(reparto.find(etiqueta_inicio) != -1):
        reparto = reparto[reparto.find(etiqueta_inicio)+len(etiqueta_inicio):]
        all_cast += reparto[:reparto.find(etiqueta_cierre)] + ", "

    return all_cast.rstrip().rstrip(',')


def produccion(self):
    etiqueta_produccion = "<dt>Productora</dt>"
    pos_etiqueta_produccion = self.html.find(etiqueta_produccion)
    productora = self.html[pos_etiqueta_produccion:]
    productora = productora[: productora.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    productoras = ""
    while(productora.find(etiqueta_inicio) != -1):
        productora = productora[productora.find(
            etiqueta_inicio)+len(etiqueta_inicio):]
        productoras += productora[:productora.find(etiqueta_cierre)] + ", "

    return productoras.rstrip().rstrip(',')


def tipo(self):
    etiqueta_genero = "<dt>Género</dt>"
    pos_etiqueta_genero = self.html.find(etiqueta_genero)
    genero = self.html[pos_etiqueta_genero:]
    genero = genero[:genero.find("</dd>")]
    etiqueta_inicio = '<a href='
    etiqueta_cierre = "</a>"
    barra = "|"
    generos = ""
    while(genero.find(etiqueta_inicio) != -1):
        genero = genero[genero.find(etiqueta_inicio)+len(etiqueta_inicio):]
        genero = genero[genero.find(">")+len(">"):]
        generos += genero[:genero.find(etiqueta_cierre)] + ". "

    return generos


def argumento(self):
    etiqueta_sipnosis = '<dt>Sinopsis</dt>'
    pos_etiqueta_sipnosis = self.html.find(etiqueta_sipnosis)
    sipnosis = self.html[pos_etiqueta_sipnosis:]
    sipnosis = sipnosis[:sipnosis.find("</dd>")]
    sipnosis = sipnosis[sipnosis.find(
        '<dd class="" itemprop="description">') + len('<dd class="" itemprop="description">'):]

    return sipnosis
