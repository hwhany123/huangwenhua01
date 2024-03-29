
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
from django.db import models


class ysb(models.Model):
    xh = models.PositiveBigIntegerField(blank=True, null=True)
    fyxm = models.CharField(primary_key=True, max_length=255)
    lb = models.CharField(max_length=255, blank=True, null=True)
    bhs = models.FloatField(db_column='总额（不含税）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '2023年行政费用预算表'



class kjkmdzb(models.Model):
    aqhbtrfw2 = models.CharField(max_length=255, blank=True, null=True)
    aqhbtrfw = models.CharField(max_length=255, blank=True, null=True)
    aqssfylx = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '会计科目类型对照'


class xsz(models.Model):
    年 = models.IntegerField(blank=True, null=True)
    月= models.IntegerField(blank=True, null=True)
    日 = models.IntegerField(blank=True, null=True)
    凭证号 = models.CharField(max_length=255, blank=True, null=True)
    分录号 = models.IntegerField(blank=True, null=True)
    摘要 = models.CharField(max_length=255, blank=True, null=True)
    科目编码 = models.CharField(max_length=255, blank=True, null=True)
    科目名称 = models.CharField(max_length=255, blank=True, null=True)
    辅助项 = models.CharField(max_length=255, blank=True, null=True)
    币种 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.FloatField(blank=True, null=True)
    借方 = models.FloatField(blank=True, null=True)
    数量1 = models.FloatField(blank=True, null=True)
    贷方 = models.FloatField(blank=True, null=True)
    核销信息 = models.CharField(max_length=255, blank=True, null=True)
    结算信息 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False

        db_table = '序时账'

    def __str__(self):
        # return self.title 将文章标题返回
        return self.摘要


class xjbmdzb(models.Model):
    xh = models.CharField(primary_key=True, max_length=255)
    sybm = models.CharField(max_length=255, blank=True, null=True)
    xbm = models.CharField(max_length=255, blank=True, null=True)
    jbm = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新旧部门对照表'

class xszst(models.Model):
    年 = models.IntegerField(blank=True, null=True)
    月= models.IntegerField(blank=True, null=True)

    凭证号 = models.CharField(max_length=255, blank=True, null=True)



    科目名称 = models.CharField(max_length=255, blank=True, null=True)

    部门 = models.CharField(max_length=255, blank=True, null=True)
    新部门 = models.CharField(max_length=255, blank=True, null=True)
    旧部门 = models.CharField(max_length=255, blank=True, null=True)
    费用 = models.CharField(max_length=255, blank=True, null=True)
    项目 = models.CharField(max_length=255, blank=True, null=True)
    客商 = models.CharField(max_length=255, blank=True, null=True)
    人员 = models.CharField(max_length=255, blank=True, null=True)
    生产商 = models.CharField(max_length=255, blank=True, null=True)
    银行账户 = models.CharField(max_length=255, blank=True, null=True)

    税率 = models.CharField(max_length=255, blank=True, null=True)
    物料名称 = models.CharField(max_length=255, blank=True, null=True)
    成本对象 = models.CharField(max_length=255, blank=True, null=True)

    安全环保投入范围 = models.CharField(max_length=255, blank=True, null=True)
    安全环保投入类型 = models.CharField(max_length=255, blank=True, null=True)

    摘要 = models.CharField(max_length=255, blank=True, null=True)

    借方 = models.FloatField(blank=True, null=True)

    贷方 = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False

        db_table = '序时账视图'

    def __str__(self):
        # return self.title 将文章标题返回
        return str(self.id)

class ys(models.Model):

    序号 = models.FloatField(blank=True, null=True, db_column='序号')
    年 = models.FloatField(blank=True, null=True, db_column='年')
    费用项目 = models.FloatField(blank=True, null=True, db_column='费用项目')
    类别 = models.FloatField(blank=True, null=True, db_column='类别')
    总额不含税 = models.FloatField(blank=True, null=True, db_column='总额（不含税）')
    其中传统口径 = models.FloatField(blank=True, null=True, db_column='其中：传统口径')
    其中用于安全生产 = models.FloatField(blank=True, null=True, db_column='其中：用于安全生产')
    其中用于环境保护 = models.FloatField(blank=True, null=True, db_column='其中：用于环境保护')
    其中研发项目 = models.FloatField(blank=True, null=True, db_column='其中：研发项目')
    其中工程项目资本化 = models.FloatField(blank=True, null=True, db_column='其中：工程项目（资本化）')
    其中农化服务费 = models.FloatField(blank=True, null=True, db_column='其中：农化服务费')
    其中用于知识产权的 = models.FloatField(blank=True, null=True, db_column='其中：用于知识产权的')
    其中用于法治的 = models.FloatField(blank=True, null=True, db_column='其中：用于法治的')
    总额不含税追加 = models.FloatField(blank=True, null=True, db_column='总额（不含税）-追加')
    其中传统口径追加 = models.FloatField(blank=True, null=True, db_column='其中：传统口径-追加')
    其中用于安全生产追加 = models.FloatField(blank=True, null=True, db_column='其中：用于安全生产-追加')
    其中用于环境保护追加 = models.FloatField(blank=True, null=True, db_column='其中：用于环境保护-追加')
    其中研发项目追加 = models.FloatField(blank=True, null=True, db_column='其中：研发项目-追加')
    其中工程项目资本化追加 = models.FloatField(blank=True, null=True, db_column='其中：工程项目（资本化）-追加')
    其中农化服务费追加 = models.FloatField(blank=True, null=True, db_column='其中：农化服务费-追加')
    其中用于知识产权的追加 = models.FloatField(blank=True, null=True, db_column='其中：用于知识产权的-追加')
    其中用于法治的追加 = models.FloatField(blank=True, null=True, db_column='其中：用于法治的-追加')

    class Meta:
        managed = False

        db_table = '2023年行政费用预算表'

    def __str__(self):
        # return self.title 将文章标题返回
        return str(self.id)

