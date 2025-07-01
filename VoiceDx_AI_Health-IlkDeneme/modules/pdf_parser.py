import pdfplumber
import re

class PDFParser:
    def __init__(self):
        pass

    def parse(self, pdf_path):
        results = []

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if not text:
                        print(f"[Sayfa {page_number+1}] metin bulunamadı.")
                        continue

                    lines = text.split('\n')
                    print(f"\n--- Sayfa {page_number+1} ---")
                    for line in lines:
                        print(f"[SATIR]: {line}")  # her satırı yazdırıyoruz (sorunları görmek için)

                        # Satırı boşluklara ya da tab'lara göre ayır
                        parts = re.split(r"\s{2,}|\t+|\s+", line)

                        if len(parts) >= 3:
                            test_name = parts[0]
                            value_match = re.findall(r"[\d.]+", parts[1])
                            unit = parts[2]

                            if value_match:
                                try:
                                    value = float(value_match[0])
                                    results.append({
                                        "test": test_name,
                                        "value": value,
                                        "unit": unit
                                    })
                                except Exception as e:
                                    print(f"Sayısal dönüştürme hatası: {e}")
                                    continue
        except Exception as e:
            print(f"PDF açma hatası: {e}")

        return results
