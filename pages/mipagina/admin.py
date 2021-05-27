from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersCreationForm, UsuarioPersChangeForm
from .models import UsuarioPers,Viaje,Hospedaje,Ciudad,Vuelo

#creacion y visualizacion del usuario personalizado
class UsuarioPersAdmin(UserAdmin):
    add_form = UsuarioPersCreationForm
    form = UsuarioPersChangeForm
    model = UsuarioPers
    list_display = ['email', 'username', 'edad' , 'telefono','genero', 'is_staff',]

# Register your models here.
#registro de los modelos para poder visualizarlos el admin
admin.site.register(UsuarioPers,UsuarioPersAdmin)
admin.site.register(Viaje)
admin.site.register(Hospedaje)
admin.site.register(Ciudad)
admin.site.register(Vuelo)