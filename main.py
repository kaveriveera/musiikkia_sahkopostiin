import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def arvo_kappale(tiedosto):
     """
     Arpoo tiedostosta satunnaisen kappaleen.
     """
     with open(tiedosto, "r", encoding="utf-8") as rivit:
        kappaleet = rivit.readlines()
        return random.choice(kappaleet).strip()
     
def laheta_sahkoposti(lahettaja, salasana, vastaanottaja, aihe, sisalto):
    """
    Lähettää sähköpostin käyttäen smtplib -kirjastoa.
    """
    try:
        viesti = MIMEMultipart()
        viesti["From"] = lahettaja
        viesti["To"] = vastaanottaja
        viesti["Subject"] = aihe
        viesti.attach(MIMEText(sisalto, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(lahettaja, salasana)
            server.send_message(viesti)
        print("Viesti lähetetty!")
    except Exception as e:
        print(f"Virhe viestin lähetyksessä: {e}")

if __name__ == "__main__":
    tiedosto = "kappaleet.txt"
    lahettaja = os.getenv("GMAIL_KAYTTAJATUNNUS")  #ympäristömuuttuja Gmail-osoitteelle
    salasana = os.getenv("GMAIL_SOVELLUSKOHTAINEN_SALASANA")  #ympäristömuuttuja sovelluskohtaiselle salasanalle
    vastaanottaja = os.getenv("GMAIL_VASTAANOTTAJA")  #vastaanottajan sähköposti

    if not lahettaja or not salasana:
        print("Virhe: GMAIL_USER tai GMAIL_APP_PASSWORD ei ole asetettu ympäristömuuttujaksi.")
        exit(1)

    #satunnaunen kappale tiedostosta
    kappale = arvo_kappale(tiedosto)

    #kappaleen lähetys
    aihe = "Päivän kappale"
    viesti = f"Tässä on päivän kappale:\n\n{kappale}"
    laheta_sahkoposti(lahettaja, salasana, vastaanottaja, aihe, viesti)
    
