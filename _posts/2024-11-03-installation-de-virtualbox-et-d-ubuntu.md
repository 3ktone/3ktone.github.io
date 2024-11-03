---
layout: post
title: Installation de VirtualBox et d'Ubuntu
date: 2024-11-03 19:48:54
categories: [Cours, Linux pour débutant]
tags: [VirtualBox, Ubuntu, Tutoriel, Installation, MachineVirtuelle, Virtualisation, Linux, Windows, macOS, Debutant, GuidePasAPas, ISOUbuntu, ConfigurationVM, OpenSource, ApprendreLinux]
---

## Introduction
Ce guide couvre l'installation de VirtualBox, un logiciel de virtualisation open source, et d'Ubuntu, une distribution Linux populaire, en tant que machine virtuelle. Une machine virtuelle permet d'executer un OS comme Ubuntu sans affecter le systeme principal, ideal pour experimenter et apprendre Linux.

### Qu'est-ce que VirtualBox et qu'est-ce qu'une VM?

**VirtualBox** est un logiciel de virtualisation open source developpe par Oracle, qui permet d'executer plusieurs systemes d'exploitation sur un seul ordinateur. En pratique, cela signifie que vous pouvez installer et utiliser un systeme dexploitation comme Ubuntu ou Windows a linterieur de votre systeme principal, par exemple Windows ou Linux. Ce type de logiciel est particulierement utile pour tester des OS, executer des applications compatibles avec un autre systeme, ou isoler certaines taches pour la securite.

Une **machine virtuelle** (VM) est un environnement emule par un logiciel comme VirtualBox, qui agit comme un ordinateur independant. Cette machine virtuelle possede ses propres composants "virtuels" : processeur, memoire (RAM), disque dur, etc., qui sont crees en utilisant les ressources de votre ordinateur physique. Elle utilise un fichier dimage disque (comme un fichier .iso pour installer un systeme dexploitation) pour demarrer et fonctionne ainsi comme un ordinateur reel, mais sans necessiter de materiel physique supplementaire. 

Les VM sont particulierement utilisees pour tester de nouveaux environnements ou des configurations sans risquer dendommager le systeme principal.

### Prerequis
- **PC sous Windows, macOS ou Linux**
- **Connexion Internet**
- **Espace libre** : Environ 25 Go pour Ubuntu et VirtualBox.

---

## Etape 1 : Installer VirtualBox

1. **Telecharger VirtualBox** :
   - Rendez-vous sur le site officiel : [virtualbox.org](https://www.virtualbox.org/).
   - Cliquez sur "Download VirtualBox" et choisissez la version pour votre OS (Windows, macOS, ou Linux).

2. **Installer VirtualBox** :
   - Une fois le telechargement termine, lancez linstallateur.
   - Suivez les etapes de l'assistant d'installation :
     - **Windows** : Acceptez les permissions administrateur si demande.
     - **macOS** : Glissez l'icone VirtualBox dans le dossier Applications.
     - **Linux** : Utilisez le gestionnaire de paquets, ex : `sudo apt install virtualbox` (Ubuntu/Debian).

3. **Lancer VirtualBox** : Une fois installe, ouvrez VirtualBox pour verifier que l'installation s'est deroulee correctement. Vous devriez voir l'interface de gestion des machines virtuelles.

---

## Etape 2 : Telecharger l'ISO d'Ubuntu

1. **Aller sur le site d'Ubuntu** :
   - Rendez-vous sur [ubuntu.com/download](https://ubuntu.com/download).
   - Selectionnez "Ubuntu Desktop" et telechargez la derniere version LTS (supportee sur le long terme) pour garantir la stabilite.

2. **Verifier l'ISO** *(optionnel mais recommande)* :
   - Comparer la somme de controle SHA256 de l'ISO telecharge avec celle fournie sur le site. Cela garantit que le fichier n'est pas corrompu.
   - Pour obtenir le SHA256 sous Linux/macOS, utilisez `sha256sum /chemin/vers/ubuntu.iso`, et sous Windows, une application comme **HashMyFiles**.

---

## Etape 3 : Creer une machine virtuelle pour Ubuntu

1. **Ouvrir VirtualBox** :
   - Cliquez sur **"Nouvelle"** dans la barre d'outils.

2. **Configurer la machine virtuelle** :
   - **Nom** : Choisissez "Ubuntu" ou un nom personnalise.
   - **Type** : Selectionnez "Linux".
   - **Version** : Choisissez "Ubuntu (64-bit)".
   - **Memoire** : 4 Go de RAM (4096 Mo) est recommande pour une utilisation fluide. Ne depassez pas 50 % de la RAM de votre machine.
   
3. **Disque dur virtuel** :
   - Selectionnez **"Creer un disque dur virtuel maintenant"**.
   - **Format** : Choisissez VDI (VirtualBox Disk Image).
   - **Type de stockage** : Preferez un disque **dynamique** pour economiser de lespace.
   - **Taille** : 20 Go minimum ; 25 Go recommande.

4. **Ajouter l'ISO d'Ubuntu** :
   - Dans le gestionnaire de VirtualBox, selectionnez votre VM Ubuntu puis **Configuration > Stockage**.
   - Cliquez sur l'icone du CD pour ajouter un **controleur IDE**.
   - **Choisir un disque** > Selectionner l'ISO d'Ubuntu telecharge.

---

## Etape 4 : Installation d'Ubuntu sur la machine virtuelle

1. **Demarrer la VM** :
   - Selectionnez la VM Ubuntu dans VirtualBox et cliquez sur **Demarrer**.

2. **Lancer l'installation** :
   - Apres le demarrage, un ecran vous propose de "Try Ubuntu" ou "Install Ubuntu". Choisissez **Install Ubuntu**.

3. **Configurer Ubuntu** :
   - **Disposition du clavier** : Selectionnez votre langue et disposition.
   - **Mise a jour et autres logiciels** : Choisissez une installation normale et cochez les options pour les mises a jour si vous avez une connexion Internet fiable.
   - **Type d'installation** : Choisissez **Effacer le disque et installer Ubuntu** (cela n'affecte que le disque virtuel).

4. **Creation du compte utilisateur** :
   - Remplissez les champs pour creer un compte utilisateur, incluant le nom, le nom de l'ordinateur, le nom d'utilisateur et le mot de passe.
   
5. **Installation** :
   - Confirmez les parametres et cliquez sur **Installer maintenant**.
   - Patientez pendant que l'installation se termine, puis redemarrez la VM lorsque demande.

6. **Retirer l'ISO d'installation** :
   - Avant de redemarrer, allez dans **Peripheriques > Lecteurs optiques** et deselectionnez lISO, sinon la VM demarrera encore sur l'ISO.

---

## Conclusion
Votre VM Ubuntu est maintenant installee et prete a etre utilisee ! Vous pouvez explorer Linux en toute securite dans un environnement isole.
