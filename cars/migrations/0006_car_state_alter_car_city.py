# Generated by Django 5.0.3 on 2024-03-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_rename_milage_car_km_remove_car_miles'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AB', 'Alba'), ('AR', 'Arad'), ('AG', 'Argeş'), ('BC', 'Bacău'), ('BH', 'Bihor'), ('BN', 'Bistriţa-Năsăud'), ('BT', 'Botoşani'), ('BR', 'Brăila'), ('BV', 'Braşov'), ('BZ', 'Buzău'), ('CL', 'Călăraşi'), ('CS', 'Caraş-Severin'), ('CT', 'Constanţa'), ('CJ', 'Cluj-Napoca'), ('CV', 'Covasna'), ('DB', 'Dâmboviţa'), ('DJ', 'Dolj'), ('GL', 'Galaţi'), ('GR', 'Giurgiu'), ('GJ', 'Gorj'), ('HR', 'Harghita'), ('HD', 'Hunedoara'), ('IL', 'Ialomiţa'), ('IS', 'Iaşi'), ('IF', 'Ilfov'), ('MM', 'Maramureş'), ('MH', 'Mehedinţi'), ('MS', 'Mureş'), ('NT', 'Neamţ'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SJ', 'Sălaj'), ('SM', 'Satu Mare'), ('SB', 'Sibiu'), ('SV', 'Suceava'), ('TR', 'Teleorman'), ('TM', 'Timişoara'), ('TL', 'Tulcea'), ('VL', 'Vâlcea'), ('VS', 'Rhode Island'), ('VN', 'Vrancea'), ('B', '\tBucureşti')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
