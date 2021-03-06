from django.db import models

class Player(models.Model):
    playerid = models.CharField(max_length=30, primary_key=True)
    birthyear=models.IntegerField(null=True)
    birthmonth=models.IntegerField(null=True)
    birthday = models.IntegerField(null=True)
    birthcountry = models.CharField(max_length=30,null=True)
    birthstate = models.CharField(max_length=30,null=True)
    birthcity = models.CharField(max_length= 30,null=True)
    deathyear = models.IntegerField(null=True)
    deathmonth = models.IntegerField(null=True)
    deathday = models.IntegerField(null=True)
    deathcountry=models.CharField(max_length=20,null=True)
    deathstate = models.CharField(max_length=30,null=True)
    deathcity = models.CharField(max_length=30,null=True)
    namefirst=models.CharField(max_length=30,null=True)
    namelast = models.CharField(max_length=30,null=True)
    namegiven = models.CharField(max_length=60,null=True)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    bats = models.CharField(max_length=1,null=True)
    throws = models.CharField(max_length=1,null=True)
    debut = models.CharField(max_length=20,null=True)
    finalgame = models.CharField(max_length=20,null=True)
    retroid = models.CharField(max_length=20,null=True)
    bbrefid=models.CharField(max_length=20,null=True)

class Batting(models.Model):
    def __str__(self):
        return f'{self.yearid}'
    player = models.ForeignKey(Player, on_delete="CASCADE")
    yearid = models.IntegerField(null=True)
    stint = models.IntegerField(null=True)
    teamid = models.CharField(max_length=50,null=True)
    lgid = models.CharField(max_length=10,null=True)
    g=models.IntegerField(null=True)
    ab=models.IntegerField(null=True)
    r=models.IntegerField(null=True)
    h=models.IntegerField(null=True)
    _2b=models.IntegerField(null=True)
    _3b=models.IntegerField(null=True)
    hr=models.IntegerField(null=True)
    rbi=models.IntegerField(null=True)
    sb=models.IntegerField(null=True)
    cs=models.IntegerField(null=True)
    bb=models.IntegerField(null=True)
    so=models.IntegerField(null=True)
    ibb=models.IntegerField(null=True)
    hbp=models.IntegerField(null=True)
    sh=models.IntegerField(null=True)
    sf=models.IntegerField(null=True)
    gidp=models.IntegerField(null=True)

class Pitching(models.Model):
    def __str__(self):
        return f'{self.yearid}'
    player = models.ForeignKey(Player, on_delete="CASCADE")
    yearid = models.IntegerField(null=True)
    stint = models.IntegerField(null=True)
    teamid = models.CharField(max_length=50,null=True)
    lgid = models.CharField(max_length=10,null=True)
    w=models.IntegerField(null=True)
    l=models.IntegerField(null=True)
    g=models.IntegerField(null=True)
    gs=models.IntegerField(null=True)
    cg=models.IntegerField(null=True)
    sho=models.IntegerField(null=True)
    sv=models.IntegerField(null=True)
    ipouts =models.IntegerField(null=True)
    h=models.IntegerField(null=True)
    er=models.IntegerField(null=True)
    hr=models.IntegerField(null=True)
    bb=models.IntegerField(null=True)
    so=models.IntegerField(null=True)
    baopp=models.FloatField(null=True)
    era=models.FloatField(null=True)
    ibb=models.IntegerField(null=True)
    wp=models.IntegerField(null=True)
    hbp=models.IntegerField(null=True)
    bk=models.IntegerField(null=True)
    bfp=models.IntegerField(null=True)
    gf=models.IntegerField(null=True)
    r=models.IntegerField(null=True)
    sh=models.IntegerField(null=True)
    sf=models.IntegerField(null=True)
    gidp=models.IntegerField(null=True)