from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User
from django.utils import timezone

class bx_clbx(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles_bx'
    )
    id = models.AutoField(primary_key=True)

    报销人= models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    是否享受车改=models.BooleanField(default=False)
    是否公派车辆=models.BooleanField(default=False)
    事由= models.CharField(max_length=255, blank=True, null=True)
    行项目=JSONField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = '差旅报销'