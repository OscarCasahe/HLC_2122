import requests

r = requests.get('https://www.filmaffinity.com/es/film615789.html')
#r = requests.get('https://www.filmaffinity.com/es/film612331.html')

t = r.text


def titulo_original(t):
    etiqueta_titulo = "<dt>Título original</dt>"
    pos_etiqueta_titulo = t.find(etiqueta_titulo)
    titulo = t[pos_etiqueta_titulo:]
    titulo = titulo[:titulo.find("</dd>")].splitlines()[2].lstrip().rstrip()
    return titulo


def anio_original(t):
    etiqueta_anio = "<dt>Año</dt>"
    pos_etiqueta_anio = t.find(etiqueta_anio)
    anio = t[pos_etiqueta_anio:]
    anio = anio[:anio.find("</dd>")].splitlines()[1]
    anio = anio[anio.find(">")+1:]
    return anio


def duracion(t):
    etiqueta_duracion = "<dt>Duración</dt>"
    pos_etiqueta_duracion = t.find(etiqueta_duracion)
    duracion = t[pos_etiqueta_duracion:]
    duracion = duracion[:duracion.find("</dd>")].splitlines()[1]
    duracion = duracion[duracion.find(">")+1:]
    return duracion


def pais(t):
    etiqueta_pais = "<dt>País</dt>"
    pos_etiqueta_pais = t.find(etiqueta_pais)
    pais = t[pos_etiqueta_pais:]
    pais = pais[:pais.find("</dd>")].splitlines()[1]
    pais = pais[pais.find(";")+1:]
    return pais


def direccion(t):
    etiqueta_direccion = "<dt>Dirección</dt>"
    pos_etiqueta_direccion = t.find(etiqueta_direccion)
    direccion = t[pos_etiqueta_direccion:]
    direccion = direccion[:direccion.find("</dd>")]
    etiqueta_directores = '<span itemprop="name">'
    etiqueta_cierre = "</span>"
    directors = ""
    while(direccion.find(etiqueta_directores) != -1):
        direccion = direccion[direccion.find(
            etiqueta_directores)+len(etiqueta_directores):]
        directors += direccion[:direccion.find(etiqueta_cierre)] + ", "

    return directors.rstrip().rstrip(',')


def guions(t):
    etiqueta_guion = "<dt>Guion</dt>"
    pos_etiqueta_guion = t.find(etiqueta_guion)
    guion = t[pos_etiqueta_guion:]
    guion = guion[:guion.find("</dd>")]
    etiqueta_guionistas = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    guiones = ""
    while(guion.find(etiqueta_guionistas) != -1):
        guion = guion[guion.find(etiqueta_guionistas) +
                      len(etiqueta_guionistas):]
        guiones += guion[:guion.find(etiqueta_cierre)] + ", "

    return guiones.rstrip().rstrip(',')


def music(t):
    etiqueta_musica = "<dt>Música</dt>"
    pos_etiqueta_musica = t.find(etiqueta_musica)
    musica = t[pos_etiqueta_musica:]
    musica = musica[:musica.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    bso = ""
    while(musica.find(etiqueta_inicio) != -1):
        musica = musica[musica.find(etiqueta_inicio)+len(etiqueta_inicio):]
        bso += musica[:musica.find(etiqueta_cierre)] + ", "

    return bso.rstrip().rstrip(',')


def dir_fotografia(t):
    etiqueta_fotografia = "<dt>Fotografía</dt>"
    pos_etiqueta_fotografia = t.find(etiqueta_fotografia)
    fotografia = t[pos_etiqueta_fotografia:]
    fotografia = fotografia[:fotografia.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    photo = ""
    while(fotografia.find(etiqueta_inicio) != -1):
        fotografia = fotografia[fotografia.find(
            etiqueta_inicio)+len(etiqueta_inicio):]
        photo += fotografia[:fotografia.find(etiqueta_cierre)] + ", "

    return photo.rstrip().rstrip(',')


def cast(t):
    etiqueta_reparto = "<dt>Reparto</dt>"
    pos_etiqueta_reparto = t.find(etiqueta_reparto)
    reparto = t[pos_etiqueta_reparto:]
    reparto = reparto[:reparto.find("</dd>")]
    etiqueta_inicio = '<span itemprop="name">'
    etiqueta_cierre = "</span>"
    all_cast = ""
    while(reparto.find(etiqueta_inicio) != -1):
        reparto = reparto[reparto.find(etiqueta_inicio)+len(etiqueta_inicio):]
        all_cast += reparto[:reparto.find(etiqueta_cierre)] + ", "

    return all_cast.rstrip().rstrip(',')


def produccion(t):
    etiqueta_produccion = "<dt>Productora</dt>"
    pos_etiqueta_produccion = t.find(etiqueta_produccion)
    productora = t[pos_etiqueta_produccion:]
    productora = productora[: productora.find("</dd>")]
    etiqueta_inicio = '<span class="nb"><span>'
    etiqueta_cierre = "</span>"
    productoras = ""
    while(productora.find(etiqueta_inicio) != -1):
        productora = productora[productora.find(
            etiqueta_inicio)+len(etiqueta_inicio):]
        productoras += productora[:productora.find(etiqueta_cierre)] + ", "

    return productoras.rstrip().rstrip(',')


def tipo(t):
    etiqueta_genero = "<dt>Género</dt>"
    pos_etiqueta_genero = t.find(etiqueta_genero)
    genero = t[pos_etiqueta_genero:]
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


def argumento(t):
    etiqueta_sipnosis = '<dt>Sinopsis</dt>'
    pos_etiqueta_sipnosis = t.find(etiqueta_sipnosis)
    sipnosis = t[pos_etiqueta_sipnosis:]
    sipnosis = sipnosis[:sipnosis.find("</dd>")]
    sipnosis = sipnosis[sipnosis.find(
        '<dd class="" itemprop="description">') + len('<dd class="" itemprop="description">'):]

    return sipnosis


diccionario = {"Título original: ": titulo_original(t),
               "Año ": anio_original(t),
               "Duración ": duracion(t),
               "País ": pais(t),
               "Dirección ": direccion(t),
               "Guión ": guions(t),
               "Música ": music(t),
               "Fotografía ": dir_fotografia(t),
               "Reparto ": cast(t),
               "Productora ": produccion(t),
               "Género ": tipo(t),
               "Sipnosis ": argumento(t)}

print(diccionario)
