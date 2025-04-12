from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# tests/test_ocr.py pour tester cette fonctionnalité. Quand PyMuPDF sera installé, on pourra traiter les images qu'on extrait des PDFs. 
# Lien pour installer Tesseract : https://github.com/UB-Mannheim/tesseract/wiki , bien installer dans le path
# Pour installer pytesseract : pip install pytesseract

def extract_text_from_image(image_path):
    """
    Extrait le texte d'une image en utilisant Tesseract OCR.
    :param image_path: Chemin de l'image (PNG, JPG...)
    :return: Texte extrait
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')  # 'fra' pour français
        return text
    except Exception as e:
        print(f"[Erreur OCR] {e}")
        return ""


from src.ocr.ocr_processor import extract_text_from_image

"""
if __name__ == "__main__":
    text = extract_text_from_image("data/example_image.png")
    print("Texte extrait :\n", text)
"""
