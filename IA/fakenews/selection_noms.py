import spacy
nlp = spacy.load("en_core_web_sm")


def selection_noms(txt): #Fonction qui sélectionne les mots importants
   
    doc = nlp(txt)
    mots=[token.text for token in doc]
    nat = [token.pos_ for token in doc]

    from spacy.lang.en.stop_words import STOP_WORDS
 
    mots_filtres =''
    n=len(mots)
    for i in range(0,n):
        lex = nlp.vocab[mots[i]]
        if lex.is_stop == False and (nat[i] != 'VERB') and (nat[i] != 'AUX'):  #On ne considère que les mots qui ne sont ni des stopswords(adverbes, pronoms...), ni des verbes                 
            mots_filtres+=mots[i]+' ' 
 
    return mots_filtres  


