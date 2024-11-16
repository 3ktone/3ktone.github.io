---
layout: post
title: Le Terminal
date: 2024-11-16 18:56:00
categories: [Cours, Linux pour débutant]
tags: [Terminal, Ubuntu, CommandesDeBase, Clear, RaccourcisClavier, mkdir, touch, cd, GestionnaireDeFichiers]
---

# Commandes de base dans un terminal

Nous allons voir dans ce guide les commandes de base pour naviguer et gerer des fichiers ou dossiers dans un terminal Ubuntu. C'est un point de depart pour comprendre comment interagir avec le systeme sans interface graphique et communiquer avec notre systeme d'exploitation.
Car oui, le terminal est simplement une fenetre de communication entre l'utilisateur et l'OS.
La premiere chose  que nous allons voir est comment utiliser le terminal comme gestionnaire de fichier.

---
# `pwd` 
### Description
 Pour commencer la commande `pwd` (Print Working Directory) affiche le chemin absolu du repertoire dans lequel vous vous trouvez actuellement. Elle est essentielle pour comprendre votre position dans l'arborescence des fichiers.
 
  ## Utilisation de base - **Afficher le chemin absolu du repertoire courant** : 

```bash
pwd
```
En tapant cette commande vous devriez vous trouver dans /home/votre_nom car vous etes un utilisateur et vous pouvez meme lui demander avec la commande who am i?
```bash
whoami
```
Le terminal devrais vous donner votre nom d'utilisateur.
Vous savez maintenant dire "ou suis-je?" et "Qui suis-je?"

---

## `ls` - Lister les fichiers et dossiers

### Description
La commande `ls` affiche le contenu d'un repertoire.

### Utilisation
- **Lister les fichiers et dossiers** :  
  ```bash
  ls
  ```

- **Afficher les details des fichiers et dossiers** :  
  ```bash
  ls -l
  ```
  Cela inclut les permissions, le proprietaire, la taille, et la date de modification.

- **Lister les fichiers caches** :  
  ```bash
  ls -a
  ```
  
---

## `cd` - Changer de repertoire (Change Directory)

### Description
La commande `cd` permet de naviguer dans les repertoires du systeme de fichiers.

### Utilisation
- **Se deplacer dans un repertoire** :  
  ```bash
  cd nom_du_dossier
  ```
  Exemple :  
  ```bash
  cd Documents
  ```

- **Retourner a votre repertoire personnel (Home)** :  
  ```bash
  cd ~
  ```  
  ou simplement :  
  ```bash
  cd
  ```

- **Revenir au repertoire parent** :  
  ```bash
  cd ..
  ```

- **Monter de plusieurs niveaux dans l'arborescence** :  
  ```bash
  cd ../..
  ```

- **Utiliser un chemin absolu pour naviguer** :  
  ```bash
  cd /usr/share
  ```

### Notes
- Un chemin absolu commence toujours par `/`, qui represente la racine du systeme.
- Un chemin relatif est base sur votre position actuelle dans l'arborescence des fichiers.

---

## `cat` - Visualiser le contenu dun fichier

### Description
La commande `cat` permet d'afficher le contenu d'un fichier directement dans le terminal.

### Utilisation
- **Afficher un fichier texte** :  
  ```bash
  cat nom_du_fichier
  ```
  Exemple :  
  ```bash
  cat README.txt
  ```

### Notes
- `cat` est utile pour visualiser rapidement des fichiers texte sans ouvrir d'editeur.

---

## `mkdir` - Creer un repertoire

### Description
La commande `mkdir` cree un nouveau dossier.

### Utilisation
- **Creer un repertoire** :  
  ```bash
  mkdir nom_du_dossier
  ```

- **Creer un repertoire avec des sous-dossiers en une seule commande** :  
  ```bash
  mkdir -p dossier_principal/sous_dossier
  ```

### Notes
- L'option `-p` est particulierement utile pour eviter les erreurs si un repertoire dans le chemin n'existe pas encore.

---

## `touch` - Creer un fichier

### Description
La commande `touch` cree un fichier vide.

### Utilisation
- **Creer un fichier texte** :  
  ```bash
  touch fichier.txt
  ```

- **Creer un fichier avec une autre extension** :  
  ```bash
  touch fichier.log
  ```
  Vous pouvez utiliser n'importe quelle extension (.txt, .log, .py, etc.).

---

## `rm` - Supprimer des fichiers

### Description
La commande `rm` supprime un fichier ou un dossier.

### Utilisation
- **Supprimer un fichier** :  
  ```bash
  rm nom_du_fichier
  ```

- **Supprimer un dossier vide** :  
  ```bash
  rm -d nom_du_dossier
  ```

- **Supprimer un dossier avec tout son contenu** :  
  ```bash
  rm -r nom_du_dossier
  ```

- **Forcer la suppression (sans confirmation)** :  
  ```bash
  rm -rf nom_du_dossier
  ```

### Attention
La commande `rm -rf` est puissante et doit etre utilisee avec prudence, car elle supprime tout sans possibilite de recuperation.

---

## `rmdir` - Supprimer un repertoire vide

### Description
La commande `rmdir` supprime un repertoire, mais uniquement s'il est vide.

### Utilisation
- **Supprimer un repertoire vide** :  
  ```bash
  rmdir nom_du_dossier
  ```

- **Supprimer un repertoire contenant des sous-dossiers ou fichiers** :  
  `rmdir` ne fonctionne pas dans ce cas. Utilisez `rm -r` a la place :  
  ```bash
  rm -r nom_du_dossier
  ```

---
### Exercice pratique : Creer et organiser des fichiers/dossiers via le terminal

#### Objectif  
Nous allons creer une structure de dossiers et de fichiers dans notre terminal, puis nous allons verifier que le resultat soi le meme avec un gestionnaire de fichiers graphique. Cet exercice vous permettra de comprendre comment gerer vos fichiers/dossiers en ligne de commande et de comparer avec l'interface graphique.

---

#### Etape 1 : Creer un dossier principal  

1. Dans le terminal, creez un dossier appele `ProjetTerminal` :  
   ```bash
   mkdir ProjetTerminal
   ```

2. Naviguez dans ce dossier :  
   ```bash
   cd ProjetTerminal
   ```

3. Verifiez votre position actuelle avec `pwd` :  
   ```bash
   pwd
   ```
   Resultat attendu :  
   ```
   /home/votre_nom_utilisateur/ProjetTerminal
   ```

---

#### Etape 2 : Creer des sous-dossiers et fichiers  

1. **Creer deux sous-dossiers** :  
   ```bash
   mkdir Documentation Code
   ```

2. **Naviguer dans le dossier `Documentation` et creer un fichier texte** :  
   ```bash
   cd Documentation
   touch README.txt
   ```

3. **Ajouter un fichier dans le dossier `Code` depuis votre position actuelle** :  
   ```bash
   touch ../Code/script.py
   ```

4. **Verifier la structure creee** :  
   Revenez au dossier principal avec :  
   ```bash
   cd ..
   ```
   Affichez son contenu :  
   ```bash
   ls -l
   ```

   Vous devriez voir :  
   ```
   drwxr-xr-x 2 votre_nom votre_nom 4096 date heure Code
   drwxr-xr-x 2 votre_nom votre_nom 4096 date heure Documentation
   ```

---

#### Etape 3 : Ouvrir le gestionnaire de fichiers graphique  

1. Ouvrez le gestionnaire de fichiers dans le dossier actuel avec la commande :  
   ```bash
   xdg-open .
   ```
   Cela ouvrira le dossier `ProjetTerminal` dans votre gestionnaire de fichiers graphique.

2. Naviguez dans les sous-dossiers pour verifier que `README.txt` et `script.py` existent.

---

#### Etape 4 : Modifier un fichier avec le terminal  

1. Ouvrez le fichier `README.txt` avec un editeur de texte en ligne de commande :  
   ```bash
   nano Documentation/README.txt
   ```

2. Ajoutez du contenu, par exemple :  
   ```
   Ceci est un fichier de documentation pour le projet Terminal.
   ```

3. Enregistrez et quittez l'editeur en appuyant sur **Ctrl + O**, puis **Entree**, et enfin **Ctrl + X**.

---

#### Etape 5 : Supprimer la structure  

1. Supprimer le dossier et tout son contenu :  
   Revenez au dossier parent avec :  
   ```bash
   cd ..
   ```
   Puis executez :  
   ```bash
   rm -rf ProjetTerminal
   ```

2. Verifiez que le dossier a ete supprime :  
   ```bash
   ls
   ```

---

#### Resultat attendu  

A la fin de cet exercice, vous aurez appris a :  
- Creer et organiser des dossiers et fichiers avec `mkdir` et `touch`.
- Naviguer dans les dossiers avec `cd`.
- Ouvrir et modifier un fichier avec un editeur de texte en ligne de commande.
- Verifier votre travail dans un gestionnaire de fichiers graphique.

---

## `clear`  - Nettoyer l'affichage du terminal  

### Description La commande 
- `clear` permet de nettoyer l'ecran du terminal, supprimant toutes les lignes precedentes et laissant un terminal "propre". C'est une commande utile pour garder une interface lisible, surtout apres avoir execute plusieurs commandes.  
## Utilisation de base  - **Nettoyer l'ecran du terminal** :
```bash
clear
```

---
## Raccourci clavier equivalent

- Au lieu de taper `clear`, vous pouvez utiliser le raccourci clavier suivant :  
    **`Ctrl + L`**  
    Ce raccourci a le meme effet que la commande `clear`.

---

## Notes importantes

1. **L'historique des commandes n'est pas supprime** :  
    Meme si l'ecran est nettoye, vous pouvez toujours naviguer dans l'historique des commandes en utilisant les fleches haut et bas.
    
2. **Pratique pour les longues sessions** :  
    Si vous executez de nombreuses commandes, utiliser `clear` ou `Ctrl + L` peut rendre le terminal plus lisible et mieux organise.
    

---

## Exemple pratique

1. **Avant d'utiliser `clear` ou `Ctrl + L`** :  
    Vous avez un terminal rempli de texte et souhaitez repartir avec un ecran vide.
    
```bash
echo "Ceci est un test"
pwd
ls

```
    
2. **Utilisation de `clear` ou `Ctrl + L`** :  
    Entrez :
    
    bash
    
    Copier le code
    ```bash
    clear
```
    ou appuyez sur **`Ctrl + L`**.
    
3. **Apres nettoyage** :  
    L'ecran sera vide, pret pour de nouvelles commandes.
    

---

## Commandes complementaires

- **`exit`** : Pour quitter le terminal.
- **`history`** : Pour afficher l'historique des commandes executees

---
## Conclusion
Ces commandes vous permettent de naviguer dans le systeme de fichiers et de gerer les dossiers et fichiers sans interface graphique. Avec de la pratique, vous deviendrez rapidement a l'aise avec le terminal.

---