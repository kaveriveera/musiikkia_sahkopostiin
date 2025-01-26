# musiikkia_sahkopostiin
Python-sovellus, joka poimii satunnaisen kappaleen tiedostosta ja lähettää sen sähköpostitse Gmailin SMTP-palvelimen avulla. Sisältää Docker-tuen.

# Käyttö

## Luo Gmail-sovelluskohtainen salasana
Tämä onnistuu Google-tilisi asetuksista kohdasta "Sovelluskohtaiset salasanat".

## Luo '.env'-tiedosto
Ohjelma käyttää '.env'-tiedostoa Gmail-tilisi, salasanasi ja vastaanottajan sähköpostiosoitteen määrittämiseen. Luo '.env'-tiedosto projektin juurihakemistoon seuraavasti:

GMAIL_KAYTTAJATUNNUS = sahkopostisi@gmail.com
GMAIL_SOVELLUSKOHTAINEN_SALASANA = 16-merkkinen-salasana
GMAIL_VASTAANOTTAJA = vastaanottajan.sahkoposti@gmail.com

## Suorita
python main.py
