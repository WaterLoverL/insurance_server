from django.db import models

from django.contrib.auth.models import User


class PolicyHolder(models.Model):
    ID_TYPES = (
        (1, '身份证'),
        (2, '护照')
    )
    SEX_TYPES = (
        (1, '男'),
        (2, '女'),
    )
    NameA = models.CharField(max_length=18, verbose_name='姓名')
    IdTypeA = models.SmallIntegerField(choices=ID_TYPES, default=1, verbose_name='证件类型')
    IDCardNumA = models.CharField(max_length=32, verbose_name='证件号码')
    cardNum = models.CharField(max_length=18, verbose_name='卡号', null=True, blank=True)
    pwd = models.CharField(max_length=88, verbose_name='密码', null=True, blank=True)
    SexA = models.SmallIntegerField(choices=SEX_TYPES,default=1,verbose_name='性别')
    BirthA = models.DateField(verbose_name='出生日期')
    spanAgeA = models.IntegerField(verbose_name='本卡生效时年龄')
    EMailA = models.EmailField(max_length=254, verbose_name='电子邮件')
    PhoneA = models.CharField(max_length=11, verbose_name='手机号码')
    AddrA = models.CharField(max_length=120, verbose_name='联系地址')
    RelashipE = models.BooleanField(default=True, verbose_name='是投保人')
    NameE = models.CharField(max_length=18, verbose_name='被保人姓名')
    IdTypeE = models.SmallIntegerField(choices=ID_TYPES, default=1, verbose_name='被保人证件类型')
    IDCardNumE = models.CharField(max_length=32, verbose_name='被保人证件号码')
    SexE = models.SmallIntegerField(choices=SEX_TYPES, default=1, verbose_name='被保人性别')
    BirthE = models.DateField(verbose_name='被保人出生日期')
    spanAgeE = models.IntegerField(verbose_name='被保人本卡生效时年龄')
    EMailE = models.EmailField(max_length=254, verbose_name='被保人电子邮件')
    PhoneE = models.CharField(max_length=11, verbose_name='被保人手机号码')
    AddrE = models.CharField(max_length=120, verbose_name='被保人联系地址')
    TEDT0A = models.DateField(verbose_name='生效日期')

    def __str__(self):
        return self.NameA


class Insurance(models.Model):
    CaseStatus = (
        (1, '完成'),
        (2, '正在处理'),
        (3, '未完成')
    )
    address = models.CharField(max_length=255, verbose_name='住址')
    TEDT0A = models.DateTimeField(verbose_name='生效时间')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='出险时间')
    reason = models.TextField(verbose_name='事故原因')
    apply_type= models.CharField(max_length=50,verbose_name='申请类别')
    maimlist = models.CharField(max_length=18,verbose_name='伤残等级')
    money = models.FloatField(verbose_name='发票金额')
    compensate = models.FloatField(verbose_name='第三方赔付')
    to_letter = models.CharField(max_length=18,verbose_name='交件人')
    from_letter = models.CharField(max_length=255,verbose_name='收件人')
    receipt_time = models.DateTimeField(verbose_name='收件时间')
    bank = models.CharField(max_length=255,verbose_name='银行')
    bank_account = models.CharField(max_length=32, verbose_name='银行账号')
    reparations = models.FloatField(verbose_name='赔款')
    payee = models.CharField(max_length=255,verbose_name='领款人')
    finishedtime = models.DateTimeField(verbose_name='完成日期')
    amount = models.SmallIntegerField(verbose_name='数量')
    transfer_accounts = models.CharField(max_length=255,verbose_name='转账')
    case_status = models.SmallIntegerField(choices=CaseStatus, verbose_name='案件状态')
    organization = models.CharField(max_length=255,verbose_name='机构')
    file_status = models.SmallIntegerField(choices=CaseStatus, verbose_name='资料状态')
    comment1 = models.TextField(verbose_name='备注1')
    comment2 = models.TextField(verbose_name='备注2')
    case_info = models.CharField(max_length=255,verbose_name='案件处理')
    other_reason = models.CharField(max_length=255,verbose_name='退案拒赔及原因')
    status = models.SmallIntegerField(choices=CaseStatus, verbose_name='状态')

    def __str__(self):
        return self.payee

