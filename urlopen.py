import urllib.request



def urlopen(url):
    pagina = urllib.request.urlopen(url)    
    texto  = pagina.read().decode("utf8")
    inicio = texto.find(">$") + 2
    fim = inicio +4
    return texto[inicio:fim]