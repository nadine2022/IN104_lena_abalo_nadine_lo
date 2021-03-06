import spacy
from newsapi import NewsApiClient
from apinews1 import nombre_articles
from apinews1 import base_articles
from selection_verbes import selection_verbes
from selection_noms import selection_noms

newsapi=NewsApiClient(api_key='cc48bcc39628400db2715d790b287b32')
nlp=spacy.load("en_core_web_sm")
nlp1=spacy.load('en_vectors_web_lg')

def similitude(verbe,L):#un verbe et une liste
    n=len(L)
    for i in range(0,n):
        if (nlp1(verbe).similarity(nlp1(L[i]))>0.4):
            return True
    return False

def selection_2(verbs, nouns): # verbs =liste des verbes tokenisés de la phrase
    
    data1= newsapi.get_everything(q=nouns,sources='abc-news,bbc-news,bbc-sport,bleacher-report,business-insider,business-insider-uk,cbs-news,cnbc,cnn,engadget,espn,independent,mashable,national-geographic,nbc-news,new-scientist,newsweek,new-york-magazine,reuters,the-verge,the-wall-street-journal,the-washington-post,the washington-times,time,usa-today', language='en')
    
   
    m=len(verbs)
    p=0 #nombre d'articles qui passent la deuxième séléction
   

    for i in range(0,len(data1['articles'])):# en réalité, on ne peut avoir qu'accès à un nombre limité d'articles, car avec les contenus intégrals, la base de données est vite saturée, il est possible de lire que les premiers.
        
        #pour chaque article on veut relever les verbes à l'infinitif
        
        #texte de l'article       
        doc=nlp(data1['articles'][i]['content'])
        L=[] #liste où on va mettre les verbes
        
        for token in doc :
            if (token.pos==100):
                L.append(token.lemma_)
        
        f=1
        for j in range(0,m):
            
            if (similitude(verbs[j],L)==False):
                f=0
        if (f==1):
            p=p+1

    
    proportion=p/len(data1['articles'])  #on a fait une étude sur un échantillon, on en a déduit une probabilité qu'on applique ensuite au nombre total réel          
    return proportion


def testons():
    text=input("News:")
    noms=selection_noms(text)
    verbes=selection_verbes(text)
    p=selection_2(verbes,noms)
    return p
    
    

        
        
