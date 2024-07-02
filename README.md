## 🔶 Arbre préfixe
Ah ! j'en perds mes mots...

👉 Le challenge de cette semaines porte sur un thème très important dans l'univers de l'algorithmie.
Il s'agit de créer une [*trie*](https://fr.wikipedia.org/wiki/Trie_(informatique)) ou *arbre préfixe* en français.
Cela doit rester simple mais complet, incluant sa représentation et au minimum les fonctions `add()` et `contains()`.


from wikipedia:
> En informatique, un ou une trie (prononcé [ˈtriː] ou [ˈtraɪ]) ou arbre préfixe,
> est une structure de données ayant la forme d'un arbre enraciné.
> Il est utilisé pour stocker une table associative où les clés sont généralement des chaînes de caractères.
> Contrairement à un arbre binaire de recherche, aucun nœud dans le trie ne stocke la chaîne à laquelle il est associé.
> C'est la position du nœud dans l'arbre qui détermine la chaîne correspondante.
> Pour tout nœud, ses descendants ont en commun le même préfixe.
> La racine est associée à la chaîne vide.
> Des valeurs ne sont pas attribuées à chaque nœud,
> mais uniquement aux feuilles et à certains nœuds internes
> se trouvant à une position qui désigne l'intégralité d'une chaîne correspondant à une clé.


🔹 **Étapes**
1. Créez la logique de base en définissant la fonction `add()` pour ajouter un mot
2. Ajouter une *valeur* de type booléenne pour marquer la dernière lettre de la *clé*
   (chaîne représentant le mot intégré à la *trie*)
3. Chaque *nœud interne* ou *feuille* doit ainsi contenir la lettre courante et la *valeur* citée au point n°2
   (True si c'est un mot, False si c'est un prédicat)
4. Créez la fonction `contains()` pour vérifier la présence d'une *clé* dans l'arbre préfixe
5. Développez l'affichage complet

🔹 **Conditions**
- L'affichage se fait via la console
- L'affichage des données doit respecter le format visuel suivant (voir ci-dessous à *Résultat*)
- Utilisez au minimum les mots ci-dessous qui viendront alimenter votre arbre préfixe

🔹 **Mots à intégrer**
[à, arbre, art, artiste, chape, chapeau, créatif, création, œuf, zèbre]

🔹 **Résultat**
```
|
|__à *[à]
|
|__a
|  |__r
|     |__b
|     |  |__r
|     |     |__e *[arbre]
|     |
|     |__t *[art]
|        |__i
|           |__s
|              |__t
|                 |__e *[artiste]
|
|__c
|  |__h
|  |  |__a
|  |     |__p
|  |        |__e *[chape]
|  |           |__a
|  |              |__u *[chapeau]
|  |
|  |__r
|     |__é
|        |__a
|           |__t
|              |__i
|                 |__f *[créatif]
|                 |
|                 |__o
|                    |__n *[création]
|
|__œ
|  |__u
|     |__f *[œuf]
|
|__z
   |__è
      |__b
         |__r
            |__e *[zèbre]
```

