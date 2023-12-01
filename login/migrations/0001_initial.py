# Generated by Django 4.2.7 on 2023-11-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100, null=True)),
                ('admin', models.BooleanField(default=0)),
                ('phone_number', models.IntegerField(null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('action', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('date_due', models.DateField(blank=True, null=True)),
                ('type', models.BooleanField(default=0)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('contribution_month', models.IntegerField(default=0)),
                ('contribution_year', models.IntegerField(default=2001)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.IntegerField(default=1)),
                ('loan', models.IntegerField(default=6300)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=20)),
                ('aggregate_balance', models.IntegerField(default=6300)),
                ('total_contributions', models.IntegerField(default=10500)),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('event', 'event'), ('info', 'info'), ('system', 'system'), ('team', 'team')], max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('sender', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=1000)),
                ('subject', models.CharField(default='Welcome Message', max_length=250)),
                ('read', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PayLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=50)),
                ('payment_amount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('payment_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=20)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField()),
            ],
        ),
    ]