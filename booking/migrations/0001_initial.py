# Generated by Django 4.1.7 on 2023-04-03 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professors', models.CharField(choices=[('Biplab Basak', 'Biplab Basak'), ('Niladri Chatterjee', 'Niladri Chatterjee'), ('Aparajita Dasgupta', 'Aparajita Dasgupta'), ('Minati De', 'Minati De'), ('S. Dharmaraja', 'S. Dharmaraja'), ('Debdip Ganguly', 'Debdip Ganguly'), ('Surjeet Kaur', 'Surjeet Kaur'), ('Harish Kumar', 'Harish Kumar'), ('N. Shravan Kumar', 'N. Shravan Kumar'), ('V.V.K. Srinivas Kumar', 'V.V.K. Srinivas Kumar'), ('Ananta Kumar Majee', 'Ananta Kumar Majee'), ('Aparna Mehra', 'Aparna Mehra'), ('Mani Mehra', 'Mani Mehra'), ('Vivek Mukundan', 'Vivek Mukundan'), ('Anima Nagar', 'Anima Nagar'), ('B.S. Panda', 'B.S. Panda'), ('Shiv Prakash Patel', 'Shiv Prakash Patel'), ('Kamana Porwal', 'Kamana Porwal'), ('Amit Priyadarshi', 'Amit Priyadarshi'), ('Ashutosh Rai', 'Ashutosh Rai'), ('S.C.S. Rao', 'S.C.S. Rao'), ('Biswajyoti Saha', 'Biswajyoti Saha'), ('Ekata Saha', 'Ekata Saha'), ('Sivananthan Sampath', 'Sivanathan Sampath'), ('Ritumoni Sarma', 'Ritumoni Sarma'), ('Punit Sharma', 'Punit Sharma'), ('Rajendra Kumar Sharma', 'Rajendra Kumar Sharma'), ('Vikas Vikram Singh', 'Vikas Vikram Singh'), ('K. Sreenadh', 'K. Sreenadh'), ('Amitabha Tripathi', 'Amitabha Tripathi'), ('Viswanathan Puthan Veedu', 'Viswanathan Puthan Veedu')], default='Aparna Mehra', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('10 AM', '10 AM'), ('10:30 AM', '10:30 AM'), ('11 AM', '11 AM'), ('11:30 AM', '11:30 AM'), ('12 NOON', '12 NOON'), ('12:30 PM', '12:30 PM'), ('1 PM', '1 PM'), ('1:30 PM', '1:30 PM'), ('2 PM', '2 PM'), ('2:30 PM', '2:30 PM'), ('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM')], default='10 AM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]