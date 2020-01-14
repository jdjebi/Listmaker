# Fiche de travail

## python_core

### To add
- Modélisation UML de la classe de view console
- Aucune gestion d'intégrité des données
- Mettre à jour les modélisations
- Réorganiser l'ensemble du projet
- Transformer les modules lmk en un ensemble de package
- Standariser le LmkViewer1 avec l'ensemble du en d'autres intégrer dans le python_core
- Faire en sorte qu'on puisse utiliser les fichier .

- utiliser la commande open en processus
	- L'ajout de processus entraine la gestion du processus. En fait lorsque le programme principal est fermé si le processus a été lancé alors ce dernier n'est fermé automatiquement, il faut le faire manuellement

- La recherche des fichiers de données doit se faire dans les dossiers spécifié dans le fichier ".config"

### Brainstorming
- Utiliser des variables d'environement

### CLI 1:
 Le CLI permet de:

 - Créer une liste: La création de d'une liste se fait en définissant ses colonnes le fichier de la liste est enregistré pour le moment dans le dossier python_core/test_files_created

 - Supprimer une liste par la bias d'un identifiant

 - Afficher la liste les listes crées

 - Sélectionnez une liste particulière afin de pouvoir y ajouter des éléments plus facilement

 - Lorsqu'une liste est sélectionnée de nouvelles commandes sont disponibles à savoir:

 	- view: Afficher le contenu de la liste dans un tableau
 	- info: Affiche des infos de la liste(ID CLI, Chemin du fichier,Titres des colonnes Nombre d'élement)
 	- insert: Ajout d'une nouvelle ligne (Les ajouts ne sont pas enregistrés)
 	- save: Enregistre les mise à jours

---
Les autres commandes sont les commandes sont les suivantes:

- clear: efface l'écran
- exit: Quitte le CLI
- list: Affiche les Fichiers de liste du dossier python_core/test_files_created
- ^view: [0-9]+ // ID : Affiche la liste d'ID
- ^del: [0-9]+ // ID : Supprime la liste d'ID correspondant
- ^select: [0-9]+ // ID: Sélectionne la liste d'ID correspondant
- ^unselect: Désélectionne la liste sélectionnée
- ^create (.)+ // NOM_LISTE: Crée un fichier de liste dans le dossier python_core/test_files_created dont le nom est NOM_LISTE

### CLI 2:
- Le CLI utilise un fichier de configuration pour spécifier le dossier qui sera utiliser pour comme dossier de travailler en lecture et écriture. Il s'agit d'un nommé "config" à la racine du CLI sa suppression entrainera un dysfonctionnement de toute l'application


- Nouvelles commande:

^open : Affiche la liste sélecionnée dans une fenêtre
^open [0-9]+ // ID: affiche la liste dans une fenêtre
