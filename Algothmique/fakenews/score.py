from apinews1 import nombre_articles
from mots import mots_cles_a_chercher
from mots import selection


def give_score():
    fact=input('Rentrez une phrase : ') #On veut détecter les mots clés à changer avec les données de l'utilisateur

    mots_cles=selection(fact)
    indic = nombre_articles(mots_cles[0]) #On utilise comme indicateur le mot avec le moins d'apparitions dans les articles  
    for i in range (1, len(mots_cles)):
        if nombre_articles(mots_cles[i]) <indic:
            indic = nombre_articles(mots_cles[i])
    nombre_total = mots_cles_a_chercher(mots_cles) #On récupère le nombre d'articles qui contiennent tous nos mots clés
    score = nombre_total*100/indic #On considère que l'indicateur correspond au score de 100, puis on fait une règle de 3 pour avoir le score de nos mots
    return score
