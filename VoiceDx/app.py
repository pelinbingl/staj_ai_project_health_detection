import os
import re
import pdfplumber
from transformers import pipeline
from huggingface_hub import login

# 🔐 Hugging Face Token ile giriş yap
login("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")  # BURAYA KENDİ TOKENINI YAZ

#  Speech-to-Text (Whisper)
class SpeechToText:
    def __init__(self):
        self.pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base", device=-1)

    def transcribe(self, audio_path):
        result = self.pipeline(audio_path)
        return result["text"]


#  Semptom çıkarıcı
class SymptomClassifier:
    def __init__(self):
        self.symptom_list = [
            "baş dönmesi", "mide bulantısı", "göğüs ağrısı",
            "nefes darlığı", "halsizlik", "ateş", "öksürük"
        ]
        self.synonyms = {
            "başım dönüyor": "baş dönmesi",
            "göğsümde ağrı": "göğüs ağrısı",
            "midem bulanıyor": "mide bulantısı"
        }

    def classify(self, text):
        text = text.lower()
        for k, v in self.synonyms.items():
            if k in text and v not in text:
                text += " " + v
        return [s for s in self.symptom_list if s in text]

# -----------------------------
# 📄 PDF parser (tahlil verisi)
class PDFParser:
    def parse(self, pdf_path):
        results = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text:
                    continue
                for line in text.split('\n'):
                    parts = re.split(r"\s{2,}|\t+|\s+", line)
                    if len(parts) >= 3:
                        test, value_raw, unit = parts[0], parts[1], parts[2]
                        value_match = re.findall(r"[\d.]+", value_raw)
                        if value_match:
                            try:
                                value = float(value_match[0])
                                results.append({"test": test, "value": value, "unit": unit})
                            except:
                                continue
        return results


#  Teşhis motoru
class DiagnosisEngine:
    def __init__(self):
        self.symptom_disease_map = {
            "baş dönmesi": ["Düşük tansiyon", "Anemi"],
            "göğüs ağrısı": ["Kalp krizi", "Kas spazmı"]
        }

    def evaluate(self, symptoms, lab_results):
        diagnoses = []
        for s in symptoms:
            for d in self.symptom_disease_map.get(s, []):
                diagnoses.append(f"Semptoma göre olası: {d}")

        for result in lab_results:
            t, v = result["test"].lower(), result["value"]
            if t == "crp" and v > 5:
                diagnoses.append("CRP yüksek → Enfeksiyon olabilir.")
            if t == "hemoglobin" and v < 12:
                diagnoses.append("Hemoglobin düşük → Anemi olabilir.")
        return diagnoses
    
    
#  Rapor oluşturucu
class ReportGenerator:
    def generate(self, symptoms, lab_results, comments):
        rapor = "🩺 Yapay Zekâ Destekli Sağlık Raporu\n\n"
        if symptoms:
            rapor += "🔹 Semptomlar:\n" + "\n".join(f"- {s}" for s in symptoms) + "\n"
        if lab_results:
            rapor += "\n🔹 Tahlil Sonuçları:\n" + "\n".join(
                f"- {t['test']}: {t['value']} {t['unit']}" for t in lab_results) + "\n"
        if comments:
            rapor += "\n🔹 Ön Değerlendirme:\n" + "\n".join(f"- {c}" for c in comments) + "\n"
        rapor += "\n📌 Not: Bu rapor ön değerlendirme niteliğindedir."
        return rapor

#  ANA AKIŞ
if __name__ == "__main__":
    print("🔊 Ses analizi başlatılıyor...")

    # 1. Ses dosyasını yazıya dök
    stt = SpeechToText()
    metin = stt.transcribe("C:\\Users\\Pelin\\OneDrive\\Desktop\\VoiceDx\\ses_kaydi.wav")
    print(f"📥 Yazıya dökülen ifade:\n{metin}\n")

    # 2. Semptom çıkarımı
    classifier = SymptomClassifier()
    semptomlar = classifier.classify(metin)

    # 3. PDF’ten tahlil al
    parser = PDFParser()
    tahliller = parser.parse("C:\\Users\\Pelin\\OneDrive\\Desktop\\VoiceDx\\Enabiz-Tahlilleri.pdf")

    # 4. Teşhis üret
    motor = DiagnosisEngine()
    yorumlar = motor.evaluate(semptomlar, tahliller)

    # 5. Rapor oluştur
    generator = ReportGenerator()
    rapor = generator.generate(semptomlar, tahliller, yorumlar)

    print("\n" + "=" * 50)
    print(rapor)
    print("=" * 50)
