class DiagnosisEngine:
    def __init__(self):
        # Semptom → Olası hastalıklar (çok sade örnek)
        self.symptom_disease_map = {
            "baş dönmesi": ["Düşük tansiyon", "Anemi", "İç kulak hastalıkları"],
            "mide bulantısı": ["Gıda zehirlenmesi", "Migren", "Gastrit"],
            "göğüs ağrısı": ["Kalp krizi", "Kas spazmı", "Reflü"],
            "ateş": ["Enfeksiyon", "Grip", "COVID-19"],
            "öksürük": ["Bronşit", "Astım", "Zatürre"]
        }

    def evaluate(self, symptoms, lab_results):
        diagnoses = []

        # Semptomlara göre tahminler
        for symptom in symptoms:
            diseases = self.symptom_disease_map.get(symptom, [])
            for disease in diseases:
                if disease not in diagnoses:
                    diagnoses.append(f"Semptoma göre olası: {disease}")

        # Tahlil analiz kuralları
        for result in lab_results:
            test = result["test"].lower()
            value = result["value"]

            if test == "crp" and value > 5:
                diagnoses.append("CRP yüksek → Vücutta iltihap/infeksiyon olabilir.")
            if test == "glukoz" and value > 110:
                diagnoses.append("Glukoz yüksek → Hiperglisemi (şeker hastalığı) riski.")
            if test == "hemoglobin" and value < 12:
                diagnoses.append("Hemoglobin düşük → Anemi (kansızlık) olabilir.")

        return diagnoses
