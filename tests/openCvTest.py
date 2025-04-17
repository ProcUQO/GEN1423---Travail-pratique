# tests/openCvTest.py
import unittest
import os
from src.OpenCv.image_processor import traiter_image

class TestTraitementImage(unittest.TestCase):
    def test_traitement_image(self):
        # Définir le chemin de l'image
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, '..', 'data', 'Test Image.png')  # Chemin relatif vers l'image
        
        # Tester la fonction de traitement d'image
        image_seuillee = traiter_image(image_path)
        self.assertIsNotNone(image_seuillee)  # Vérifie que l'image a été traitée

if __name__ == "__main__":
    unittest.main()
