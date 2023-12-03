# Generated by Django 4.2.7 on 2023-12-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, choices=[('diurno1', 'diurno1'), ('noturno1', 'noturno1'), ('diurno2', 'diurno2'), ('noturno2', 'noturno2')], max_length=32, null=True, verbose_name='Turno')),
                ('pub_date', models.DateTimeField(verbose_name='Data de registro')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('veiculo', models.CharField(max_length=30, verbose_name='Veículo')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('hora_saida', models.DateTimeField(blank=True, null=True, verbose_name='Saída')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('vigilante', models.CharField(max_length=50, verbose_name='Vigilante')),
                ('observacao', models.TextField(default='NA', verbose_name='Observacao')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, choices=[('diurno1', 'diurno1'), ('noturno1', 'noturno1'), ('diurno2', 'diurno2'), ('noturno2', 'noturno2')], max_length=32, null=True, verbose_name='Turno')),
                ('pub_date', models.DateTimeField(verbose_name='Data de registro')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('identidade', models.CharField(max_length=15, verbose_name='Identidade/CPF')),
                ('hora_saida', models.DateTimeField(blank=True, null=True, verbose_name='Saída')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('vigilante', models.CharField(max_length=50, verbose_name='Vigilante')),
                ('observacao', models.TextField(default='NA', verbose_name='Motivo da Visita')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
            },
        ),
        migrations.CreateModel(
            name='Question3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, choices=[('diurno1', 'diurno1'), ('noturno1', 'noturno1'), ('diurno2', 'diurno2'), ('noturno2', 'noturno2')], max_length=32, null=True, verbose_name='Turno')),
                ('pub_date', models.DateTimeField(verbose_name='Data de registro')),
                ('carga', models.CharField(blank=True, choices=[('Gusa', 'Gusa'), ('Escória', 'Escória'), ('Finos de minério', 'Finos de minério'), ('Carvão', 'Carvão'), ('Pó de balão', 'Pó de balão'), ('Resíduo de terra', 'Resíduo de terra'), ('Rejeitos', 'Rejeitos')], max_length=32, null=True, verbose_name='Saída de carga')),
                ('peso', models.CharField(blank=True, max_length=10, null=True, verbose_name='Toneladas')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('motorista', models.CharField(blank=True, max_length=50, null=True, verbose_name='Motorista')),
                ('identidade', models.CharField(blank=True, max_length=15, null=True, verbose_name='Identidade/CPF')),
                ('cnh', models.CharField(blank=True, max_length=15, null=True, verbose_name='CNH')),
                ('veiculo', models.CharField(max_length=30, verbose_name='Veículo')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('hora_saida', models.DateTimeField(blank=True, null=True, verbose_name='Saída')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('vigilante', models.CharField(max_length=50, verbose_name='Vigilante')),
                ('observacao', models.TextField(default='NA', verbose_name='Observacao')),
            ],
            options={
                'verbose_name': 'Carga',
                'verbose_name_plural': 'Carga',
            },
        ),
    ]
