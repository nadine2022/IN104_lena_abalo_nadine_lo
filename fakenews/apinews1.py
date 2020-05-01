from newsapi import NewsApiClient
from panel.models import Article

newsapi=NewsApiClient(api_key='cc48bcc39628400db2715d790b287b32')

#liste de tous les articles qui contiennent le mot clé (q)
data = newsapi.get_everything(q='jupyter lab', language='en')

#construction de la base de donnée
n=len(data)

for i in range(0,n):
    Article(source=data['articles'][i]['source']['name'],
            title=data['articles'][i]['title'],
            pub_date=data['articles'][i]['publishedAt']).save()

print(Article.objects.all())

