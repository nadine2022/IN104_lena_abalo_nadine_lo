from apinews1 import nombre_articles

#On commence par définir les paliers
#Il y a de l'ordre de 2.000.000 d'articles sur newsapi
#On décide donc que 2.000.000 correspond au score de 100 et on calcule avec cet indicateur 

def give_score(nombre):
    N= 2.000.000
    score = nombre*100/N
    return (score)
