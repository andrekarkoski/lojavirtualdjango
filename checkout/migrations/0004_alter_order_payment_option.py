# Generated by Django 3.2.1 on 2021-05-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento'),
        ),
    ]
