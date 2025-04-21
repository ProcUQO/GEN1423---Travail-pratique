from image_processor import traiter_image  # Traitement d'image avec OpenCV
from ocr_processor import extract_text_from_image  # OCR avec pytesseract
from analyse_pdf import analyser_pdf  # Extraction de texte et images avec PyMuPDF
from utils import split_path, recursive_mkdir, vider_dossier

import json
import os

def testImage():
    image_path = '../data/Test Image.png'  # Chemin vers l'image
    
    # Traitement de l'image avec OpenCV
    print("Traitement de l'image avec OpenCV...")
    image_seuillee = traiter_image(image_path)
    if image_seuillee is not None:
        print("Image traitée avec succès.")
    else:
        print("Erreur lors du traitement de l'image.")
    
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

OUTPUT_BASE_PATH = os.path.join("..", "tests", "extraction_test")

def main():
    # Chemin des fichiers
    pdf_path = input("Chemin du fichier PDF à traiter: ")
    output_path = os.path.join(OUTPUT_BASE_PATH, *(split_path(pdf_path)[1:]))

    recursive_mkdir(output_path)
    vider_dossier(output_path)

    print("Analyse du fichier PDF..")
    results = analyser_pdf(pdf_path, output_path)
    for image in results["images"]:
        image["text"] = extract_text_from_image(os.path.join(output_path, image["image"]))

    with open(os.path.join(output_path, 'index.json'), 'w') as f:
        json.dump(results, f)
    
if __name__ == "__main__":
    main()
