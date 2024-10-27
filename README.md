# Le Recipinator

_Le Recipinator_ est un programme d'indexation et de tri des recettes qui sommeillent dans nos livres de cuisine. Pour mieux utiliser nos livres de cuisine, ce programme vous propose de vous plonger dedans et d'ajouter les recettes qui vous font envie en spécifiant les ingrédients nécessaires. Les recettes indexées peuvent ensuite être triées en fonction des ingrédients, du régime ou d'un score de saisonnalité. 

![Capture d'écran de l'outil de sélection des recettes](./doc/screenshots/selection_recettes.png)

**_Le Recipinator_ n'est pas :**  

- un logiciel parfaitement développé et terminé
- un agrégateur automatique de recette
- un outil de lecture automatique des livres de recette
- une appli bien développée à installer sur un smartphone. 

## Installation et lancement

### Prérequis

_Le Recipinator_ est écrit en Python. Il requiert à minima les librairies suivantes: 

- PyYAML
- numpy
- pandas
- streamlit

Une fichier `requirements.txt` se trouve dans le fichier racine avec la liste complètes des paquets que j'ai utilisés pour le développement.

### Installation 

Pour installer _le Recipinator_, téléchargez l'archive contenant le code et extrayez-la dans le dossier de votre choix. Je vous recommande de supprimer l'intégralité du contenu du dossier `recipes`. (Ce sont les recettes de la maison que je stocke ici en cas de crash. Un jour il y aura une branche de prod comme pour un vrai code et vous n'aurez plus à faire le sale boulot.)

### Lancement (Linux ou apparenté)

Pour lancer _le Recipinator_, exécutez la ligne de commande suivante dans le dossier contenant le script `run_recipinator.py`:

> ```python3 -m streamlit run run_recipinator.py```

Cela aura pour effet de lancer une application web ressemblant à cette capture ci-dessous:

![Capture d'écran de la page d'accueil du Recipinator](./doc/screenshots/frontpage.png)

À partir de là, laissez-vous guider. Vous pourrez notamment ajouter une nouvelle base de donnée au bas de la page d'accueil. 

## Remerciements

Le classement par saison doit beaucoup à la liste envoyée par [La Gazinière](https://lagaziniere850fcs.wordpress.com/) dans leur newsletter mensuelle. Merci à elleux pour leurs bonnes recettes et leurs recommandations culinaires ! 