import spacy
from newsapi import NewsApiCLient
from apinews1 import nombre_articles
from selection_verbes import selection_verbes
from selection_noms import selection_noms
from selection2 import selection_2
nlp = spacy.load("en_core_web_sm")

  


def scores():
    txt=input('News : ')
    doc=nlp(txt)
    
    mots=[token.text for token in doc]
    if len(mots)<3:
        raise OutOfRangeError("You have to write at least 3 words")
    
    verbs=selection_verbes(txt)
    nouns=selection_noms(txt)
    proportion = selection_2(verbs,nouns) #On récupère la proportion obtenue sur la base de 20 articles
    tot = nombre_articles(nouns) #On prend le nombre total d'articles dans lesquels les mots apparaissent afin d'y appliquer la proportion
    nb_final = proportion*tot
    
    if nb_final >= 200:
        score = 100
    score = 0.5*nb_final #Par article obtenu, on accorde 0.5 points
  
    return score 
