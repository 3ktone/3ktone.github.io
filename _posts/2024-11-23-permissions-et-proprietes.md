---
layout: post
title: Permissions et Propriétés
date: 2024-11-23 11:55:34
categories: [Cours, Linux pour débutant]
tags: [Linux, Permissions, Commandes, ls, chown, chmod, Proprietaire, Groupe, Scripts, Bash, MatrixEffect, Exercices, Tutoriel, Pratique, CommandesLinux, Scripting, Terminal, Administration]
---

## Introduction

La commande `ls -l` permet dafficher des informations detaillees sur les fichiers et dossiers dans Linux, y compris leurs metadonnees et permissions.

## Comprendre les Permissions

Voici un exemple de sortie de la commande `ls -l` :

```
drw-r--r-- 2 nemo nemo 4.0K Nov 22 10:13 dossier
-rw-r--r-- 1 nemo nemo   13 Nov 22 10:06 fichier.txt
-rwxr-xr-x 1 nemo nemo  151 Nov 22 10:09 matrix.sh
```

### Analyse des Permissions

1. **Premier caractere** :
    - `d` : indique un dossier (directory)
    - `-` : indique un fichier
2. **Groupes de 3 caracteres** (par exemple, `rw-`) :
    - **Proprietaire** : droits accordes au createur du fichier.
    - **Groupe** : droits pour les utilisateurs du groupe.
    - **Public** : droits pour tous les autres.
3. **Caracteres possibles** :
    - `r` : lecture (read)
    - `w` : ecriture (write)
    - `x` : execution (execute)
    - `-` : aucun droit

### Exemple dinterpretation

```
-rwxr-xr-x 1 nemo nemo 151 Nov 22 10:09 matrix.sh
```

- **`-`** : cest un fichier.
- **`rwx`** : le proprietaire (nemo) peut lire, ecrire et executer.
- **`r-x`** : le groupe peut lire et executer.
- **`r-x`** : les autres peuvent lire et executer.

### Proprietaire et Groupe

Les champs suivants indiquent :

- **Premier nom** : le proprietaire du fichier (ex. `nemo`).
- **Second nom** : le groupe proprietaire (ex. `nemo`).

---

## Modifier les Permissions

### Changer le Proprietaire

Utilisez la commande `chown` pour modifier le proprietaire et/ou le groupe :

```bash
chown utilisateur:groupe fichier.txt
```

### Modifier les Permissions

Pour ajuster les permissions, utilisez `chmod` avec une notation numerique :

```bash
chmod 664 fichier.txt
```

#### Signification des valeurs :

- **4** : lecture (`r`)
- **2** : ecriture (`w`)
- **1** : execution (`x`)
- **0** : aucun droit

**Exemple pour `664` :**

- **6** (4+2) : lecture + ecriture pour le proprietaire.
- **6** (4+2) : lecture + ecriture pour le groupe.
- **4** : lecture seule pour les autres.

---

## Exercices Pratiques

### Exercice 1 : Analyser des Permissions

Analysez les permissions suivantes :

```
drwxr-xr-x 2 root root 4096 Nov 22 10:13 dossier_root
```

- **`d`** : cest un dossier.
- **`rwx`** : le proprietaire (root) peut lire, ecrire et executer.
- **`r-x`** : le groupe peut lire et executer.
- **`r-x`** : les autres peuvent lire et executer.

### Exercice 2 : Modifier des Permissions

Un fichier `script.sh` a les permissions suivantes : `-rw-r--r--`.

1. Rendre le fichier executable par le proprietaire uniquement :
    
    ```bash
    chmod 744 script.sh
    ```
    
2. Retirer tous les droits au public :
    
    ```bash
    chmod 640 script.sh
    ```
    

---

## Creation dun Effet "Matrix" en Bash

Voici un script pour simuler leffet Matrix dans un terminal.

### Code du Script

```bash
#!/bin/bash

# Active la couleur verte pour leffet Matrix
echo -e "\e[32m"

# Boucle infinie pour afficher des caracteres aleatoires
while true; do
    echo $RANDOM | md5sum | head -c $((RANDOM % 40 + 10))
    sleep 0.05  # Pause pour creer un effet danimation
done
```

### Utilisation

1. Creez le fichier :
    
    ```bash
    nano matrix.sh
    ```
    
2. Collez le code dans le fichier.
3. Rendez le script executable :
    
    ```bash
    chmod +x matrix.sh
    ```
    
4. Executez le script :
    
    ```bash
    ./matrix.sh
    ```
    
5. Arretez le script avec `Ctrl + C`.

---

## Exercices sur le Script

### Exercice 1 : Analyse

Expliquez les composants suivants :

- `echo -e "\e[32m"` : active la couleur verte.
- `md5sum` : genere une chaine hexadecimale a partir dun nombre aleatoire.
- `head -c` : extrait un nombre specifique de caracteres.
- `$((RANDOM % 40 + 10))` : genere un nombre aleatoire entre 10 et 49.

### Exercice 2 : Modifications

1. **Changer la couleur** :
    - Vert : `\e[32m`
    - Rouge : `\e[31m`
    - Bleu : `\e[34m`
2. **Modifier la vitesse** :
    - Testez differentes valeurs pour `sleep` (ex. `0.1`, `0.01`).
3. **Changer la longueur des lignes** :
    - Ajustez `RANDOM % 40 + 10` (ex. `RANDOM % 20 + 5`).
