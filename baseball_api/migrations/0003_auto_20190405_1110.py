# Generated by Django 2.2 on 2019-04-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_api', '0002_auto_20190405_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='_2b',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='_3b',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='ab',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='bb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='cs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='g',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='gidp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='h',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='hbp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='hr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='ibb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='lgid',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='player',
            field=models.ForeignKey(on_delete='CASCADE', to='baseball_api.Player', to_field='playerid'),
        ),
        migrations.AlterField(
            model_name='batting',
            name='r',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='rbi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='sb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='sf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='sh',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='so',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='stint',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='teamid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='batting',
            name='yearid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='bapp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='bb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='bfp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='bk',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='cg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='er',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='era',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='g',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='gf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='gidp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='gs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='h',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='hbp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='hr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='ibb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='ipouts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='l',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='lgid',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='player',
            field=models.ForeignKey(on_delete='CASCADE', to='baseball_api.Player', to_field='playerid'),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='r',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='sf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='sh',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='sho',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='so',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='stint',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='sv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='teamid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='w',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='wp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='yearid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bats',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bbrefid',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthcity',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthcountry',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthmonth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthstate',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='birthyear',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathcity',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathcountry',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathday',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathmonth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathstate',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='deathyear',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='debut',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='finalgame',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='namefirst',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='namegiven',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='namelast',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='retroid',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='throws',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
