from django.shortcuts import render

import commonware


log = commonware.log.getLogger('blog')


def home(request):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    log.debug("I'm alive!")
    return render(request, 'blog/home.html', data)
