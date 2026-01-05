# 🚀 Guide de Mise en Ligne du Site
## votrevillevotrevoix37.fr

---

## 📅 **OBJECTIF : Site en ligne le 10 janvier 2026 à 10h00**

---

## ÉTAPE 1 : Vérifier la disponibilité du domaine

### À faire MAINTENANT :

1. Allez sur : **https://www.ovhcloud.com/fr/domains/**
2. Dans la barre de recherche, tapez : `votrevillevotrevoix37`
3. Vérifiez si le **.fr** est disponible (pastille verte)
4. Si disponible, passez à l'étape 2
5. Si non disponible, essayez : `votrevillevotrevoix37.com`

---

## ÉTAPE 2 : Acheter le domaine (1 an)

### Chez OVH (Recommandé - environ 6-8€/an) :

1. Sur la page de résultats, cliquez sur **votrevillevotrevoix37.fr**
2. Cliquez sur **Commander** (ou "Ajouter au panier")
3. **IMPORTANT** : Sélectionnez **1 an** uniquement
4. Options à décocher :
   - ❌ Hébergement web (pas nécessaire avec GitHub Pages)
   - ❌ SSL (GitHub Pages le fournit gratuitement)
   - ❌ Emails (sauf si vous en voulez)
5. Créez un compte OVH ou connectez-vous
6. Complétez le paiement

### Informations importantes à fournir :
- **Titulaire** : Nom de la liste "Votre Ville, Votre Voix"
- **Contact administratif** : Vos coordonnées
- **Adresse** : Château-Renault, 37110, France

⏱️ **Délai** : Le domaine est actif immédiatement après paiement

---

## ÉTAPE 3 : Configurer le DNS chez OVH

### À faire 10-15 minutes après l'achat :

1. Connectez-vous à votre **Espace Client OVH**
2. Allez dans : **Web Cloud** → **Noms de domaine**
3. Cliquez sur **votrevillevotrevoix37.fr**
4. Cliquez sur l'onglet **Zone DNS**

### Modifier la Zone DNS :

#### A. Supprimer les enregistrements par défaut :
- Cliquez sur l'icône 🗑️ à côté des enregistrements A existants
- Supprimez tous les A qui pointent vers des IP OVH

#### B. Ajouter les 4 enregistrements A de GitHub :

Cliquez sur **Ajouter une entrée** → **A**

**Enregistrement 1 :**
- Sous-domaine : (laissez vide ou mettez un point `.`)
- TTL : 3600
- Cible : `185.199.108.153`

**Enregistrement 2 :**
- Sous-domaine : (laissez vide ou mettez un point `.`)
- TTL : 3600
- Cible : `185.199.109.153`

**Enregistrement 3 :**
- Sous-domaine : (laissez vide ou mettez un point `.`)
- TTL : 3600
- Cible : `185.199.110.153`

**Enregistrement 4 :**
- Sous-domaine : (laissez vide ou mettez un point `.`)
- TTL : 3600
- Cible : `185.199.111.153`

#### C. Ajouter l'enregistrement CNAME pour www :

Cliquez sur **Ajouter une entrée** → **CNAME**

- Sous-domaine : `www`
- TTL : 3600
- Cible : `votrevillevotrevoix.github.io.`

⚠️ **IMPORTANT** : N'oubliez pas le **point final** après `.io.`

#### D. Valider les modifications :
- Cliquez sur **Valider**
- Patientez **24-48 heures** pour la propagation DNS complète

---

## ÉTAPE 4 : Fusionner les branches sur GitHub

### À faire sur GitHub.com :

1. Allez sur : **https://github.com/votrevillevotrevoix/municipale-chateau-renault-2026**

2. Cliquez sur **Pull requests** → **New pull request**

3. **Pull Request 1** - Corrections CSS :
   - Base : `main` (ou votre branche principale)
   - Compare : `claude/single-line-vote-text-8kkwh`
   - Titre : "Corrections CSS pour mentions légales et politique de confidentialité"
   - Cliquez sur **Create pull request**
   - Puis **Merge pull request** → **Confirm merge**

4. **Pull Request 2** - Formulaire et domaine :
   - Base : `main`
   - Compare : `claude/verify-html-site-8kkwh`
   - Titre : "Configuration formulaire de contact et domaine personnalisé"
   - Cliquez sur **Create pull request**
   - Puis **Merge pull request** → **Confirm merge**

---

## ÉTAPE 5 : Activer GitHub Pages

### Configuration initiale :

1. Sur GitHub, allez dans : **Settings** (⚙️)
2. Dans le menu de gauche : **Pages**
3. Configuration :
   - **Source** : Deploy from a branch
   - **Branch** : `main` (ou master) - Dossier : `/ (root)`
   - Cliquez sur **Save**

⏱️ **Attendez 2-3 minutes**, la page va se rafraîchir

### Après 24-48h de propagation DNS :

4. Retournez dans **Settings** → **Pages**
5. Dans **Custom domain**, le domaine `votrevillevotrevoix37.fr` devrait déjà apparaître (grâce au fichier CNAME)
6. Cochez ✅ **Enforce HTTPS**
7. Cliquez sur **Save**

Votre site sera accessible sur : **https://votrevillevotrevoix37.fr**

---

## ÉTAPE 6 : Publication le 10 janvier à 10h00

### Option A - Dépôt privé (RECOMMANDÉ) :

**Maintenant :**
- Le dépôt reste **privé** sur GitHub
- Tout est configuré mais le site n'est pas accessible au public

**Le 10 janvier 2026 à 10h00 :**
1. Allez dans **Settings** → Scroll tout en bas
2. Section **Danger Zone** → **Change repository visibility**
3. Cliquez sur **Change visibility** → **Make public**
4. Tapez le nom du dépôt pour confirmer
5. Cliquez sur **I understand, change repository visibility**

✅ **Le site sera en ligne immédiatement !**

---

### Option B - Page temporaire "Coming Soon" :

Si vous préférez avoir le dépôt public dès maintenant :

1. Je crée une page temporaire "Site en ligne le 10 janvier"
2. Le 10 janvier à 10h00, vous remplacez par le vrai contenu

**Dites-moi si vous préférez cette option**

---

## ✅ CHECKLIST FINALE

Avant le 10 janvier :
- [ ] Domaine acheté et payé
- [ ] DNS configuré (4 enregistrements A + 1 CNAME)
- [ ] Attendre 24-48h pour propagation DNS
- [ ] Branches fusionnées sur GitHub
- [ ] GitHub Pages activé
- [ ] HTTPS activé (après propagation DNS)
- [ ] Formulaire de contact testé (activation FormSubmit)

Le 10 janvier à 10h00 :
- [ ] Rendre le dépôt public (Settings → Change visibility)
- [ ] Vérifier que le site est accessible
- [ ] Tester le formulaire de contact

---

## 📞 SUPPORT

- **OVH Support** : https://www.ovhcloud.com/fr/support/
- **GitHub Support** : https://support.github.com/

---

## 🎯 ESTIMATION DES DÉLAIS

| Étape | Temps requis |
|-------|-------------|
| Achat domaine | 10-15 min |
| Configuration DNS | 10 min |
| Propagation DNS | 24-48h |
| Fusion branches GitHub | 5 min |
| Activation GitHub Pages | 5 min |
| Activation HTTPS | Après propagation DNS |

**TOTAL** : Commencez 48h avant la date de publication (soit le 8 janvier)

---

## ❓ Questions fréquentes

**Q : Le domaine sera-t-il actif immédiatement ?**
R : Le domaine est actif après paiement, mais le DNS prend 24-48h pour se propager.

**Q : Puis-je tester le site avant le 10 janvier ?**
R : Oui, via l'URL GitHub : votrevillevotrevoix.github.io/municipale-chateau-renault-2026

**Q : Que se passe-t-il si le .fr n'est pas disponible ?**
R : Essayez .com ou contactez-moi pour changer le fichier CNAME.

**Q : Le formulaire de contact fonctionnera-t-il tout de suite ?**
R : FormSubmit nécessite une activation au premier envoi (cliquer sur le lien de confirmation).

---

**Bonne chance pour votre campagne ! 🎉**
