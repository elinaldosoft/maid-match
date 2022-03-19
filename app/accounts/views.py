from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


class MixBaseView(View):
    template_name = None

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)


class AccountsView(MixBaseView):
    template_name = 'accounts/index.html'


class AccountsRegisterView(MixBaseView):
    template_name = 'accounts/register.html'


class AccountsComplementRegisterView(MixBaseView):
    template_name = 'accounts/complement_register.html'
