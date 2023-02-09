from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    """
    View Class for handling home page of the Moorganiser website
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')