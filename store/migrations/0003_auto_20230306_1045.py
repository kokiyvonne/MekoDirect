# Generated by Django 4.1.6 on 2023-03-06 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.RunSQL(
                          """
                          INSERT INTO store_collection (title) VALUES ("collection1");
                          """,
                          """
                          DELETE FROM store_collection WHERE title = 'collection1';
                          """)
    ]