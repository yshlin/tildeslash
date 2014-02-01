

class DefaultLocaleMiddleware(object):
    def process_request(self, request):
        import tower
        from tildeslash.settings import DEFAULT_LOCALE
        request.locale = DEFAULT_LOCALE
        tower.activate(DEFAULT_LOCALE)