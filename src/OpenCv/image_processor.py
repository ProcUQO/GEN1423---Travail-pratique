import cv2

def traiter_image(image_path):
    """
    Traite une image en la lisant, en la convertissant en niveaux de gris,
    puis en appliquant un seuillage binaire.
    :param image_path: Chemin de l'image (PNG, JPG...)
    :return: Image après traitement
    """
    try:
        # Lire l'image
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"[Erreur OpenCV] Impossible de charger l'image depuis {image_path}")
            return None

        # Conversion en niveaux de gris
        image_grise = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Appliquer un seuillage binaire
        _, image_seuillee = cv2.threshold(image_grise, 127, 255, cv2.THRESH_BINARY)

        return image_seuillee
    except Exception as e:
        print(f"[Erreur OpenCV] {e}")
        return None
