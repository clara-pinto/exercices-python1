# Vos imports ici..
import urllib.request
from html.parser import HTMLParser

class IMDBParser(HTMLParser):
    # Votre classe ici
    def __init__(self):
        super().__init__()
        self.movies = [] #accumule les titres des films
        self.in_title = False #attribut indique si parser à l'interieur de la balise HTML
        self.in_title_column = False

    def handle_starttag(self, tag, attrs):
        if tag == "td" and ('class', 'titleColumn') in attrs:
            self.in_title_column = True

        if tag == "a" and self.in_title_column :
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "a" :
            self.in_title = False

        if tag == "td" :
            self.in_title_column = False

    def handle_data(self, data):
        if self.in_title == True :
            if data.strip():
                self.movies.append(data.strip())


def scrap_imdb(html_data):
    """
    Extrait la liste de film contenue dans html_data.

    Args:
        html_data: source de la page html

    Returns:
        Liste de films
    """
    # Votre code ici...
    parser = IMDBParser()
    parser.feed(html_data)

    return l
    
        
def main():
    """
    >>> with open("IMDb.html", mode='r', encoding='utf8') as f: html_data = f.read()
    >>> movies =  scrap_imdb(html_data)
    >>> for m in movies[:5]: print(m)
    Les évadés
    Le parrain
    The Dark Knight: Le chevalier noir
    Le parrain, 2ème partie
    12 hommes en colère
    >>> for m in movies[-5:]: print(m)
    Aladdin
    La couleur des sentiments
    La Belle et la Bête
    Du rififi chez les hommes
    Danse avec les loups
    """
    # Votre code ici...
    firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
    url = 'http://www.imdb.com/chart/top?ref_=nv_ch_250_4'
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', firefox)
        r = urllib.request.urlopen(req)
        html_data = r.read().decode('utf-8')
    except IOError:
        print("Erreur lors du téléchargement de la page")
    
    movies =  scrap_imdb(html_data) # movies = ['Les Évadés', 'Le Parrain', ..., 'Aladdin']
    
    # print reversed list of movies
    for m in reversed(movies):
        print(m)

    return None

if __name__ == '__main__':
    main()