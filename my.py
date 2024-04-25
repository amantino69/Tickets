import sounddevice as sd
import numpy as np
from google.cloud import speech
import pyttsx3
from dotenv import load_dotenv
import os
from pdb import set_trace

from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Usar getenv para carregar a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS
google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

set_trace()

# Verificar se a variável de ambiente foi carregada corretamente
if google_application_credentials is None:
    print("A variável de ambiente GOOGLE_APPLICATION_CREDENTIALS não foi definida")
else:
    print(f"A variável de ambiente GOOGLE_APPLICATION_CREDENTIALS foi definida para: {google_application_credentials}")

# Inicializar o cliente de reconhecimento de fala
client = speech.SpeechClient()

# Inicializar o conversor de texto em fala
engine = pyttsx3.init()

# Definir a duração da gravação (em segundos)
duration = 5  # gravação de 5 segundos

# Gravar o áudio do microfone usando a biblioteca sounddevice
print("Diga algo!")
recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
sd.wait()

# Converter o áudio para um formato que a biblioteca google-cloud-speech possa entender
recording = np.int16(recording * 32767).tobytes()

# Criar um objeto RecognitionAudio com o áudio gravado
audio = speech.RecognitionAudio(content=recording)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="pt-BR",
)

try:
    # Reconhecer a fala usando o Google Cloud Speech
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Você disse: {}".format(result.alternatives[0].transcript))

        # Reproduzir o texto reconhecido
        engine.say(result.alternatives[0].transcript)
        engine.runAndWait()

except Exception as e:
    print("Não foi possível solicitar resultados do serviço Google Cloud Speech; {0}".format(e))