import pytesseract
from PIL import Image
import os

# Caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\deivi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def ler_texto(imagem_path: str, idioma: str = "por") -> str:
    """
    Recebe o caminho de uma imagem e retorna o texto extraído via OCR.
    """
    if not os.path.exists(imagem_path):
        return "Arquivo de imagem não encontrado!"

    try:
        img = Image.open(imagem_path)
        texto = pytesseract.image_to_string(img, lang=idioma)
        return texto.strip()
    except Exception as e:
        return f"Erro no OCR: {str(e)}"
