# pour tester ocr_processor.py. Le texte va apparaître dans la console.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ocr.ocr_processor import extract_text_from_image

# il faut que l'image soit dans le dossier data pour le test.
if __name__ == "__main__":
    image_path = os.path.join("data", "Test Image.png")
    text = extract_text_from_image(image_path)
    print("Texte extrait :\n", text)
