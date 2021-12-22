import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
#import unittest

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
version_id = '2018-05-01'
language_translator = LanguageTranslatorV3(version=version_id,authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Takes english text as arguement and returns french translation'''
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text 

def french_to_english(french_text):
    '''Takes french text as arguement and returns english translation'''
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation = translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text