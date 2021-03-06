# Generated by Django 3.2.13 on 2022-06-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=100)),
                ('original_name', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('KR', 'Korean'), ('JP', 'Japanese'), ('UD', 'Not sure')], default='UD', max_length=2)),
                ('color', models.CharField(choices=[('YL', 'Yellow'), ('RD', 'Red'), ('BR', 'Brown'), ('BL', 'Black'), ('UD', 'Not sure')], default='UD', max_length=2)),
                ('taste', models.CharField(choices=[('SW', 'Sweet'), ('SC', 'Spicy'), ('SR', 'Sour'), ('SL', 'Salty'), ('BT', 'Bitter'), ('UD', 'Not sure')], default='UD', max_length=2)),
                ('protein', models.CharField(choices=[('BF', 'Beef'), ('PR', 'Pork'), ('SF', 'Shell fish'), ('FS', 'Fish'), ('VG', 'Vegetarian'), ('CK', 'Chicken'), ('NM', 'No protein'), ('UD', 'Not sure')], default='UD', max_length=2)),
                ('type', models.CharField(choices=[('BD', 'Boiled'), ('FR', 'Fried'), ('ST', 'Steamed'), ('BE', 'Baked'), ('BQ', 'Barbeque'), ('RW', 'Raw'), ('UD', 'Not sure')], default='UD', max_length=2)),
            ],
        ),
    ]
