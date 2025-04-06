import os

IMGUR_LINKS_FILE = "imgur_links.txt"
OUTPUT_HTML_FILE = "index.html"

def load_imgur_links():
    if not os.path.exists(IMGUR_LINKS_FILE):
        return []
    with open(IMGUR_LINKS_FILE, "r") as file:
        return [line.strip() for line in file if line.strip()]

def generate_html(links):
    html_head = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Galeri Online Hewan Kamu</title>
    <style>
        body { font-family: sans-serif; background: #f8f8f8; text-align: center; }
        h1 { color: #333; }
        .gallery { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 20px; }
        .gallery img { width: 300px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>Galeri Online Hewan Kamu 🐾</h1>
    <div class="gallery">
"""
    html_body = "\n".join(f'        <img src="{url}" alt="Foto Gabungan (Imgur)">' for url in links)
    html_tail = """
    </div>
</body>
</html>
"""
    return html_head + html_body + html_tail

def save_html(content):
    with open(OUTPUT_HTML_FILE, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    links = load_imgur_links()
    html_content = generate_html(links)
    save_html(html_content)
    print(f"Galeri online diperbarui ({len(links)} gambar) -> {OUTPUT_HTML_FILE}")

if __name__ == "__main__":
    main()
