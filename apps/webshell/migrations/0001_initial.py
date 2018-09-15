# Generated by Django 2.1.1 on 2018-09-15 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadlockCommand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('command', models.CharField(default='', max_length=1024, verbose_name='pt-deadlock-logger命令')),
                ('schema_id', models.CharField(default='', max_length=128, verbose_name='关联MysqlSchemaInfo的id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '死锁命令表',
                'verbose_name_plural': '死锁命令表',
                'db_table': 'sqlaudit_deadlock_command',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='DeadlockRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('server', models.CharField(max_length=20)),
                ('ts', models.DateTimeField(auto_now=True)),
                ('thread', models.IntegerField()),
                ('txn_id', models.CharField(max_length=1024)),
                ('txn_time', models.PositiveSmallIntegerField()),
                ('user', models.CharField(max_length=16)),
                ('hostname', models.CharField(max_length=20)),
                ('ip', models.CharField(max_length=15)),
                ('db', models.CharField(max_length=64)),
                ('tbl', models.CharField(max_length=64)),
                ('idx', models.CharField(max_length=64)),
                ('lock_type', models.CharField(max_length=16)),
                ('lock_mode', models.CharField(max_length=1)),
                ('wait_hold', models.CharField(max_length=1)),
                ('victim', models.SmallIntegerField()),
                ('query', models.TextField()),
                ('is_pull', models.SmallIntegerField(default=0, verbose_name='是否已推送，0：未推送，1：已推送')),
            ],
            options={
                'verbose_name': '死锁采集记录表,pt-deadlock-logger工具采集',
                'verbose_name_plural': '死锁采集记录表,pt-deadlock-logger工具采集',
                'db_table': 'sqlaudit_deadlocks_records',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WebShellGrant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'webshell授权',
                'verbose_name_plural': 'webshell授权',
                'db_table': 'sqlaudit_web_shell_grant',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WebShellInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('command', models.CharField(default='', max_length=1024, verbose_name='命令')),
                ('comment', models.CharField(max_length=128, null=True, verbose_name='描述')),
                ('envi_id', models.IntegerField(choices=[(1, '生产环境'), (2, '测试环境')], verbose_name='环境')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'webshell',
                'verbose_name_plural': 'webshell',
                'db_table': 'sqlaudit_web_shell',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='WebShellOpLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('user', models.CharField(default='', max_length=128, verbose_name='操作用户')),
                ('session_id', models.CharField(default='', max_length=128, verbose_name='会话id')),
                ('op_cmd', models.CharField(default='', max_length=4096, null=True, verbose_name='操作的命令')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'web shell操作记录表',
                'verbose_name_plural': 'web shell操作记录表',
                'db_table': 'sqlaudit_web_shell_oplog',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='webshellinfo',
            unique_together={('comment',)},
        ),
        migrations.AddField(
            model_name='webshellgrant',
            name='shell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webshell.WebShellInfo'),
        ),
        migrations.AddField(
            model_name='webshellgrant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='deadlockrecord',
            unique_together={('server', 'ts', 'thread')},
        ),
        migrations.AlterUniqueTogether(
            name='webshellgrant',
            unique_together={('user', 'shell')},
        ),
    ]
