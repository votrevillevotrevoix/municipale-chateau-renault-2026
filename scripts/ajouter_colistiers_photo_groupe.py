#!/usr/bin/env python3
"""
Script pour incruster les photos des trois colistiers manquants sur la photo de groupe.
Les trois portraits seront positionnés derrière la dernière rangée.
"""

from PIL import Image, ImageDraw, ImageFilter
import os

def creer_photo_composite():
    """
    Crée une photo composite en ajoutant les trois portraits individuels
    sur la photo de groupe, positionnés derrière la dernière rangée.
    """

    # Chemins des images
    photo_groupe = "images/Groupe original.jpg"
    portrait1 = "images/candidats/6 - Michael Boudmer.jpg"
    portrait2 = "images/candidats/10 - Jacky Tarenne.jpg"
    portrait3 = "images/candidats/17 - Claire Guery-Pottier.jpg"
    output_path = "images/Groupe original.jpg"  # Remplace la photo originale

    # Vérifier que tous les fichiers existent
    fichiers = [photo_groupe, portrait1, portrait2, portrait3]
    for fichier in fichiers:
        if not os.path.exists(fichier):
            print(f"ERREUR: Le fichier {fichier} n'existe pas.")
            print(f"Veuillez placer les images aux bons emplacements.")
            return

    # Charger la photo de groupe
    print(f"Chargement de la photo de groupe: {photo_groupe}")
    groupe = Image.open(photo_groupe)
    largeur_groupe, hauteur_groupe = groupe.size

    # Charger les trois portraits
    print(f"Chargement des portraits individuels...")
    portraits = [
        Image.open(portrait1),
        Image.open(portrait2),
        Image.open(portrait3)
    ]

    # Définir la taille cible pour les portraits (proportionnelle à la photo de groupe)
    # On va redimensionner les portraits pour qu'ils aient une hauteur d'environ 20% de la photo de groupe
    hauteur_portrait_cible = int(hauteur_groupe * 0.20)

    # Redimensionner les portraits en gardant le ratio
    portraits_redimensionnes = []
    for i, portrait in enumerate(portraits):
        largeur_portrait, hauteur_portrait = portrait.size
        ratio = hauteur_portrait_cible / hauteur_portrait
        nouvelle_largeur = int(largeur_portrait * ratio)
        portrait_redim = portrait.resize((nouvelle_largeur, hauteur_portrait_cible), Image.Resampling.LANCZOS)
        portraits_redimensionnes.append(portrait_redim)
        print(f"  Portrait {i+1}: {largeur_portrait}x{hauteur_portrait} -> {nouvelle_largeur}x{hauteur_portrait_cible}")

    # Créer une nouvelle image avec plus d'espace en bas pour les portraits
    espace_supplementaire = hauteur_portrait_cible + 20  # 20px de marge
    nouvelle_hauteur = hauteur_groupe + espace_supplementaire

    # Créer l'image composite avec un fond qui match la photo de groupe
    composite = Image.new('RGB', (largeur_groupe, nouvelle_hauteur), (200, 200, 200))

    # Coller la photo de groupe originale en haut
    composite.paste(groupe, (0, 0))

    # Calculer les positions pour les trois portraits (centrés horizontalement)
    largeur_totale_portraits = sum(p.width for p in portraits_redimensionnes) + 40  # 20px d'espace entre chaque
    x_depart = (largeur_groupe - largeur_totale_portraits) // 2
    y_position = hauteur_groupe + 10  # 10px sous la photo de groupe

    # Coller les trois portraits
    x_courant = x_depart
    for i, portrait in enumerate(portraits_redimensionnes):
        composite.paste(portrait, (x_courant, y_position))
        x_courant += portrait.width + 20  # Espace entre les portraits
        print(f"  Portrait {i+1} positionné à x={x_courant - portrait.width - 20}, y={y_position}")

    # Sauvegarder le résultat
    print(f"Sauvegarde de la photo composite: {output_path}")
    composite.save(output_path, quality=95, optimize=True)
    print(f"✓ Photo composite créée avec succès!")
    print(f"  Dimensions: {largeur_groupe}x{nouvelle_hauteur}")
    print(f"  Fichier: {output_path}")

def creer_photo_incrustee():
    """
    Version alternative: incruste les portraits directement sur la photo de groupe
    en les positionnant comme une rangée supplémentaire derrière les autres.
    """

    # Chemins des images
    photo_groupe = "images/Groupe original.jpg"
    portrait1 = "images/candidats/6 - Michael Boudmer.jpg"
    portrait2 = "images/candidats/10 - Jacky Tarenne.jpg"
    portrait3 = "images/candidats/17 - Claire Guery-Pottier.jpg"
    output_path = "images/Groupe original - avec colistiers.jpg"

    # Vérifier que tous les fichiers existent
    fichiers = [photo_groupe, portrait1, portrait2, portrait3]
    for fichier in fichiers:
        if not os.path.exists(fichier):
            print(f"ERREUR: Le fichier {fichier} n'existe pas.")
            print(f"Veuillez placer les images aux bons emplacements.")
            return

    # Charger la photo de groupe
    print(f"Chargement de la photo de groupe: {photo_groupe}")
    groupe = Image.open(photo_groupe).convert('RGB')
    largeur_groupe, hauteur_groupe = groupe.size

    # Charger les trois portraits
    print(f"Chargement des portraits individuels...")
    portraits = [
        Image.open(portrait1).convert('RGB'),
        Image.open(portrait2).convert('RGB'),
        Image.open(portrait3).convert('RGB')
    ]

    # Taille des portraits (à ajuster selon la perspective de la photo)
    # Même taille que les personnes du dernier rang pour une intégration naturelle
    hauteur_portrait_cible = int(hauteur_groupe * 0.12)  # 12% de la hauteur (taille des personnes du dernier rang)

    # Redimensionner les portraits
    portraits_redimensionnes = []
    for i, portrait in enumerate(portraits):
        largeur_portrait, hauteur_portrait = portrait.size
        ratio = hauteur_portrait_cible / hauteur_portrait
        nouvelle_largeur = int(largeur_portrait * ratio)
        portrait_redim = portrait.resize((nouvelle_largeur, hauteur_portrait_cible), Image.Resampling.LANCZOS)
        portraits_redimensionnes.append(portrait_redim)
        print(f"  Portrait {i+1}: {largeur_portrait}x{hauteur_portrait} -> {nouvelle_largeur}x{hauteur_portrait_cible}")

    # Créer une copie de la photo de groupe pour y incruster les portraits
    composite = groupe.copy()

    # Position où incruster les portraits (au même niveau que le dernier rang du bas)
    # Les placer à la même hauteur que les personnes du dernier rang
    y_position = int(hauteur_groupe * 0.50)  # 50% depuis le haut (même hauteur que le dernier rang)

    # Positions X spécifiques dans les espaces vides (sans personne)
    # Ajustées pour remplir les espaces vides du dernier rang
    positions_x = [
        int(largeur_groupe * 0.15),  # Portrait 1 - espace vide à gauche
        int(largeur_groupe * 0.42),  # Portrait 2 - espace vide au centre
        int(largeur_groupe * 0.78)   # Portrait 3 - espace vide à droite
    ]

    # Coller les portraits avec détourage automatique
    for i, portrait in enumerate(portraits_redimensionnes):
        # Détourer automatiquement le portrait en détectant le fond
        portrait_rgba = portrait.convert('RGBA')
        pixels = portrait_rgba.load()

        # Détecter la couleur du fond (coin supérieur gauche généralement)
        bg_color = portrait.getpixel((10, 10))
        threshold = 40  # Tolérance pour la détection du fond

        # Créer un masque basé sur la différence avec la couleur de fond
        mask = Image.new('L', (portrait.width, portrait.height), 0)
        mask_pixels = mask.load()

        for y in range(portrait.height):
            for x in range(portrait.width):
                pixel = portrait.getpixel((x, y))
                # Calculer la différence avec la couleur de fond
                diff = sum(abs(pixel[c] - bg_color[c]) for c in range(3))

                if diff > threshold:
                    # C'est le sujet, pas le fond
                    mask_pixels[x, y] = 255
                else:
                    # C'est le fond, rendre transparent
                    mask_pixels[x, y] = 0

        # Appliquer une érosion puis une dilatation pour nettoyer le masque
        mask = mask.filter(ImageFilter.MinFilter(3))  # Érosion
        mask = mask.filter(ImageFilter.MaxFilter(3))  # Dilatation

        # Appliquer un flou gaussien pour adoucir les bords
        mask = mask.filter(ImageFilter.GaussianBlur(5))

        # Coller le portrait avec le masque à la position définie
        x_position = positions_x[i]
        composite.paste(portrait, (x_position, y_position), mask)
        print(f"  Portrait {i+1} incrusté à x={x_position}, y={y_position}")

    # Sauvegarder le résultat
    print(f"Sauvegarde de la photo composite: {output_path}")
    composite.save(output_path, quality=95, optimize=True)
    print(f"✓ Photo composite créée avec succès!")
    print(f"  Dimensions: {largeur_groupe}x{hauteur_groupe}")
    print(f"  Fichier: {output_path}")

if __name__ == "__main__":
    print("=== Création de la photo de groupe complète ===\n")
    print("Deux options disponibles:")
    print("1. creer_photo_composite() - Ajoute les portraits en bas de la photo")
    print("2. creer_photo_incrustee() - Incruste les portraits sur la photo\n")

    # Utiliser la version incrustée par défaut
    creer_photo_incrustee()
