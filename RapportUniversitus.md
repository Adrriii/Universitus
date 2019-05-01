# Rapport Universitus

## Introduction



Ce projet s'inscrit dans le cours de Projet de Communication Transdisciplinaire. <br> Nous devons mettre en place un guide pour les nouveaux étudiants en informatique, leur permettant de faire connaissance avec les services disponibles à l'université, et leur permettant d'apprendre les commandes de base de Linux.

## Implémentation

### Choix technique

Le jeu sera une application web, permettant ainsi de faciliter son accès aux utilisateurs. Nous avons donc due passer par une phase d'apprentissage des technologies liées au web, car la majorité de notre groupe n'avait que quelques bases dans ce domaine.

#### Front-End

Pour le côté utilisateur, nous avions dans un premier temps cherché à utilisé des émulations de terminaux pré-fait. Mais ceux que nous avions trouvé n'étaient pas suffisament modulables, étaient "lourds", et ajoutés de nombreuse technologies à connaitre (ReactJs, Less, ...).

Nous avons donc décidé de réaliser le terminal nous même, inspiré de divers projet libre sur github. L'émulation du terminal à donc été réalisé en Javascript, sans utiliser de framework. Cela nous a permi de garder une application légère que nous maitrisions.

Nous avons donc utilisé du HTML 5, CSS 3 et Javascript ES6. Notre application est donc compatible avec une large majorité de navigateur web.

Pour la communication avec le serveur, nous avons utilisé dans un premier temps des appels Ajax. Puis en testant différentes technologies, nous avons décidés d'utiliser les WebSocket. Cela nous a permis de grandement simplifié la communication avec le serveur, toujours en gardant une compatibilité avec les navigateurs web les plus utilisés.

#### Back-End

Côté serveur, nous avons décidé d'utiliser NodeJs. Ce choix nous permettais d'utiliser nos connaissances nouvellement apprises en javascript pour le front-end côté serveur. De plus, l'utilisation de NodeJs nous permettait d'utiliser le package Dockerode, qui nous permet de simplifier la gestion des conteneurs.

##### Conteneurs

Nous avons décidé d'utiliser Docker, qui permet de fournir à l'utilisateur un univers *bac-à-sable* dans lequel il pourra réaliser des actions qui seraient normalement *dangereuse*. Ainsi, même si l'utilisateur parvient à supprimer des éléments importants du système entrainant un crash du conteneur, on pourra facilement le relancer. Et cela sans impacter les autres utilisateurs.

Les conteneurs sont géré par le serveur, grâce à Dockerode. Le conteneur est créé à la connexion de l'utilisateur, et est fermé lorsqu'il quitte l'application.

#### Jeu

Pour le jeu, nous pouvions utiliser n'importe quel langages grâce à l'utilisation des conteneurs. Nous devions utiliser un langage nous permettant de faire des appels aux commandes Linux.

Nous avons choisi Python 3, car c'est un langage que nous avons tous vue en cours, et notre application ne demande pas des performances très élevées. De plus, Python est un langage de haut niveau, qui nous permet de gagner du temps de développement et de traiter facilement les chaines de caractères.

Notre jeu a été réalisé en gardant à l'esprit qu'un utilisateur puisse facilement ajouter du contenue. Ainsi l'ajout de quête et de personnages se font à l'aide de fichier de configuration.

Notre jeu est une surcouche du système, dans lequel le joueur est bloqué. Le joueur évolue donc dans l'arborescence du système, dans lequel le jeu ajoute du contenu.



## Fonctionnalités

## Gestion du projet

Pour la gestion de notre projet, nous avons utilisé les fonctionnalités fourni par GitLab. Nous avons ainsi les taches planifiées dans un ScrumBoard, nous permettant de générer automatiquement le diagramme de Gantt.

La première partie du projet à été la réalisation du cahier des charges.

