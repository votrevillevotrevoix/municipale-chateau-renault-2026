# 📰 Guide d'Ajout d'Articles - Section Actualités

## ⏱️ Temps nécessaire : 2 minutes par article

---

## 🚀 Comment ajouter un nouvel article ?

### Étape 1 : Ouvrir le fichier `articles.json`

Le fichier se trouve à la racine du projet : `articles.json`

### Étape 2 : Copier le modèle d'article

**Option 1 : Sans image (rapide)**
```json
  {
    "titre": "Titre de votre article",
    "date": "2026-01-11",
    "source": "Facebook",
    "lien": "https://votre-lien.com"
  },
```

**Option 2 : Avec image (plus visuel)**
```json
  {
    "titre": "Titre de votre article",
    "date": "2026-01-11",
    "source": "Facebook",
    "lien": "https://votre-lien.com",
    "image": "images/nom-de-votre-image.jpg"
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
- **image** : *(Optionnel)* Chemin vers l'image miniature (ex: "images/photo.jpg")

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

Voici un exemple de fichier `articles.json` avec 3 articles (certains avec images, d'autres sans) :

```json
[
  {
    "titre": "Rencontre avec les agriculteurs locaux",
    "date": "2026-01-11",
    "source": "La Nouvelle République",
    "lien": "https://www.lanouvellerepublique.fr",
    "image": "images/rencontre-agriculteurs.jpg"
  },
  {
    "titre": "Notre programme complet est disponible",
    "date": "2026-01-10",
    "source": "Facebook",
    "lien": "https://www.facebook.com/share/p/xxxxx/"
  },
  {
    "titre": "Ouverture de notre local de campagne",
    "date": "2026-01-08",
    "source": "Facebook",
    "lien": "https://www.facebook.com/share/p/yyyyy/",
    "image": "images/Local.jpg"
  }
]
```

💡 **Notez** : Les articles peuvent avoir une image ou non, c'est totalement optionnel !

---

## 📱 Comment récupérer le lien Facebook ?

Sur votre post Facebook :
1. Cliquez sur les **3 points** (...) en haut à droite du post
2. Choisissez **"Copier le lien"**
3. Le lien ressemble à : `https://www.facebook.com/share/p/xxxxx/`
4. **Collez ce lien** dans le champ `"lien"` de votre JSON

⚠️ N'utilisez **PAS** le code d'intégration (iframe), juste l'URL directe.

---

## 🖼️ Comment ajouter une photo miniature ?

### Option 1 : Utiliser une image existante
Si vous avez déjà une image dans le dossier `images/` :
```json
"image": "images/nom-de-votre-image.jpg"
```

### Option 2 : Ajouter une nouvelle image
1. Téléchargez votre photo depuis Facebook ou ailleurs
2. Placez-la dans le dossier `images/` du projet
3. Ajoutez le chemin dans le JSON :
```json
"image": "images/ma-nouvelle-photo.jpg"
```

### Sans image
Si vous n'avez pas d'image, **pas de problème** ! Supprimez simplement la ligne `"image"` :
```json
{
  "titre": "Mon article",
  "date": "2026-01-11",
  "source": "Facebook",
  "lien": "https://..."
}
```

---

## 🎨 Icônes et couleurs automatiques

Le système détecte automatiquement la source :
- **Facebook** : Affiche l'icône Facebook en bleu
- **Autres sources** : Affiche une icône journal en vert

Les images miniatures s'affichent automatiquement en haut de chaque carte (200px de hauteur).

---

## ✅ Checklist avant publication

- [ ] Le fichier `articles.json` est valide (pas d'erreur de syntaxe)
- [ ] Les virgules sont correctement placées
- [ ] La date est au format AAAA-MM-JJ
- [ ] Le lien est complet (commence par https://)
- [ ] Les guillemets sont bien présents autour des valeurs
- [ ] Si vous avez ajouté une image, vérifiez que le fichier existe dans `images/`

---

## 🆘 En cas d'erreur

Si les articles ne s'affichent pas :

1. Vérifiez la console du navigateur (F12)
2. Vérifiez que le fichier `articles.json` est valide (utilisez jsonlint.com)
3. Vérifiez qu'il n'y a pas de virgule en trop ou manquante

---

## 💡 Conseils

**Articles :**
- Ajoutez les articles le matin pour qu'ils soient visibles toute la journée
- Gardez les titres courts et percutants (max 60 caractères)
- Utilisez des dates cohérentes
- Archivez les anciens articles (supprimez-les du fichier) après quelques mois

**Images :**
- Les images rendent les cartes plus attractives (recommandé !)
- Format recommandé : JPG ou PNG
- Taille recommandée : 800x600 pixels minimum
- L'image sera automatiquement redimensionnée à 200px de hauteur
- Nommez vos images de façon descriptive (ex: `rencontre-commercants.jpg`)
- Pour télécharger une image depuis Facebook : clic droit > "Enregistrer l'image sous..."
