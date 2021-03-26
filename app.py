import speech_recognition as sr
from playsound import playsound


def reconnaissance():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ecoute en cours...")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        print('Traitement en cours')
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio, language="fr-FR")
        if "Baptiste" in text or "baptiste" in text:
            print('Baptiste')
            playsound('larsen.mp3', block=True)
    except sr.UnknownValueError:
        print("Google ne comprend pas votre audio")
    except sr.RequestError as e:
        print(
            "Erreur lors de la requete vers les serveurs de Google; {0}".format(e))
    reconnaissance()


if __name__ == '__main__':
    reconnaissance()
