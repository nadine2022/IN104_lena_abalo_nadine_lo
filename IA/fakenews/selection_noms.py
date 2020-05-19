import spacy
nlp = spacy.load("en_core_web_sm")


def selection_noms(): #Fonction qui sélectionne les mots importants
    txt=input('News : ')
    doc = nlp(txt)
    mots=[token.text for token in doc]

    from spacy.lang.en.stop_words import STOP_WORDS
 
    mots_filtres =''

    for x in mots:
        lex = nlp.vocab[x]
        if lex.is_stop == False:  #On ne considère que les mots qui ne sont pas des stopswords(adjectfs, adverbes, pronoms...)                 
            mots_filtres+=x+' ' 
 
    print(mots_filtres)   

selection_noms()
