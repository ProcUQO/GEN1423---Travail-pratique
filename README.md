# GEN1423---Travail-pratique
Il est important d'installer les modules.

# Installer PyMuPDF, OpenCV, Tesseract et Pytesseract
py -m pip install -r requirements.txt
Lien pour installer Tesseract : https://github.com/UB-Mannheim/tesseract/wiki 

# Pour run/tester OpenCV 
python tests/openCvTest.py

# Pour run/tester Pytesseract (conversion image vers text)
tests/test_ocr.py

# Pour run/tester PyMuPDF (extraire images et texte)
tests\test_extraction.py
