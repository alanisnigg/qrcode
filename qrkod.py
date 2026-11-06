import qrcode
from pathlib import Path

data = "https://www.youtube.com/@ewfffy"

img = qrcode.make(data)

dosya_yolu = Path(__file__).resolve().parent / "qrcode.png"

img.save(dosya_yolu)

print("QR kod oluşturuldu!")
print("Dosyanın yeri:", dosya_yolu)