from apinews1 import nombre_articles
from mots import mots_clés_à_chercher
from mots import selection

def give_score():
    
    mots_clés=selection()
    indic = nombre_articles(mots_clés[0]) #On utilise comme indicateur le mot avec le moins d'apparitions dans les articles  
    for i in range (1, len(mots_clés)):
        if ((nombre_articles(mots_clés[i]) <indic) and (nombre_articles(mots_clés[i])!=0)):
            indic = nombre_articles(mots_clés[i])
      
    nombre_total = mots_clés_à_chercher(mots_clés) #On récupère le nombre d'articles qui contiennent tous nos mots clés
    score = nombre_total*100/indic #On considère que l'indicateur correspond au score de 100, puis on fait une règle de 3 pour avoir le score de nos mots
    return score
