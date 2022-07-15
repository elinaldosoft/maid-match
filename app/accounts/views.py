from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


class MixBaseView(View):
    template_name = None
    brandtext = None
    logged = False

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, context={'brandtext': self.brandtext, 'logged': self.logged})


class HomeView(MixBaseView):
    template_name = 'accounts/index.html'
    logged = True
    brandtext = 'Listagem de Profissionais'


class AccountsView(MixBaseView):
    template_name = 'accounts/index.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect('home_page')


class AccountsRegisterView(MixBaseView):
    template_name = 'accounts/register.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect('complement_register')


class AccountsComplementRegisterView(MixBaseView):
    template_name = 'accounts/complement_register.html'
    brandtext = "Por favor, complete seu cadastro"


class AccountsEmpolyerProfilesView(MixBaseView):
    template_name = 'profiles/employer_profile.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect('employer_profile.html')
