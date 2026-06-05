from PIL import Image
import os

icons = [
    'logo/icones/code-icon.png',
    'logo/icones/money-icon.png',
    'logo/icones/speech-icone.png',
    'logo/icones/english-icon.png'
]

for icon in icons:
    path = f'e:/Clientes/Happy/happy/{icon}'
    if os.path.exists(path):
        img = Image.open(path)
        img = img.convert("RGBA")
        bbox = img.getbbox()
        width, height = img.size
        print(f"{icon}: size={width}x{height}, bbox={bbox}")
    else:
        print(f"File not found: {path}")
