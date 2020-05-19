from newsapi import NewsApiClient
from panel.models import Article

newsapi=NewsApiClient(api_key='cc48bcc39628400db2715d790b287b32')

#liste de tous les articles qui contiennent le mot clé (q)
def nombre_articles(mots_cles):

    data = newsapi.get_everything(q=mots_cles,sources='abc-news,bbc-news,bbc-sport,bleacher-report,business-insider,business-insider-uk,cbs-news,cnbc,cnn,engadget,espn,independent,mashable,national-geographic,nbc-news,new-scientist,newsweek,new-york-magazine,reuters,the-verge,the-wall-street-journal,the-washington-post,the washington-times,time,usa-today', language='en')
    return(len(data['articles']))
    


def base_articles(mots_cles):
    data = newsapi.get_everything(q=mots_cles,sources='abc-news,bbc-news,bbc-sport,bleacher-report,business-insider,business-insider-uk,cbs-news,cnbc,cnn,engadget,espn,independent,mashable,national-geographic,nbc-news,new-scientist,newsweek,new-york-magazine,reuters,the-verge,the-wall-street-journal,the-washington-post,the washington-times,time,usa-today', language='en')

    #construction de la base de donnée
    n=len(data)

    #for i in range(0,n):
        
       #Article(source=data['articles'][i]['source']['name'],
                #title=data['articles'][i]['title'],
                #pub_date=data['articles'][i]['publishedAt']) #.save()

    return data  #la base de données

