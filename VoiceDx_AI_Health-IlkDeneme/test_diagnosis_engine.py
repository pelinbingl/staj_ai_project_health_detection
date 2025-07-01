import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from diagnosis_engine import DiagnosisEngine
from pdf_parser import PDFParser  # EKLENDİ

# Semptomlar: sesli ifade sonucu
semptomlar = ["baş dönmesi", "göğüs ağrısı"]

# PDF'ten tahlil verilerini çek
parser = PDFParser()
tahliller = parser.parse("C:\\Users\\Pelin\\Downloads\\Enabiz-Tahlilleri.pdf")  # gerçek PDF buraya!

# Teşhis motorunu başlat
motor = DiagnosisEngine()
yorumlar = motor.evaluate(semptomlar, tahliller)

# Sonuçları yazdır
print("Teşhis Motoru Yorumları:")
for y in yorumlar:
    print("-", y)
