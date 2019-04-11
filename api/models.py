from django.db import models

# Create your models here.


class APILoan(models.Model):
    u"游戏广告位置"
    name = models.CharField("姓名", max_length=128, null=False, blank=False)
    phone = models.CharField("电话", max_length=13, null=False, blank=False)
    loan_money = models.DecimalField("借款金额(万元)",max_digits=12,decimal_places=4, help_text="单位（万元）")
    create_time = models.DateTimeField("申请时间",auto_now_add=True)

    class Meta:
        db_table = "api_loan"
        verbose_name_plural = "预借款人信息表"
        verbose_name = "预借款人信息表"

    @property
    def list_field(self):
        return ['name', 'phone', 'loan_money', 'create_time']

