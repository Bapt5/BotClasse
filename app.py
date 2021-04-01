import speech_recognition as sr
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def reconnaissance():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ecoute en cours...")
        audio = r.listen(source, phrase_time_limit=15)

    # Speech recognition using Google Speech Recognition
    try:
        print('Traitement en cours...')
        text = r.recognize_google(audio, language="fr-FR")
        if "Baptiste" in text or "baptiste" in text:
            print('Baptiste')
            mic = driver.find_element_by_xpath("//*[@id='mic-enable']")
            if mic.get_attribute("aria-pressed") == "false":
                mic.click()
            playsound('larsen.mp3', block=True)
            mic.click()
    except sr.UnknownValueError:
        print("Google ne comprend pas votre audio")
    except sr.RequestError as e:
        print(
            "Erreur lors de la requete vers les serveurs de Google; {0}".format(e))
    reconnaissance()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 600)
    input('Tapes sur Entrée quand tu es connnecté')
    reconnaissance()
