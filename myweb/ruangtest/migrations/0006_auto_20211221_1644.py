# Generated by Django 3.2.10 on 2021-12-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruangtest', '0005_auto_20211220_1906'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ask',
            new_name='yrn',
        ),
        migrations.RenameField(
            model_name='yrn',
            old_name='pertanyaan',
            new_name='yrn',
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans1',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans10',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans11',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans12',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans13',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans14',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans15',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans16',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans17',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans18',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans19',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans2',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans20',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans21',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans22',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans3',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans4',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans5',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans6',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans7',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans8',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans9',
            field=models.CharField(choices=[('Ya', 'ya'), ('Tidak', 'tidak')], default='tidak', max_length=10, null=True),
        ),
    ]
