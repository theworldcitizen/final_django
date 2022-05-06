# Generated by Django 3.2.12 on 2022-05-01 16:30

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('number_of_stars', models.IntegerField(choices=[(1, 'One-Star'), (2, 'Two-Star'), (3, 'Three-Star'), (4, 'Four-Star'), (5, 'Five-Star')], verbose_name='Number of stars')),
                ('number_of_ratings', models.IntegerField(default=0, verbose_name='Number of ratings')),
                ('rating', models.FloatField(default=0, verbose_name='rating')),
                ('account_number', models.IntegerField(verbose_name='Account Number')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('yard', models.BooleanField(verbose_name='Yard')),
                ('pool', models.BooleanField(verbose_name='Pool')),
                ('gym', models.BooleanField(verbose_name='Gym')),
                ('wifi', models.BooleanField(verbose_name='Wifi')),
                ('parking', models.BooleanField(verbose_name='Parking')),
                ('restaurant', models.BooleanField(verbose_name='Restaurant')),
                ('hotelier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Hotelier')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
            managers=[
                ('objects', api.models.HotelManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(validators=[api.models.is_valid_date], verbose_name='Check In')),
                ('check_out', models.DateField(validators=[api.models.is_valid_date], verbose_name='Check Out')),
                ('total_cost', models.IntegerField(validators=[api.models.is_valid_number], verbose_name='Total Cost')),
                ('payment_status', models.IntegerField(choices=[(1, 'Paid'), (0, 'Unpaid')], verbose_name='Payment status')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_reservations', to='api.hotel', verbose_name='Hotel')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
            },
            managers=[
                ('objects', api.models.ReservationManager()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SINGLE', 'Single Room'), ('K_DOUBLE', 'King Double Room'), ('Q_DOUBLE', 'Queen Double Room'), ('SINGLE_DELUXE', 'Single Deluxe Room'), ('DOUBLE_DELUXE', 'Double Deluxe Room'), ('TWIN', 'Twin Room'), ('TWIN_DOUBLE', 'Twin Double Room'), ('TRIPLE', 'Triple Room'), ('PRESIDENTIAL', 'Presidential Suite')], max_length=20, verbose_name='Type')),
                ('cost', models.IntegerField(validators=[api.models.is_valid_number], verbose_name='Cost')),
                ('area', models.IntegerField(validators=[api.models.is_valid_number], verbose_name='Area')),
                ('king_bed', models.IntegerField(verbose_name='King Bed')),
                ('queen_bed', models.IntegerField(verbose_name='Queen Bed')),
                ('tv', models.BooleanField(verbose_name='TV')),
                ('wifi', models.BooleanField(verbose_name='Wifi')),
                ('kitchen', models.BooleanField(verbose_name='Kitchen')),
                ('extra_bed', models.BooleanField(verbose_name='Extra Bed')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.hotel', verbose_name='Hotel')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
            managers=[
                ('objects', api.models.RoomManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.IntegerField(verbose_name='Reference number')),
                ('reservation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_transaction', to='api.reservation', verbose_name='Reservation')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='room_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_photos', to='api.room', verbose_name='Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_reservations', to='api.room', verbose_name='Room'),
        ),
        migrations.CreateModel(
            name='HotelPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='hotel_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_photos', to='api.hotel', verbose_name='Hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(validators=[api.models.is_valid_comment], verbose_name='Comment Text')),
                ('rating', models.IntegerField(choices=[(1, 'One-Star'), (2, 'Two-Star'), (3, 'Three-Star'), (4, 'Four-Star'), (5, 'Five-Star')], verbose_name='Number of stars')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_comments', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_comments', to='api.hotel', verbose_name='Hotel')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            managers=[
                ('objects', api.models.CommentManager()),
            ],
        ),
    ]
