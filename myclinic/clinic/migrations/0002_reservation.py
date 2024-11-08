# Generated by Django 5.0.6 on 2024-11-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(max_length=20)),
                ('stay_type', models.CharField(choices=[('veterinary', 'ตรวจสุขภาพ'), ('sterilization', 'ทำหมัน'), ('bath', 'อาบน้ำ')], max_length=20)),
                ('size', models.CharField(choices=[('small', 'ขนาดเล็ก (0-4 kg)'), ('medium', 'ขนาดกลาง (5-10 kg)'), ('large', 'ขนาดใหญ่ (11-25 kg)'), ('extra_large', 'ขนาดใหญ่พิเศษ (26-44 kg)')], max_length=20)),
                ('booking_date', models.DateTimeField()),
            ],
        ),
    ]
