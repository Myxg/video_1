from django.db import models
from django.utils.timezone import now

# Create your models here.


class form_ShiPin_Report(models.Model):
    objects = None


    ID = models.CharField(max_length=32)
    Dropdown_BiSaiJieGuo = models.CharField(max_length=32)
    Date_field_BiSaiRiQi = models.CharField(max_length=32)
    Url = models.TextField(max_length=1000)
    Query_SaiShiMingCheng_ID = models.CharField(max_length=100)
    form_YunDongYuan_B1_ID = models.CharField(max_length=128)
    form_YunDongYuan_B2_ID = models.CharField(max_length=32)
    Single_Line_ShiPinMingCheng = models.CharField(max_length=255)
    Query_SaiShiMingCheng = models.CharField(max_length=100)
    Formula_InputTimDate = models.CharField(max_length=100)
    Dropdown_BiSaiXiangMu = models.CharField(max_length=32)
    Dropdown_LunCi = models.CharField(max_length=32)
    form_YunDongYuan_ShengLi_2 = models.CharField(max_length=32)
    Dropdown_QueShi = models.CharField(max_length=32)
    form_YunDongYuan_A2 = models.CharField(max_length=32)
    form_YunDongYuan_ShengLi_1 = models.CharField(max_length=32)
    form_YunDongYuan_A1 = models.CharField(max_length=32)
    form_YunDongYuan_B2 = models.CharField(max_length=32)
    form_YunDongYuan_B1 = models.CharField(max_length=32)
    form_YunDongYuan_A1_ID = models.CharField(max_length=32)
    form_YunDongYuan_A2_ID = models.CharField(max_length=32)
    Single_Line_BiFen = models.CharField(max_length=32)
    Added_Time = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'form_ShiPin_Report'