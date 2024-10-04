from django.core.validators import URLValidator
from django.db import models
from  django.contrib.auth.models import User


class PanelInfo(models.Model):
    url_panel = models.URLField(validators=[URLValidator(schemes=['http', 'https'])],null=False,blank=False)
    name_panel = models.CharField(null=False,blank=False,max_length=100)
    username = models.CharField(null=False,blank=False,max_length=100)
    password = models.CharField(null=False,blank=False,max_length=100)
    inbound = models.JSONField(null=True)
    proxies = models.JSONField(null=True)

    class Meta:
        unique_together = ['name_panel']

class UserAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    limit_volume = models.FloatField(null=True,blank=False)
    limit_user = models.IntegerField(null=True,blank=True)

class Account_agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    panel = models.ForeignKey(PanelInfo, on_delete=models.CASCADE)
    username = models.CharField(null=False,blank=False,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    volume = models.FloatField(null=False,blank=False)
    time = models.IntegerField(null=False,blank=False)
    class Meta:
        unique_together = ['username']

class Log_UserAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    change_at = models.DateTimeField(auto_now_add=True)
    log_info = models.TextField(null=False,blank=False)