---
layout: post
Title: Architecture réseau et protocoles
date: 2023-07-21 08:35:00
categories: [Cours, Fondamentaux]
tags: [Concepts,histoire,réseaux]
---

Introduction Aux Réseaux Informatiques
===

___Salutation Internaute !___

Dans cet article, nous allons faire un peu d'histoire et explorer ce qui nous a mené à la création d'Internet et certaines de ses innovations techniques que nous utilisons encore aujourd'hui...

Il était une fois, ARPANET!
---

L'histoire d'Internet remonte aux années 1960 et 1970, lorsque les premiers réseaux informatiques ont commencé à être développés. À l'époque, les ordinateurs étaient d'énormes machines généralement isolés et utilisés de manière indépendante, principalement dans le domaine de la recherche ou des grandes entreprises spécialisées. Cependant, les chercheurs et les scientifiques ont rapidement réalisé les avantages potentiels de la communication entre les ordinateurs et ont commencé à explorer des moyens de connecter ces systèmes.

C'est à cette même époque que l'**ARPA** (Advanced Research Projects Agency), une agence du département américain de la Défense, a initié le développement d'un réseau expérimental appelé **ARPANET**. Son objectif était de permettre aux chercheurs de partager des ressources informatiques et de communiquer entre les différents centres de recherche. On peut considérer ARPANET comme le prédécesseur direct d'Internet.

![ARPANET](/images/Arpanet_map_1973.jpg){: width="550" }

Cette image représente la map logique du réseau ARPANET à ses balbutiements. On peut voir que le réseau connectait principalement des universités américaine et des centres de recherches comme le MIT, Harvard ou UCLA à travers les Etats-Unis.

Architecture Réseau
---

Il est difficile de ce représenter ce qu'est Internet de nos jours, une simple recherche sur Google, un des accès les plus populaires pour accéder à internet, affiche des millions de résultats sur une même page! Mais ou sont tous ces sites? Comment sont-ils arrangés?

Physiquement, ce sont pour la plupart des serveurs au quatre coin du globe qui, derrière les rideaux, représenter par du code et des protocoles, convenant des règles de conduite du quand et du pourquoi, réside un concept simple, l'architecture! La disposition qu’assume un groupe formant un ensemble dans un espace déterminé...Tel la silhouette d'une ville au loin, offrant divers services à ses citoyens numérique, on peut discerner des quartiers, assumant une forme ou une autre dépendant des besoins et des caractéristiques de leurs habitants virtuels.

Dans le contexte de la guerre froide, où les tensions mondiales et la menace d'un conflit nucléaire étaient omniprésentes, l'importance d'un réseau de communication résilient et robuste est devenue évidente. Face à la possibilité de catastrophes nucléaires pouvant détruire une grande partie des infrastructures de communication, une nouvelle approche devait être empruntée pour garantir que les communications puissent survivre à de tels événements.

C'est dans ce contexte que le concept du réseau **maillé** (ou mesh network en anglais), une des configurations possible pour un réseau, a émergé comme une solution prometteuse. Le réseau maillé était conçu pour être flexible, adaptable et capable de survivre à des pannes locales ou à des attaques ciblées, car il ne dépendait pas d'une infrastructure centrale vulnérable.

Et au lieu de s'appuyer sur des routes de communication préétablies comme celle du réseau téléphonique, le réseau maillé reposait sur un système interconnecté de nœuds et de liaisons. Chaque nœud du réseau était capable de communiquer directement avec ses nœuds voisins et de transmettre des données à travers le réseau en utilisant divers chemins. Cette architecture distribuée assurait que les données pouvaient contourner les points de défaillance et trouver rapidement des itinéraires alternatifs pour atteindre leur destination.

Ainsi, le réseau maillé offrait une résilience exceptionnelle et une capacité de récupération rapide en cas de perturbations majeures, ce qui en faisait une ressource inestimable en cas de crise ou de catastrophe. Pendant la guerre froide, cette approche innovante a été largement adoptée pour développer des réseaux de communication militaires capables de résister à d'éventuelles attaques ou destructions de centres névralgiques.

On peut trouver des similitudes conceptuelles entre le réseau maillé et certains aspects d'Internet. Bien qu'Internet ne soit pas un réseau maillé au sens strict, il est constitué de multiples réseaux interconnectés à différents niveaux (réseaux des FAI, réseaux d'entreprises, etc.), ce qui forme une structure distribuée avec des liaisons entre ces différents réseaux. Cette interconnexion permet aux données de trouver des chemins alternatifs en cas de congestion ou de défaillance d'une partie du réseau.

Voici un exemple des principales configurations possible pour un réseau:

![topologie réseau](/images/topologie%20réseau.png){: width="550" }

Protocoles De Communications
---

*C'est quoi un **protocole**?*
![Service de table](/images/IllustrationServiceTable.jpg)

Une bonne manière de ce le représenter est cette images dantesque d'un service de table complet, avec tous ses couverts, verres, assiettes.
Qui commence à manger en premier? Et comment interagir de manière ordonnée pour que tout se passe bien? Et bien, l'interprétation est la même!
Un protocole définit les règles pour que les appareils communiquent efficacement et puissent agir de manière organisée celons un ensemble de règles prédéfinit.

Contrairement à l'approche **centralisée**, où toutes les données doivent passer par un point central avant d'atteindre leur destination, le routage des paquets a été choisi comme alternative pour la transmission des données. Cette approche permet de découper les données en petits paquets, chacun contenant des informations sur sa source, sa destination et une partie des données elles-mêmes. Ces paquets sont acheminés à travers le réseau en utilisant des protocoles et des algorithmes spécifiques par les routeurs, qui déterminent en temps réel le meilleur chemin à suivre pour chaque paquet afin de les faire parvenir à leur destination.

Grâce à cette approche de transmission par paquets et de routage, lorsqu'un paquet est envoyé, il entre dans un réseau complexe de routeurs qui se chargent de le faire parvenir à sa destination. Chaque routeur examine les informations contenues dans le paquet, telles que l'adresse de destination, et utilise les protocoles **TCP/IP** (Transmission Control Protocol/Internet Protocol) spécifiques pour déterminer le meilleur chemin à suivre en temps réel.
C'est de la que vient le mot **IP**! c'est l'adressage que l'on utilise sur Internet comme protocole de communication, IP adresses!

L'une des caractéristiques clés du TCP/IP est sa nature décentralisée et son architecture ouverte. Contrairement à d'autres protocoles propriétaires de l'époque, le TCP/IP était un standard ouvert, open source, accessible à tous. Cette approche a favorisé l'adoption universelle du protocole et a permis l'expansion rapide d'Internet, sans dépendre d'une seule entité ou entreprise.

Conclusion:
---

Internet est une longue histoire qui débute par de la **recherche militaire** dans un conflit géopolitique sans précédent, suivant le chemin ouvert part les pionniers de la recherche et d'autre anonymes comme les **Cypherpunks**, guidé par une volonté sans faille de distribution global d'information qui suit son court encore aujourd'hui.

Nous avons aussi effleuré la notion de **topologie** de réseau avec l'introduction du réseau maillé, ainsi que les règles régissant les échanges sur les réseaux,comme le protocole TCP/IP.

Pour ceux que ça intéresse, j'ai une petite surprise!

![Internet en 2010 Opte](/images/network-2010.png){: width="450" }

Cette image est une représentation numérique d'internet en 2010 faites par Opte.org.

Comme ils est dit dans la section "à propos" du site:

> Certaines personnes ont besoin de voir pour comprendre.
> Étant donné que l'Internet est un immense regroupement de réseaux individuels qui permettent une communication relativement fluide des données, il semblait logique de tracer des lignes d'un point à un autre.
> Ce projet a été un travail d'amour de plus de 17 ans sous le nom de "The Opte Project".

***Qu'est ce qu'est OPTE project?***

[The Opte Project](https://www.opte.org/) est une magnifique représentation graphique de l'évolution d'Internet entre 1997 et 2021, avec des couleur pour les différencier .

Dans le site on peu retrouver une visualisation du [black-out d'Internet en Iran](https://youtu.be/BUtlP1kVo-4) en 2019 était une interruption totale d'une semaine du fonctionnement d'Internet.

Pour finir, je vous laisse profitez du spectacle en vidéo!

<iframe width="940" height="528" src="https://www.youtube.com/embed/DdaElt6oP6w" title="The Internet:  1997 - 2021 (1m)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
