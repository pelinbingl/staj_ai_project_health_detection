from gtts import gTTS
from pydub import AudioSegment

# Türkçe metin
metin = "Üç gündür başım dönüyor. Sabah kalkınca daha da kötü oluyor. Göğsümde baskı şeklinde bir ağrı var ve kendimi halsiz hissediyorum."

# TTS ile .mp3 üret
tts = gTTS(metin, lang='tr')
tts.save("ses_kaydi.mp3")

# .mp3'ü .wav'e çevir
sound = AudioSegment.from_mp3("ses_kaydi.mp3")
sound.export("ses_kaydi.wav", format="wav")

print("✅ ses_kaydi.wav başarıyla oluşturuldu.")
