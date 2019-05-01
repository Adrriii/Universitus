# Rapport Universitus

## Introduction

### Présentation du context

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

#### Jeu

## Fonctionnalités

## Gestion du projet



