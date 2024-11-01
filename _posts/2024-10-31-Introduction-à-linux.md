---
layout: post
title: introductio-à-linux
date: 2024-10-31 20:24:26
categories: [Cours, Linux pour débutant]
tags: [linux, distribution, ubuntu, debian, kubuntu, kde, elementaryOS, linuxMint, environement-de-bureau, opensSUZE, Slakware]
---

# Introduction à Linux
---

## Qu'est-ce que Linux ?
Nous allons explorer ensemble Linux pour te donner les connaissances necessaires afin de devenir un utilisateur avance. Mais dabord, posons nous la question : **Qu'est-ce que Linux ?**  
La reponse varie selon la personne interrogee, mais revenons un peu en arriere pour comprendre son origine.

## Historique : Les debuts de Linux
Dans les annees 80, **Richard Stallman**, travaillant au laboratoire d'IA du MIT, a lance un projet visant a creer un systeme UNIX entierement libre et ouvert. Cette initiative est nee d'une frustration : une licence de nouvelle imprimante du labo lempechait de modifier son code. Stallman, qui avait deja modifie des imprimantes pour notifier letat de limpression permettant de savoir quand l'imprimante etait libre, souhaitait continuer dans cette direction.

### GNU et Linux
Au debut des annees 90, il existait presque suffisamment de logiciels libres pour un systeme complet, mais le noyau **GNU Hurd** etait encore en developpement. En parallele, **Linus Torvalds** a commence un projet de hobby pour developper un noyau UNIX appele **Linux**. Associe aux outils GNU, ce noyau a permis la creation dun systeme dexploitation libre.

### Definition de GNU

**GNU** (acronyme recursif pour "GNU's Not Unix") est un projet lance en 1983 par **Richard Stallman** dans le but de creer un systeme d'exploitation libre, offrant une alternative ouverte a UNIX. Le projet GNU vise a fournir aux utilisateurs une liberte complete pour utiliser, modifier, et partager leur logiciel. Bien qu'il ait ete inspire par UNIX, GNU n'est pas identique a UNIX et est concu pour etre completement independant de tout code UNIX proprietaire.

Le projet a permis de developper des outils essentiels comme le compilateur **GCC**, l'editeur **Emacs**, et de nombreuses autres applications necessaires au fonctionnement dun OS complet. Cependant, le noyau du projet GNU, appele **GNU Hurd**, n'a pas ete finalise. C'est pourquoi le noyau **Linux**, developpe par **Linus Torvalds** en 1991, a ete combine avec les outils GNU pour creer une solution complete, souvent appelee "GNU/Linux".

[GNU sur Wikipedia](https://fr.wikipedia.org/wiki/GNU)

---

### Qu'est-ce qu'UNIX ?

**UNIX** est un systeme d'exploitation multitache et multi-utilisateur cree dans les annees 1970 par **Ken Thompson** et **Dennis Ritchie** aux laboratoires Bell d'AT&T. Il est repute pour sa portabilite, sa simplicite et sa robustesse. UNIX a pose les bases pour de nombreux systemes d'exploitation modernes, notamment grace a son utilisation de la **hierarchie des fichiers**, de **la ligne de commande** et des **permissions d'utilisateur**.

De nombreux systemes modernes, tels que **Linux** et **macOS**, sont inspires de UNIX ou sont directement bases sur sa structure.
Voici le lien Wikipedia pour **UNIX** :

[UNIX sur Wikipedia](https://fr.wikipedia.org/wiki/Unix)

---

### Rapport entre UNIX et macOS (Apple)

macOS, le systeme d'exploitation d'Apple pour ses ordinateurs Macintosh, est derive d'UNIX via **BSD (Berkeley Software Distribution)**, une variante libre d'UNIX. macOS s'appuie sur le noyau **XNU** (qui signifie "X is Not Unix" tout comme GNU), mais reste conforme a larchitecture UNIX. Il combine des technologies UNIX avec une interface graphique developpee par Apple, offrant ainsi les avantages de la stabilite et de la securite dUNIX.

Ce lien fort avec UNIX confere a macOS une compatibilite avec de nombreux outils UNIX, ce qui le rend populaire aupres des developpeurs et des utilisateurs avances recherchant un environnement UNIX tout en profitant de l'ecosysteme Apple.

---

# Distribution Linux : Debian et Ubuntu

## Les distributions Linux
Une distribution Linux est une version specifique de Linux, regroupant le noyau et des logiciels supplementaires.  
La distribution **Debian**, sponsorisee par la Free Software Foundation, est devenue la base d'une multitude de distributions Linux en raison de sa popularite et de sa nature libre. Aujourdhui, **Debian** est une grande communaute ou chacun peut contribuer.

### Ubuntu : une distribution populaire
Dans les annees 2000, **Canonical** a lance **Ubuntu**, une distribution basee sur Debian mais plus orientee utilisateur. Ubuntu est publiee deux fois par an avec un support a long terme (LTS) tous les deux ans.

**Nom des versions d'Ubuntu :**
- Les versions suivent le format annee/mois (par ex. : **15.10** pour octobre 2015).
- Les versions LTS (support de 5 ans) sont publiees en avril tous les deux ans.

## Installer Ubuntu
1. Rendez-vous sur [ubuntu.com](https://ubuntu.com) et telechargez la derniere version dans la section "Desktop".
2. Pour les serveurs, privilegiez la version LTS (support a long terme).
3. Choisissez le type de telechargement : via le navigateur ou via un **fichier torrent** (utile pour une connexion lente).

---

# Installation dans VirtualBox

## Utiliser une machine virtuelle
Avant d'installer Ubuntu sur le disque dur, on peut utiliser **VirtualBox** pour creer une machine virtuelle (VM) et decouvrir le systeme sans s'engager.  
Pour ce faire :
1. Telechargez VirtualBox sur [virtualbox.org](https://virtualbox.org).
2. Selectionnez le package pour votre systeme d'exploitation principal (ex. : **Windows 10**).

---
