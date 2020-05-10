import string
from apinews1 import nombre_articles

def selection():

    fact=input('Rentrez une phrase : ') #On veut détecter les mots clés à changer avec les données de l'utilisateur
    L=fact.split()

    #Séparer les points de ponctuation des mots
    for i,x in enumerate(L):
       
        n=len(L[i])
        if L[i][n-1] in string.punctuation :
            L[i]=L[i][:n-1]

    T=L[:] #copie de L
            #on fait le tri, on enlève ponctuation, adjectifs, adverbes, mots courts

    for i,x in enumerate(L):

    #élimination des mots courts(sauf les sigles), ponctuation et chiffres
        if ((len(x)<3) and (x[len(x)-1] not in string.ascii_uppercase)):
            T.pop(T.index(x))
        
        n=len(x)

        #élimination d'une partie d'adjectifs, d'adverbes
    
        terminaison_2_lettres=["ed","al","er"]
        terminaison_3_lettres=["ive","ful","ble","ant","ing"]
        terminaison_4_lettres=["less"]

        if x[n-2:n] in terminaison_2_lettres :
            T.pop(T.index(x))
        if x[n-3:n] in terminaison_3_lettres :
            T.pop(T.index(x))
        if x[n-4:n] in terminaison_4_lettres :
            T.pop(T.index(x))


    # séléction des mots-clés en utilisant apinews1
    mots_clés=[]
    
    for x in T:
        if ((nombre_articles(x)<=500000) or (x=='not')): #on garde les négations
            mots_clés.append(x)

    return(mots_clés) # les mots les plus importants

def mots_clés_à_chercher(mots_clés):
    s=""

    for i in mots_clés:
        s=s+i+" "
    print(s)
    return (nombre_articles(s)) # donne le nombre d'articles final contenant ces mots-là !!
    
