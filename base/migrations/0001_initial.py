# Generated by Django 4.1.5 on 2023-01-08 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_limit', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('accept_pet', models.BooleanField()),
                ('cleaning_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('activated_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
