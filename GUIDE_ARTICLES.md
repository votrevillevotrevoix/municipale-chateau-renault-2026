# 📰 Guide d'Ajout d'Articles - Section Actualités

## ⏱️ Temps nécessaire : 2 minutes par article

---

## 🚀 Comment ajouter un nouvel article ?

### Étape 1 : Ouvrir le fichier `articles.json`

Le fichier se trouve à la racine du projet : `articles.json`

### Étape 2 : Copier le modèle d'article

Copiez ce bloc de code :

```json
  {
    "titre": "Titre de votre article",
    "date": "2026-01-11",
    "source": "Facebook",
    "lien": "https://votre-lien.com"
  },
```

### Étape 3 : Insérer l'article en haut de la liste

**IMPORTANT** : Ajoutez toujours les nouveaux articles **EN HAUT** de la liste, juste après le crochet `[`

Exemple :

```json
[
  {
    "titre": "NOUVEL ARTICLE ICI",
    "date": "2026-01-11",
    "source": "Facebook",
    "lien": "https://..."
  },
  {
    "titre": "Ouverture de notre local de campagne",
    "date": "2026-01-08",
    "source": "Facebook",
    "lien": "https://www.facebook.com/profile.php?id=61584724443873"
  },
  ...
]
```

### Étape 4 : Remplir les informations

- **titre** : Le titre de votre article (entre guillemets)
- **date** : Format AAAA-MM-JJ (exemple : 2026-01-11 pour le 11 janvier 2026)
- **source** : Le nom de la source (Facebook, La Nouvelle République, etc.)
- **lien** : L'URL complète de l'article (entre guillemets)

### Étape 5 : Vérifier la virgule

⚠️ **IMPORTANT** :
- Mettez une **virgule** à la fin du bloc `}` SAUF pour le dernier article de la liste
- Le dernier article ne doit PAS avoir de virgule

### Étape 6 : Sauvegarder et publier

1. Sauvegardez le fichier `articles.json`
2. Poussez les modifications sur GitHub
3. Les articles s'afficheront automatiquement sur le site

---

## 📝 Exemple complet

Voici un exemple de fichier `articles.json` avec 3 articles :

```json
[
  {
    "titre": "Rencontre avec les agriculteurs locaux",
    "date": "2026-01-11",
    "source": "La Nouvelle République",
    "lien": "https://www.lanouvellerepublique.fr"
  },
  {
    "titre": "Notre programme complet est disponible",
    "date": "2026-01-10",
    "source": "Facebook",
    "lien": "https://www.facebook.com/profile.php?id=61584724443873"
  },
  {
    "titre": "Ouverture de notre local de campagne",
    "date": "2026-01-08",
    "source": "Facebook",
    "lien": "https://www.facebook.com/profile.php?id=61584724443873"
  }
]
```

---

## 🎨 Icônes et couleurs automatiques

Le système détecte automatiquement la source :
- **Facebook** : Affiche l'icône Facebook en bleu
- **Autres sources** : Affiche une icône journal en vert

---

## ✅ Checklist avant publication

- [ ] Le fichier `articles.json` est valide (pas d'erreur de syntaxe)
- [ ] Les virgules sont correctement placées
- [ ] La date est au format AAAA-MM-JJ
- [ ] Le lien est complet (commence par https://)
- [ ] Les guillemets sont bien présents autour des valeurs

---

## 🆘 En cas d'erreur

Si les articles ne s'affichent pas :

1. Vérifiez la console du navigateur (F12)
2. Vérifiez que le fichier `articles.json` est valide (utilisez jsonlint.com)
3. Vérifiez qu'il n'y a pas de virgule en trop ou manquante

---

## 💡 Conseils

- Ajoutez les articles le matin pour qu'ils soient visibles toute la journée
- Gardez les titres courts et percutants
- Utilisez des dates cohérentes
- Archivez les anciens articles (supprimez-les du fichier) après quelques mois
