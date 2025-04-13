import os
import sys
import importlib.util

# Chemin vers le fichier PDF à analyser
chemin_pdf = r"PHASE 1 - Travail Pratique - Ingénierie Logicielle.pdf"

# Chemin vers le script analyse_pdf.py
chemin_script = os.path.join("src", "PyMuPDF", "analyse_pdf.py")

# Charger le module analyse_pdf dynamiquement
spec = importlib.util.spec_from_file_location("analyse_pdf", chemin_script)
analyse_pdf = importlib.util.module_from_spec(spec)
sys.modules["analyse_pdf"] = analyse_pdf
spec.loader.exec_module(analyse_pdf)

# Appeler la fonction analyser_pdf avec le chemin du fichier PDF
analyse_pdf.analyser_pdf(chemin_pdf)
