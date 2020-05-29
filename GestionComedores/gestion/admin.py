from django.contrib import admin
from gestion.models import Escuela, Distrito, Solicitante, Necesidad, NecesidadSolicitante


class NecesidadSolicitanteAdminInline(admin.TabularInline):
    verbose_name_plural = u'Necesidades'
    verbose_name = u'Necesidad'
    model = NecesidadSolicitante
    fieldsets = (
        (None, {
            'fields': (
                ('necesidad', 'cubierta', 'fecha_solicitud', 'fecha_cobertura'),
            )}),
    )
    extra = 1


@admin.register(Solicitante)
class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'numero_documento', 'escuela']
    #list_filter = ['escuela']
    search_fields = ['numero_documento']
    inlines = [
        NecesidadSolicitanteAdminInline,
    ]

    def get_fieldsets(self, request, obj=None):
        if request.user.groups.filter(name='Escuela').exists():
            return self.escuela_fieldsets
        elif request.user.groups.filter(name='Distrito').exists():
            return self.admin_fieldsets
        elif request.user.groups.filter(name='Admin').exists():
            return self.admin_fieldsets
        return None

    escuela_fieldsets = (
        ('Alumno', {
            'fields': (
                ('apellido', 'nombre'),
                ('tipo_documento', 'numero_documento',),
                'fecha_nacimiento', 'sexo',
                ('direccion', 'numero',),
                'grado',

                'grupo_familiar',
                'fecha',
                'activo'
            )
        }),
        ('Responsable', {
            'fields': (
                'vinculo',
                ('apellido_reponsable', 'nombre_reponsable'),
                ('tipo_documento_reponsable', 'numero_documento_reponsable'),
                'sexo_responsable',
            )
        }),
    )
    admin_fieldsets = (
        ('Alumno', {
            'fields': (
                'escuela',
                ('apellido', 'nombre'),
                ('tipo_documento', 'numero_documento',),
                'fecha_nacimiento', 'sexo',
                ('direccion', 'numero',),
                'grado',

                'grupo_familiar',
                'fecha',
                'activo'
            )
        }),
        ('Responsable', {
            'fields': (
                'vinculo',
                ('apellido_reponsable', 'nombre_reponsable'),
                ('tipo_documento_reponsable', 'numero_documento_reponsable'),
                'sexo_responsable',
                )
        }),
    )

    def get_queryset(self, request):
        if request.user.groups.filter(name='Escuela').exists():
            solicitante = Solicitante.objects.filter(escuela__usuario__username=request.user.username)
        elif request.user.groups.filter(name='Admin').exists():
            solicitante = Solicitante.objects.all()
        elif request.user.groups.filter(name='Distrito').exists():
            solicitante = Solicitante.objects.filter(escuela__distrito__usuario__username=request.user.username)
        else:
            solicitante = None
        return solicitante

    def save_model(self, request, obj, form, change):
        if not obj.pk and not request.user.groups.filter(name='Admin').exists():
            obj.escuela = Escuela.objects.get(usuario=request.user)
        super().save_model(request, obj, form, change)


@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero']


@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero', 'direccion']


@admin.register(Necesidad)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']


@admin.register(NecesidadSolicitante)
class NecesidadSolicitanteAdmin(admin.ModelAdmin):
    list_display = ['solicitante', 'necesidad', 'cubierta', 'fecha_solicitud', 'fecha_cobertura', 'escuela']
    list_display_links = None
    list_select_related = ['solicitante', 'solicitante__escuela']
    list_filter = ['cubierta', 'necesidad', 'fecha_solicitud', 'solicitante__escuela']

    def escuela(self, obj):
        return obj.solicitante.escuela

    def has_add_permission(self, request):
        return False


