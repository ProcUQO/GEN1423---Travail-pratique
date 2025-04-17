from src.OpenCv.image_processor import traiter_image  # Traitement d'image avec OpenCV
from src.ocr.ocr_processor import extract_text_from_image  # OCR avec pytesseract
from src.PyMuPDF.analyse_pdf import analyser_pdf  # Extraction de texte et images avec PyMuPDF

import os

def main():
    # Chemin des fichiers
    image_path = 'data/Test Image.png'  # Chemin vers l'image
    pdf_path = 'data/Companies/Extrudex/1/ORDER 10-3-25.pdf'  # Chemin corrigé pour le PDF
    
    # Traitement de l'image avec OpenCV
    print("Traitement de l'image avec OpenCV...")
    image_seuillee = traiter_image(image_path)
    if image_seuillee is not None:
        print("Image traitée avec succès.")
    else:
        print("Erreur lors du traitement de l'image.")

    # Extraction de texte de l'image avec Tesseract OCR
    print("Extraction du texte de l'image avec OCR...")
    texte_image = extract_text_from_image(image_path)
    print("Texte extrait de l'image :\n", texte_image)
    
    # Extraction de texte et d'images du PDF avec PyMuPDF
    print("Analyse du fichier PDF avec PyMuPDF..")
    analyser_pdf(pdf_path)
    
if __name__ == "__main__":
    main()
