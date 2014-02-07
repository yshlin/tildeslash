from tildeslash import settings


def setting_values(request):
    return {'CODELOG_TITLE': settings.CODELOG_TITLE}