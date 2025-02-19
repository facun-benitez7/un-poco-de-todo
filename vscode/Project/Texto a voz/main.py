from gtts import gTTS
import os

texto = "Hoy es un buen dia para aprender Python"

output = gTTS(texto, lang="es", slow=False)
output.save("output.mp3")

os.system("start output.mp3")
