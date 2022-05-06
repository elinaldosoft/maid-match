from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


from app.common.models import Base
from app.common import choices
from app.common import fields
from app.common import messages

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, Base):
    name = models.CharField(max_length=255, verbose_name=_('Nome Completo'), null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, error_messages={'unique': messages.DUPLICATION_EMAIL})
    phone = models.CharField(max_length=255, verbose_name=_('Telefone'), blank=True, null=True)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
        verbose_name='Acesso ao Dashboard?',
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        verbose_name='Ativo?',
    )
    gender = models.CharField(max_length=10, choices=(
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ), blank=True, null=True)
    picture = fields.ImageField(blank=True, null=True, upload_to='profile')
    birth_data = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    document = models.CharField(max_length=50, blank=True, null=True, verbose_name='Documento')

    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='País')
    zipcode = models.CharField(max_length=20, blank=True, null=True, verbose_name='Cep')
    state = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número')
    complement = models.CharField(max_length=250, blank=True, null=True, verbose_name='Complemento')
    address = models.CharField(max_length=250, blank=True, null=True, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')

    type = models.CharField(max_length=20, default='subscriber', choices=choices.TYPE_USER, editable=False)
    objects = UserManager(type='admin, client, helper')
    last_login = None

    USERNAME_FIELD = 'email'


class Client(User):
    objects = UserManager(type=choices.TYPE_USER.client)

    class Meta:
        proxy = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = choices.TYPE_USER.client
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)


class Helper(User):
    objects = UserManager(type=choices.TYPE_USER.helper)

    class Meta:
        proxy = True
        verbose_name = 'Diarista'
        verbose_name_plural = 'Diaristas'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = choices.TYPE_USER.helper
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)
