class ReportGenerator:
    def __init__(self):
        pass

    def generate(self, symptoms, lab_results, comments):
        rapor = "🩺 **Yapay Zekâ Destekli Sağlık Raporu**\n\n"

        if symptoms:
            rapor += "🔹 Bildirilen semptomlar:\n"
            for s in symptoms:
                rapor += f"- {s.capitalize()}\n"

        if lab_results:
            rapor += "\n🔹 Tahlil sonuçları:\n"
            for result in lab_results:
                test = result['test']
                value = result['value']
                unit = result['unit']
                rapor += f"- {test}: {value} {unit}\n"

        if comments:
            rapor += "\n🔹 Ön değerlendirme:\n"
            for c in comments:
                rapor += f"- {c}\n"

        rapor += "\n📌 Bu rapor yapay zekâ tarafından desteklenmiş otomatik ön analizdir. Kesin tanı için lütfen uzman hekime başvurunuz."

        return rapor
