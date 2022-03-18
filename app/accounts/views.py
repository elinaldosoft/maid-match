from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


class AccountsView(View):
    template_name = 'accounts/index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
