# IN104_lena_abalo_nadine_lo
TDs

TDD : apprentissage de la manipulation des classes et des tests

Le projet est divisé en 2 parties : ALGORITHMIQUE et IA

- ALGORITHMIQUE : Programmation du détecteur de Fake News avec Python et Django

  - Création d'un site internet pour le détecteur avec Django
  - Construction d'une base d'articles provenant d'une trentaine de sources considérées comme fiables
  - Algorithme qui repère les mots-clés dans une phrase, basé sur une élimination de certains adverbes et adj et sur les principes du TF-IDF
  - Test qui vérifie le fonctionnement de l'algorithme
  - Tests sur ce que rentre l'utilisateur (fait qu'il veut vérifier)
  - Mise en place du score en prenant le nombre d'articles contenant tous les mots-clés de la phrase rentrée par l'utilisateur
  
  
  
- IA : Utilisation du Natural Language Processing

  - Réutilisation de la base de donnée établie en partie Algorthmique
  - Algorithme pour sélectionner les noms et adjectifs de la phrase de l'utilisateur
  - Algorithme pour sélectionner les verbes de la phrase mis à l'infinitif grâce à la tokenisation
  - Sélection des articles en 2 phases : Construction d'une base d'articles contenant tous les noms et adj de la phrase,
  puis avec les verbes, comparaison des sens de phrase avec similitude
  - Elaboration du score à partir de paliers
