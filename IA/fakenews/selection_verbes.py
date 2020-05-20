import spacy
nlp = spacy.load("en_core_web_sm")

def selection_verbes(txt): #fonction qui séléctionne les verbes de la phrase pour la 2e sélection
    
    doc = nlp(txt)
    
    verbs=''
    mots=[token.text for token in doc]
    nat = [token.pos_ for token in doc] #On récupère les natures de tous les mots
    
    n = len(nat)
    for i in range (0,n):
        if nat[i] =='VERB' or nat[i]=='AUX': #On prend uniquement les verbes et auxiliaires
            verbs+= mots[i]+' '
    
    doc1=nlp(verbs)  #On crée un doc avec les verbes afin de pouvoir les mettre à l'infinitif
    verb_list=[token.lemma_ for token in doc1]
    return verb_list  
