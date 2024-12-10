from deep_translator import GoogleTranslator
#this file translate the text to your desired language
def translate(input, lang):
    translated = GoogleTranslator(source='auto', target=lang).translate(input)  
    print(translated)
    return translated
