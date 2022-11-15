"""This module contains two functions for translating from French to English and vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

# Translate from English to French
def  english_to_french(text_to_translate):
    """This function translate an english given text to french

    Args:
        text_to_translate (str): the text to translate in english

    Returns:
        french_text (str): the text translated in French
    """
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='en-fr').get_result()
    for k_k,v_v in translation.items():
        if k_k=='translations':
            for i_i in v_v :
                for key,value in i_i.items() :
                    if key=='translation':
                        french_text=value
    return french_text
print(english_to_french(
    'Hello everybody, my name is Ayoub Ammor, i am from Morocco, nice to meet you.'
    ))
# Translate from French to English
def  french_to_english(text_to_translate):
    """This function translate a french given text to english

    Args:
        text_to_translate (str): the text to translate in french

    Returns:
        english_text (str): the text translated in english
    """
    translation = language_translator.translate(
    text=text_to_translate,
    model_id='fr-en').get_result()
    for k_k,v_v in translation.items():
        if k_k=='translations':
            for i_i in v_v :
                for key,value in i_i.items() :
                    if key=='translation':
                        english_text=value
    return english_text
print(type(french_to_english('Bonjour')))
