#stage 2 steganography encoder - build by Ambegoda L.D.S.P (IT24103839)
from PIL import Image

msg = "AEGIS{pixel_whispers_found} PORTAL:http://localhost:8083/login.php"
bits = ''.join(f'{ord(c):08b}' for c in msg) + '00000000'  # null terminator

img = Image.open("employee_of_the_month.png").convert("RGB")
pixels = img.load()
w, h = img.size
idx = 0
for y in range(h):
    for x in range(w):
        if idx >= len(bits):
            break
        r, g, b = pixels[x, y]
        b = (b & ~1) | int(bits[idx])
        pixels[x, y] = (r, g, b)
        idx += 1
    if idx >= len(bits):
        break
img.save("employee_of_the_month.png")
print("Embedded", len(msg), "chars")
