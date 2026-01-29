import sys
import os
import time
from datetime import datetime

# Add modules to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
import capture
import navigation
import ocr
import clippings  # New module
import config

def run_screen_analysis():
    """Logic for the original OCR analysis"""
    # 1. Check Dependencies
    if not ocr.init_tesseract():
        print("[CRITICAL] Tesseract is not configured correctly.")
        print(f"Please install it and check {config.config_file} (conceptual path)") 
        return
        
    # 2. Select Region
    print("\n[Step 1] Define the Capture Region.")
    region = capture.select_region()
    if not region:
        print("Region selection cancelled.")
        return

    # 3. Setup Session
    try:
        pages_input = input("\n[Step 2] How many pages to process? (Default: 1): ")
        total_pages = int(pages_input) if pages_input.strip() else 1
    except ValueError:
        total_pages = 1
        
    print(f"\n[Ready] Starting process for {total_pages} pages.")
    print("Switch focus to Kindle window immediately!")
    print("Process will start in 5 seconds...")
    time.sleep(5)
    
    # 4. Main Loop
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(config.OUTPUT_DIR, timestamp)
    os.makedirs(session_dir, exist_ok=True)
    
    print(f"\n[Start] Saving to: {session_dir}")
    
    try:
        for i in range(1, total_pages + 1):
            print(f"\n--- Page {i}/{total_pages} ---")
            
            # A. Capture
            img_filename = f"page_{i:03d}.png"
            img_path = os.path.join(session_dir, img_filename)
            screenshot = capture.capture_region(region, output_path=img_path)
            
            # B. OCR
            if screenshot:
                text_filename = f"page_{i:03d}.txt"
                text_path = os.path.join(session_dir, text_filename)
                
                print("[OCR] Analyzing text...")
                text = ocr.image_to_text(screenshot, lang='jpn')
                
                with open(text_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"[OCR] Text saved to {text_path}")
            
            # C. Next Page (if not last)
            if i < total_pages:
                navigation.turn_next_page()
                navigation.wait_human_like(base_delay=config.PAGE_TURN_DELAY)
                
    except KeyboardInterrupt:
        print("\n[Stop] Process interrupted by user.")
    except Exception as e:
        print(f"\n[Error] Unexpected error: {e}")

def run_highlight_import():
    """Logic for importing My Clippings.txt"""
    print("\n--- Import Kindle Highlights ---")
    print("1. Connect your Kindle Paperwhite to PC via USB.")
    print("2. Verify the drive letter (e.g. D:, E:).")
    print("3. Or copy 'My Clippings.txt' to this folder.")
    
    default_path = "My Clippings.txt"
    input_path = input(f"\nEnter path to 'My Clippings.txt' [Default: {default_path}]: ").strip()
    if not input_path:
        input_path = default_path
        
    # Remove quotes if user dragged and dropped
    input_path = input_path.replace('"', '')

    if not os.path.exists(input_path):
        print(f"[Error] File not found: {input_path}")
        return

    # Parse
    print("Parsing...")
    books = clippings.parse_clippings(input_path)
    
    if not books:
        print("No highlights found or parsing failed.")
        return

    # Save
    # Target: c:\Users\daiki\Product\2nd-Brain\2nd-Brain\03_知識ベース\Source\Kindle
    # Construct absolute path for safety
    base_knowledge_dir = r"c:\Users\daiki\Product\2nd-Brain\2nd-Brain\03_知識ベース\Source\Kindle"
    output_dir = input(f"Save directory [Default: {base_knowledge_dir}]: ").strip()
    if not output_dir:
        output_dir = base_knowledge_dir
        
    print(f"Saving to: {output_dir}")
    count = clippings.save_to_markdown(books, output_dir)
    print(f"\n[Success] Imported {count} books to Obsidian.")


def main():
    print("========================================")
    print("   Kindle Analysis & Integration Tool")
    print("========================================")
    print("1. [PC] Screen Analysis (OCR)")
    print("2. [Paperwhite] Import Highlights (My Clippings.txt)")
    
    choice = input("\nSelect mode (1/2): ").strip()
    
    if choice == '1':
        run_screen_analysis()
    elif choice == '2':
        run_highlight_import()
    else:
        print("Invalid selection.")

    print("\n========================================")
    print("   Session Complete")
    print("========================================")


if __name__ == "__main__":
    main()
