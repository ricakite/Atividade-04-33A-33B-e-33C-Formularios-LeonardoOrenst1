from django.contrib import admin
from .models import Torneios, Tenistas, Tabela

# Register your models here.

admin.site.register(Torneios)
admin.site.register(Tenistas)
admin.site.register(Tabela)
