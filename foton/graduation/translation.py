from modeltranslation.translator import register, translator, TranslationOptions

from .models import Option, Speciality

class OptionTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('fr', 'en')
translator.register(Option, OptionTranslationOptions)


class SpecialityTranslationOptions(TranslationOptions):
	fields = ('name',)
	required_languages = ('fr', 'en')
translator.register(Speciality, SpecialityTranslationOptions)
    
