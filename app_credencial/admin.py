from django.contrib import admin
from .models import Pessoa
from .models import PessoaFisica
from .models import Evento
from .models import Ingresso
from .models import Inscricao

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    pass

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    pass

