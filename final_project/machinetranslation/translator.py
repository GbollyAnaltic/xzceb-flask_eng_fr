import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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



#print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))



def englishtofrench(englishtext):

    if englishtext =='':

        return 'Empty'

    translation_new = language_translator.translate(text=englishtext ,model_id='en-fr').get_result()

    french_text= translation_new['translations'][0]['translation']

    return french_text

def frenchtoenglish(frenchtext):

    if frenchtext =='':

        return 'Empty'

    translation_new = language_translator.translate(text=frenchtext ,model_id='fr-en').get_result()

    english_text= translation_new['translations'][0]['translation']

    return english_text



print(englishtofrench(''))

print(frenchtoenglish('Bonjour'))