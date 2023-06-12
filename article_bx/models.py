from django.db import models
from django.db.models import JSONField

class bx_clbx(models.Model):
    id = models.AutoField(primary_key=True)

    报销人= models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    是否享受车改=models.BooleanField(default=False)
    是否公派车辆=models.BooleanField(default=False)
    事由= models.CharField(max_length=255, blank=True, null=True)
    行项目=JSONField()
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = '差旅报销'