from .serializers import (
    RuMultiLanguageContentReadSerializer,
    EnMultiLanguageContentReadSerializer,
    MultiLanguageContentWriteSerializer,
)


class CreatedByMixin:

    def get_serializer_class(self):
        if self.request.GET and ('lang' in self.request.GET.keys()):
            lang = self.request.GET.get('lang')
            # print('lang', lang)
            if lang not in ('ru', 'en'):
                lang = 'ru'
        else:
            if self.request.method == 'GET':
                return RuMultiLanguageContentReadSerializer
            return MultiLanguageContentWriteSerializer
        match lang:
            case 'ru':
                return RuMultiLanguageContentReadSerializer
            case 'en':
                return EnMultiLanguageContentReadSerializer
