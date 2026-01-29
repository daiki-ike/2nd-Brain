import os
import re
from datetime import datetime

# Separator used in My Clippings.txt
CLIPPING_SEPARATOR = "=========="

def parse_clippings(file_path):
    """
    Parses a Kindle 'My Clippings.txt' file.
    Returns a dictionary: { 'Book Title': [ { 'quote': '...', 'metadata': '...' }, ... ] }
    """
    if not os.path.exists(file_path):
        print(f"[Error] File not found: {file_path}")
        return None

    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    # Split by separator
    chunks = content.split(CLIPPING_SEPARATOR)
    books = {}

    for chunk in chunks:
        lines = [L.strip() for L in chunk.split('\n') if L.strip()]
        if len(lines) < 2:
            continue

        # Line 1: Title and Author
        # Example: 銃・病原菌・鉄　上巻 (ジャレド・ダイアモンド)
        title_line = lines[0]
        
        # Line 2: Metadata (Date, location)
        # Example: - Your Highlight on Location 123-125 | Added on Monday...
        meta_line = lines[1]
        
        # Line 3+: Content
        body = "\n".join(lines[2:])

        # Clean title (remove BOM if any, though utf-8-sig handles it)
        title = title_line.strip()

        # Structure the data
        entry = {
            'metadata': meta_line,
            'quote': body,
            'timestamp': extract_date(meta_line) # Optional helper
        }

        if title not in books:
            books[title] = []
        books[title].append(entry)

    print(f"[Parser] Found {len(books)} books in clippings.")
    return books

def extract_date(meta_line):
    # Simple extraction, might vary by locale. 
    # Just returning the raw line for now is safer unless we need strict sorting.
    return meta_line

def save_to_markdown(books, output_dir):
    """
    Saves parsed books to individual Markdown files.
    output_dir: Target directory (e.g. Obsidian Vault)
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    saved_count = 0
    for title, clippings in books.items():
        # Sanitize filename
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
        filename = f"{safe_title}.md"
        filepath = os.path.join(output_dir, filename)

        # Prepare Content
        md_content = f"# {title}\n\n"
        md_content += f"**Imported**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        md_content += f"**Total Highlights**: {len(clippings)}\n\n"
        md_content += "---\n\n"

        for clip in clippings:
            quote = clip['quote']
            # Ignore empty highlights (bookmarks)
            if not quote: 
                continue
                
            md_content += f"> {quote}\n\n"
            md_content += f"*{clip['metadata']}*\n\n"
            md_content += "---\n\n"

        # Save
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)
            saved_count += 1
            print(f"[Saved] {filename}")
        except Exception as e:
            print(f"[Error] Failed to save {filename}: {e}")

    return saved_count
