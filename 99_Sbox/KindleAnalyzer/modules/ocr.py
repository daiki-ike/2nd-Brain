import pytesseract
from PIL import Image
import os
import sys

# Add parent dir to sys.path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def init_tesseract():
    """
    Initialize Tesseract path from config.
    Returns True if exists, False otherwise.
    """
    if os.path.exists(config.TESSERACT_CMD):
        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_CMD
        return True
    else:
        print(f"[Warning] Tesseract not found at: {config.TESSERACT_CMD}")
        print("Please install Tesseract-OCR and update config.py")
        return False

def image_to_text(image_path_or_obj, lang='jpn'):
    """
    Converts image to text.
    image_path_or_obj: file path str or PIL Image object
    lang: 'jpn', 'eng', or 'jpn+eng'
    """
    try:
        if not init_tesseract():
            return "[Error: Tesseract not configured]"
            
        text = pytesseract.image_to_string(image_path_or_obj, lang=lang)
        return text
    except Exception as e:
        return f"[OCR Error] {e}"
