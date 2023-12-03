from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from .models import Question, Question2, Question3

class CustomFilter(SimpleListFilter):
    title = "Controle de Veículo / Pedestre"
    parameter_name = "custom"

    def lookups(self, request, model_admin):
        return(
            ("diurno1", "diurno1"),
            ("noturno1", "noturno1"),
            ("diurno2", "diurno2"),
            ("noturno2", "noturno2")
        )

    def queryset(self, request, queryset):
        if self.value() == "diurno1":
            queryset = queryset.filter(question_text__contains="diurno1")
        if self.value() == "diurno2":
            queryset = queryset.filter(question_text__contains="diurno2")
        if self.value() == "noturno1":
            queryset = queryset.filter(question_text__contains="noturno1")
        elif self.value() == "noturno2":
            queryset = queryset.filter(question_text__contains="noturno2")
        return queryset  
    
class CustomFilter2(SimpleListFilter):
    title = "Entrada/Saída de Cargas"
    parameter_name = "custom2"

    def lookups(self, request, model_admin):
        return(
            ("Gusa", "Gusa"),
            ("Escória", "Escória"),
            ("Finos de minério", "Finos de minério"),
            ("Moinho de carvão", "Moinho de carvão"),
            ("Pó de balão", "Pó de balão"),
            ("Resíduo de terra", "Resíduo de terra"),
            ("Rejeitos", "Rejeitos")
        )

    def queryset(self, request, queryset):
        if self.value() == "Gusa":
            queryset = queryset.filter(question_text__contains="Gusa")
        if self.value() == "Escória":
            queryset = queryset.filter(question_text__contains="Escória")
        if self.value() == "Finos de minério":
            queryset = queryset.filter(question_text__contains="Finos de minério")
        if self.value() == "Moinho de carvão":
            queryset = queryset.filter(question_text__contains="Moinho de carvão")
        if self.value() == "Pó de balão":
            queryset = queryset.filter(question_text__contains="Pó de balão")
        if self.value() == "Resíduo de terra":
            queryset = queryset.filter(question_text__contains="Resíduo de terra")
        elif self.value() == "Rejeitos":
            queryset = queryset.filter(question_text__contains="Rejeitos")
        return queryset  

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["pub_date", CustomFilter]
    list_display = ('veiculo','placa','pub_date','hora_saida','ativo','vigilante','modificado')

admin.site.register(Question, QuestionAdmin)


class Question2Admin(admin.ModelAdmin):
    list_filter = ["pub_date", CustomFilter]
    list_display = ('nome','identidade','pub_date','hora_saida','ativo','vigilante','modificado')

admin.site.register(Question2, Question2Admin)

class Question3Admin(admin.ModelAdmin):
    list_filter = ["pub_date", CustomFilter]
    list_display = ('carga','placa','pub_date','hora_saida','ativo','vigilante','modificado')

admin.site.register(Question3, Question3Admin)


