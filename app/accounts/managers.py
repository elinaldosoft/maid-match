from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

from app.common.choices import TYPE_USER
from app.common import utils


class UserManager(BaseUserManager):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop('type', TYPE_USER.admin)
        super().__init__(*args, **kwargs)

    def add_ip_agent(self, user, request: HttpRequest) -> None:
        if request:
            data = utils.get_ip_and_agent(request)
            user.ip = data.get('ip')
            user.agent = data.get('agent')

    def create_user(self, email, password=None, **kwargs):
        email = utils.normalize_email(email)
        request = kwargs.pop('request', None)
        user = self.model(email=email, **kwargs)
        self.add_ip_agent(user, request)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        kwargs['type'] = TYPE_USER.admin
        return self.create_user(**kwargs)

    def create(self, **kwargs):
        if self.type:
            kwargs.update({'type': self.type})

        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs.get('password'))
        return super().create(**kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(type__in=self.type.split(', '))
