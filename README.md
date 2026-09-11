# TalosInfoTek

Site francophone de tutoriels techniques et de documentation autour de Linux, des réseaux et de l’informatique.

Le site utilise [Hugo](https://gohugo.io/) et le thème [Blowfish](https://blowfish.page/).

## Développement local

Hugo Extended 0.162.0 à 0.165.x est nécessaire pour la version de Blowfish actuellement épinglée.

```shell
git clone --recurse-submodules https://github.com/3ktone/3ktone.github.io.git
cd 3ktone.github.io
hugo server --buildDrafts
```

Le site local est ensuite accessible à l’adresse indiquée par Hugo, généralement `http://localhost:1313/`.

## Ajouter une page

La documentation est organisée sous `content/docs/` et les guides pratiques sous `content/tutoriels/`. Chaque article utilise un *leaf bundle* :

```text
content/docs/linux/mon-sujet/
├── index.md
├── capture-1.png
└── capture-2.png
```

Créez la page, vérifiez-la localement, puis publiez-la :

```shell
git add content/
git commit -m "docs: ajouter mon sujet"
git pull --rebase origin main
git push origin main
```

Chaque envoi sur `main` déclenche automatiquement la construction et le déploiement sur GitHub Pages.

## Mise à jour du thème

Blowfish est enregistré comme sous-module Git et épinglé à une version testée. Pour choisir explicitement une nouvelle version :

```shell
git -C themes/blowfish fetch --tags
git -C themes/blowfish checkout vX.Y.Z
git add themes/blowfish
git commit -m "chore: mettre à jour Blowfish vers vX.Y.Z"
```

## Licence

Le contenu et le code de ce dépôt sont publiés sous la licence indiquée dans [LICENSE](LICENSE).
