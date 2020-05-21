from apinews1 import nombre_articles
from mots import mots_cles_a_chercher
from mots import selection

class OutOfRangeError(ValueError):
    pass
<<<<<<< HEAD
=======

>>>>>>> af5fca8ce9ac669b9a4c8ab9b1fe64928bf9413b


def give_score():

    fact=input("News :")
    
    L= fact.split()
    
    if len(L)<3:
        raise OutOfRangeError("You have to write at least 3 words")
    
    mots_cles=selection(fact)[:]
    mots_cles1=mots_cles[:] #liste intermédiaire
    print("Mots clés de la phrase :")
    print(mots_cles)
    mots_indic = [] #On veut ici récupérer les deux mots-clés ayant le moins d'apparitions dans les articles,

    j=0
    while j<3:  #On réalise deux fois l'opération afin d'avoir les trois mots
        indexe_indic = 0
        indic = nombre_articles(mots_cles1[0])
        
        for i in range (1, len(mots_cles1)):
            if ((nombre_articles(mots_cles1[i]) <indic) and (nombre_articles(mots_cles1[i])!=0)):
                indic = nombre_articles(mots_cles1[i])
                indexe_indic = i
        mots_indic.append(mots_cles1[indexe_indic])
        del mots_cles1[indexe_indic]  #On retire le mot-clé déjà récupéré de la liste des mots-clés
        j+=1
        
    print("Les trois mots ayant le moins d'apparitions :")
    print(mots_indic)

    nombre_indic = mots_cles_a_chercher(mots_indic) #Notre indicateur ici est le nombre d'articles comportant les deux mots avec le moins d'apparitions
    nombre_total = mots_cles_a_chercher(mots_cles) #On récupère le nombre d'articles qui contiennent tous nos mots clés
    print("Score :")
    return nombre_total*100/nombre_indic
