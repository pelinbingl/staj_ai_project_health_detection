import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from report_generator import ReportGenerator
from pdf_parser import PDFParser
from symptom_classifier import SymptomClassifier
from diagnosis_engine import DiagnosisEngine  # ✅ EKLENDİ

# 🎤 Kullanıcının konuşması yazıya dökülmüş hali
metin = "Son birkaç gündür başım dönüyor ve göğsümde ağrı hissediyorum."

# 🧠 Semptom çıkarımı
classifier = SymptomClassifier()
semptomlar = classifier.classify(metin)

# 📄 Tahlil verisi PDF'ten
parser = PDFParser()
tahliller = parser.parse("ornek_tahlil.pdf")

# 🧠 Teşhis motorunu kullanarak yorum üret
motor = DiagnosisEngine()
yorumlar = motor.evaluate(semptomlar, tahliller)

# 📑 Raporu oluştur
generator = ReportGenerator()
rapor = generator.generate(semptomlar, tahliller, yorumlar)

# 📤 Raporu yazdır
print(rapor)
