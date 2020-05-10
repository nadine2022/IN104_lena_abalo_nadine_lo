from apinews1 import nombre_articles
from mots import mots_clés_à_chercher
from mots import selection

def give_score():
    
    mots_clés=selection()
    mots_indic = [] #On veut ici récupérer les deux mots-clés ayant le moins d'apparitions dans les articles, 
    i=0
    while i<2:     #On réalise deux fois l'opération afin d'avoir les deux mots
        indexe_indic = 0
        indic = nombre_articles(mots_clés[0]) 
        for i in range (1, len(mots_clés)):
        if ((nombre_articles(mots_clés[i]) <indic) and (nombre_articles(mots_clés[i])!=0)):
            indic = nombre_articles(mots_clés[i])
            indexe_indic = i
        mots_indic.append(mots_clés[index_indic])
        del mots_clés[indexe_indic]  #On retire le mot-clé déjà récupéré de la liste des mots-clés
        i+=1
    
    nombre_indic = mots_clés_à_chercher(mots_indic) #Notre indicateur ici est le nombre d'articles comportant les deux mots avec le moins d'apparitions
    nombre_total = mots_clés_à_chercher(mots_clés) #On récupère le nombre d'articles qui contiennent tous nos mots clés
    score = nombre_total*100/nombre_indic #On considère que l'indicateur correspond au score de 100, puis on fait une règle de 3 pour avoir le score de nos mots
    return score
