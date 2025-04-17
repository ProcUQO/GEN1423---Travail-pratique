import fitz
import os
import json
import shutil

# Merci de ne pas renommer le fichier directement "PyMuPDF.py", ça crée un conflit avec le module PyMuPDF (on veut pas ça)

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
            image_filename = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
            image_path = os.path.join(dossier_output, image_filename)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images_info.append({
                "page": page_num + 1,
                "image": image_filename
            })

    doc.close()
    return images_info

# En ce moment ce n'est pas utilisé, mais ça permet de vider le dossier output, si on veut. On peut test en droppant un fichier dans le dossier.
def vider_dossier_test(dossier):
    if os.path.exists(dossier):
        for fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_fichier) or os.path.islink(chemin_fichier):
                os.unlink(chemin_fichier)
            elif os.path.isdir(chemin_fichier):
                shutil.rmtree(chemin_fichier)
    else:
        os.makedirs(dossier)

def analyser_pdf(pdf_path):
    #print(f"Analyse du fichier : {pdf_path}")

    # On définit le répertoire de sortie. Le dossier est temporaire (pour le test), à modifier.
    dossier_output = os.path.join("tests", "extraction_test")
    # vider_dossier_test(dossier_output)

    texte = extraire_texte(pdf_path)
    images = extraire_images(pdf_path, dossier_output)

    resultats = {
        "fichier": os.path.basename(pdf_path),
        "texte": texte,
        "images": images
    }

    return resultats


# Fonction de test. Je le laisse en commentaire comme exemple, fait la même chose que test_extraction. Si ça gosse, on peut le supprimer.
"""
if __name__ == "__main__":
    chemin_pdf = r"PHASE 1 - Travail Pratique - Ingénierie Logicielle.pdf"
    analyser_pdf(chemin_pdf)
"""
    ## a mettre dans le terminal: python -m pip install pymupdf