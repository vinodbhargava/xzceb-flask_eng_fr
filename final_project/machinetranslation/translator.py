"""
Translator module for translating -
1. English to French
2. French to English
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
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def get_translated_text(input_text, model_id):
    '''
    This method invokes translation API for given input and provided model id
    and returns translation text for given model id
    '''
    return language_translator.translate(
        text=input_text,
        model_id=model_id).get_result()['translations'][0]['translation']

def english_to_french(english_text):
    '''
    This method converts english input text to french text
    '''

    # get translated text by invoking get_translated_text function
    french_text = get_translated_text(english_text, 'en-fr')

    return french_text

def french_to_english(french_text):
    '''
    This method converts french input text to english text
    '''

    # get translated text by invoking get_translated_text function
    english_text = get_translated_text(french_text, 'fr-en')

    return english_text
