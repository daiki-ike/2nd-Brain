import os

# Tesseract Path (Update this if Tesseract is installed in a different location)
# Common paths:
# C:\Program Files\Tesseract-OCR\tesseract.exe
# C:\Program Files (x86)\Tesseract-OCR\tesseract.exe
TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Output Directory
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')

# Delays (Seconds) - random variance will be added
PAGE_TURN_DELAY = 1.0
CAPTURE_DELAY = 0.5
