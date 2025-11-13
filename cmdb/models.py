from django.db import models,migrations
class host(models.Model):
    hostname = models.CharField(max_length=255,unique=True,verbose_name="主机名",blank=False)
    ip = models.GenericIPAddressField(verbose_name="IP地址",blank=False)
    disk = models.CharField(max_length=255,null=True,verbose_name="磁盘",blank=True)
    cpu = models.CharField(max_length=255,null=True,verbose_name="CPU",blank=True)
    mem = models.CharField(max_length=255,null=True,verbose_name="内存",blank=True)
    desc = models.CharField(max_length=255,null=True,verbose_name="描述",blank=True)

    def __str__(self):
        return self.hostname
# Create your models here.