# Skills_assessment

Projet d'évaluation des compétences : Git, Python, Linux

Ce projet consiste en un site d'évaluation des compétences pour les concepts clés de Git, Python et Linux. L'objectif est de créer un mini-site permettant aux utilisateurs de répondre à des questions aléatoires et de vérifier si leurs réponses sont correctes.

Fonctionnalités
Affiche une question aléatoire sur les concepts clés de Git, Python ou Linux.
Un bouton "Random Question" pour charger une nouvelle question.
Un champ de texte pour que l'utilisateur puisse saisir sa réponse.
Un bouton "Evaluate Answer" pour vérifier la réponse.
Affiche si la réponse est validée ou non.

Installation

1. Clonez le repository sur votre instance Linux :
git clone https://github.com/<username>/<repository_name>.git
cd <repository_name>

2. Créez un environnement virtuel et activez-le :
python3 -m venv venv
source venv/bin/activate

3. N'oubliez pas d'installer les dépendances requises (toutes présentes dans le fichier app_qcm.py)

Utilisation

1. Exécutez l'application :
python app_qcm.py

2. Accédez au site via l'adresse IP publique de l'instance : http://13.36.166.94:8080/

Fonctionnalités : 
- Passage d'un test sur linux/python/git sous forme de 4 questions sous timer de 15 secondes par question, un score sera affiché à la fin du questionnaire
- Génération aléatoire de questions à partir d'une banque de questions disposé dans une base de données SQLite3
- Portail Admin permettant de voir toutes les questions présentes dans la base de données, d'ajouter des questions, de les supprimer et de les modifier

Licence
Ce projet est sous licence MIT.
