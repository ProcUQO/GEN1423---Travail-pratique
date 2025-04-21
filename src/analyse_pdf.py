import fitz
import os
from utils import random_str

def extraire_texte(pdf_path):
    texte_total = []
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):
        texte = page.get_text()
        texte_total.append({
            "page": page_num + 1,
            "texte": texte
        })

    doc.close()
    return texte_total

def extraire_images(pdf_path, dossier_output):
    if not os.path.exists(dossier_output):
        os.makedirs(dossier_output)

    doc = fitz.open(pdf_path)
    images_info = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"{random_str(15)}.{image_ext}"
            image_path = os.path.join(dossier_output, image_filename)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images_info.append({
                "page": page_num + 1,
                "image": image_filename
            })

    doc.close()
    return images_info

def analyser_pdf(pdf_path, output_path):
    texte = extraire_texte(pdf_path)
    images = extraire_images(pdf_path, output_path)

    resultats = {
        "fichier": os.path.basename(pdf_path),
        "texte": texte,
        "images": images
    }

    return resultats
