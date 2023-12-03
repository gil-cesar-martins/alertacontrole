import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    TURNO_CHOICES = (
        ("diurno1", "diurno1"),
        ("noturno1", "noturno1"),
        ("diurno2", "diurno2"),
        ("noturno2", "noturno2")
    )

    question_text = models.CharField('Turno',max_length=32, choices=TURNO_CHOICES, null=True, blank=True)
    pub_date = models.DateTimeField('Data de registro')
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    veiculo = models.CharField('Veículo', max_length=30 )
    placa = models.CharField('Placa', max_length=10)
    hora_saida = models.DateTimeField('Saída', null=True, blank=True)
    ativo = models.BooleanField('Ativo?', default=True)
    vigilante = models.CharField('Vigilante', max_length=50)
    observacao = models.TextField('Observacao', default='NA') 

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question2(models.Model):
    TURNO_CHOICES = (
        ("diurno1", "diurno1"),
        ("noturno1", "noturno1"),
        ("diurno2", "diurno2"),
        ("noturno2", "noturno2")
    )
    
    question_text = models.CharField('Turno',max_length=32, choices=TURNO_CHOICES, null=True, blank=True)
    pub_date = models.DateTimeField('Data de registro')
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    nome = models.CharField('Nome', max_length=50)
    identidade = models.CharField('Identidade/CPF', max_length=15)
    hora_saida = models.DateTimeField('Saída', null=True, blank=True)
    ativo = models.BooleanField('Ativo?', default=True)  
    vigilante = models.CharField('Vigilante', max_length=50)
    observacao = models.TextField('Motivo da Visita', default='NA') 

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question3(models.Model):
    TURNO_CHOICES = (
        ("diurno1", "diurno1"),
        ("noturno1", "noturno1"),
        ("diurno2", "diurno2"),
        ("noturno2", "noturno2")
    )
    
    CARGA_CHOICES = (
        ("Gusa", "Gusa"),
        ("Escória", "Escória"),
        ("Finos de minério", "Finos de minério"),
        ("Carvão", "Carvão"),
        ("Pó de balão", "Pó de balão"),
        ("Resíduo de terra", "Resíduo de terra"),
        ("Rejeitos", "Rejeitos")
    )

    question_text = models.CharField('Turno',max_length=32, choices=TURNO_CHOICES, null=True, blank=True)
    pub_date = models.DateTimeField('Data de registro')
    carga = models.CharField('Saída de carga',max_length=32, choices=CARGA_CHOICES, null=True, blank=True)
    peso = models.CharField('Toneladas', max_length=10, null=True, blank=True)
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    motorista = models.CharField('Motorista', max_length=50, null=True, blank=True)
    identidade = models.CharField('Identidade/CPF', max_length=15, null=True, blank=True)
    cnh= models.CharField('CNH', max_length=15, null=True, blank=True)
    veiculo = models.CharField('Veículo', max_length=30 )
    placa = models.CharField('Placa', max_length=10)
    hora_saida = models.DateTimeField('Saída', null=True, blank=True)
    ativo = models.BooleanField('Ativo?',  default=True)
    vigilante = models.CharField('Vigilante', max_length=50)
    observacao = models.TextField('Observacao', default='NA') 

    class Meta:
        verbose_name = 'Carga'
        verbose_name_plural = 'Carga'

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
