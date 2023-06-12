# Generated by Django 3.1.3 on 2023-06-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kjkmdzb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqhbtrfw2', models.CharField(blank=True, max_length=255, null=True)),
                ('aqhbtrfw', models.CharField(blank=True, max_length=255, null=True)),
                ('aqssfylx', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '会计科目类型对照',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='xjbmdzb',
            fields=[
                ('xh', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sybm', models.CharField(blank=True, max_length=255, null=True)),
                ('xbm', models.CharField(blank=True, max_length=255, null=True)),
                ('jbm', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '新旧部门对照表',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='xsz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('年', models.IntegerField(blank=True, null=True)),
                ('月', models.IntegerField(blank=True, null=True)),
                ('日', models.IntegerField(blank=True, null=True)),
                ('凭证号', models.CharField(blank=True, max_length=255, null=True)),
                ('分录号', models.IntegerField(blank=True, null=True)),
                ('摘要', models.CharField(blank=True, max_length=255, null=True)),
                ('科目编码', models.CharField(blank=True, max_length=255, null=True)),
                ('科目名称', models.CharField(blank=True, max_length=255, null=True)),
                ('辅助项', models.CharField(blank=True, max_length=255, null=True)),
                ('币种', models.CharField(blank=True, max_length=255, null=True)),
                ('数量', models.FloatField(blank=True, null=True)),
                ('借方', models.FloatField(blank=True, null=True)),
                ('数量1', models.FloatField(blank=True, null=True)),
                ('贷方', models.FloatField(blank=True, null=True)),
                ('核销信息', models.CharField(blank=True, max_length=255, null=True)),
                ('结算信息', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '序时账',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='xszst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('年', models.IntegerField(blank=True, null=True)),
                ('月', models.IntegerField(blank=True, null=True)),
                ('凭证号', models.CharField(blank=True, max_length=255, null=True)),
                ('科目名称', models.CharField(blank=True, max_length=255, null=True)),
                ('部门', models.CharField(blank=True, max_length=255, null=True)),
                ('新部门', models.CharField(blank=True, max_length=255, null=True)),
                ('旧部门', models.CharField(blank=True, max_length=255, null=True)),
                ('费用', models.CharField(blank=True, max_length=255, null=True)),
                ('项目', models.CharField(blank=True, max_length=255, null=True)),
                ('客商', models.CharField(blank=True, max_length=255, null=True)),
                ('人员', models.CharField(blank=True, max_length=255, null=True)),
                ('生产商', models.CharField(blank=True, max_length=255, null=True)),
                ('银行账户', models.CharField(blank=True, max_length=255, null=True)),
                ('税率', models.CharField(blank=True, max_length=255, null=True)),
                ('物料名称', models.CharField(blank=True, max_length=255, null=True)),
                ('成本对象', models.CharField(blank=True, max_length=255, null=True)),
                ('安全环保投入范围', models.CharField(blank=True, max_length=255, null=True)),
                ('安全环保投入类型', models.CharField(blank=True, max_length=255, null=True)),
                ('摘要', models.CharField(blank=True, max_length=255, null=True)),
                ('借方', models.FloatField(blank=True, null=True)),
                ('贷方', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': '序时账视图',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ysb',
            fields=[
                ('xh', models.PositiveBigIntegerField(blank=True, null=True)),
                ('fyxm', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('lb', models.CharField(blank=True, max_length=255, null=True)),
                ('bhs', models.FloatField(blank=True, db_column='总额（不含税）', null=True)),
            ],
            options={
                'db_table': '2023年行政费用预算表',
                'managed': False,
            },
        ),
    ]