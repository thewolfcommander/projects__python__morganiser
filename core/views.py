from django.http import HttpResponse
from django.views.generic import View


class HomePageView(View):
    """
    View Class for handling home page of the Moorganiser website
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("Helo world")