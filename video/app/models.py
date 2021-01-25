from django.db import models
from django.utils.timezone import now

# Create your models here.


# class form_ShiPin_Report(models.Model):
#     objects = None
#     ID = models.CharField(max_length=32, primary_key=True)
#     Dropdown_BiSaiJieGuo = models.CharField(max_length=32)
#     Date_field_BiSaiRiQi = models.CharField(max_length=32)
#     Url = models.TextField(max_length=1000)
#     Query_SaiShiMingCheng_ID = models.CharField(max_length=100)
#     form_YunDongYuan_B1_ID = models.CharField(max_length=128)
#     form_YunDongYuan_B2_ID = models.CharField(max_length=32)
#     Single_Line_ShiPinMingCheng = models.CharField(max_length=255)
#     Query_SaiShiMingCheng = models.CharField(max_length=100)
#     Formula_InputTimDate = models.CharField(max_length=100)
#     Dropdown_BiSaiXiangMu = models.CharField(max_length=32)
#     Dropdown_LunCi = models.CharField(max_length=32)
#     form_YunDongYuan_ShengLi_2 = models.CharField(max_length=32)
#     Dropdown_QueShi = models.CharField(max_length=32)
#     form_YunDongYuan_A2 = models.CharField(max_length=32)
#     form_YunDongYuan_ShengLi_1 = models.CharField(max_length=32)
#     form_YunDongYuan_A1 = models.CharField(max_length=32)
#     form_YunDongYuan_B2 = models.CharField(max_length=32)
#     form_YunDongYuan_B1 = models.CharField(max_length=32)
#     form_YunDongYuan_A1_ID = models.CharField(max_length=32)
#     form_YunDongYuan_A2_ID = models.CharField(max_length=32)
#     Single_Line_BiFen = models.CharField(max_length=32)
#     Added_Time = models.CharField(max_length=32)
#
#     class Meta:
#         managed = False
#         db_table = 'form_ShiPin_Report'
#
#
# class form_PaiMing(models.Model):
#     objects = None
#     ID = models.CharField(max_length=255, primary_key=True)
#     form_YunDongYuan = models.CharField(max_length=255)
#     form_YunDongYuan_ID = models.CharField(max_length=255)
#     Dropdown_BiSaiXiangMu = models.TextField(max_length=255)
#     Date_field_PaiMingRiQi = models.CharField(max_length=255)
#     Formula_RiQi = models.CharField(max_length=255)
#     Dropdown_PaiMingFenLei = models.CharField(max_length=255)
#     Number_PaiMing = models.CharField(max_length=255)
#     Number_PaiMingBianHua = models.CharField(max_length=255)
#     Number_Ying = models.CharField(max_length=255)
#     Number_Shu = models.CharField(max_length=255)
#     Number_JiFen = models.CharField(max_length=255)
#     Number_CanSaiZhanShu = models.CharField(max_length=255)
#
#
#     class Meta:
#         managed = False
#         db_table = 'form_PaiMing'


class video_user(models.Model):
    objects = None
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'video_user'

class file_list(models.Model):
    objects = None
    file_name = models.CharField(max_length=128)
    file_class = models.CharField(max_length=64)
    upload_user = models.CharField(max_length=64)
    upload_DATE = models.DateField(max_length=64)
    status = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'file_list'

# class player_list(models.Model):
#     objects = None
#     player_name = models.CharField(max_length=128)
#     photo = models.CharField(max_length=128)
#     project = models.CharField(max_length=128)
#
#     class Meta:
#         managed = True
#         db_table = 'player_list'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fms(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshiriqi = models.CharField(db_column='Date_field_CeShiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_guilei = models.CharField(db_column='Dropdown_GuiLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_dongzuo = models.CharField(db_column='Dropdown_DongZuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_pingfen = models.CharField(db_column='Number_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMS'


class ShenglvDanda(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_single_line_zhongwenming = models.CharField(db_column='form_YunDongYuan_Single_Line_ZhongWenMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_8 = models.CharField(db_column='form_YunDongYuan_8', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_8_single_line_zhongwenming = models.CharField(db_column='form_YunDongYuan_8_Single_Line_ZhongWenMing', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number_zongchangci = models.CharField(db_column='Number_ZongChangCi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    percent_shenglv = models.CharField(db_column='Percent_ShengLv', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_1 = models.CharField(db_column='form_SaiShi_1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_1 = models.TextField(db_column='URL_1', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_1 = models.CharField(db_column='Single_Line_BiFen_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_2 = models.CharField(db_column='form_SaiShi_2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_2 = models.TextField(db_column='URL_2', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_2 = models.CharField(db_column='Single_Line_BiFen_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_3 = models.CharField(db_column='form_SaiShi_3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_3 = models.TextField(db_column='URL_3', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_3 = models.CharField(db_column='Single_Line_BiFen_3', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShengLv_DanDa'


class ShenglvZuhe(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_shuangdazuhe_zhongguo = models.CharField(db_column='form_ShuangDaZuHe_ZhongGuo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_zhongguo_single_line1 = models.CharField(db_column='form_ShuangDaZuHe_ZhongGuo_Single_Line1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_8 = models.CharField(db_column='form_ShuangDaZuHe_8', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_8_single_line1 = models.CharField(db_column='form_ShuangDaZuHe_8_Single_Line1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number_zongchangci = models.CharField(db_column='Number_ZongChangCi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    percent_shenglv = models.CharField(db_column='Percent_ShengLv', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_1 = models.CharField(db_column='form_SaiShi_1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_1 = models.TextField(db_column='URL_1', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_1 = models.CharField(db_column='Single_Line_BiFen_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_2 = models.CharField(db_column='form_SaiShi_2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_2 = models.TextField(db_column='URL_2', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_2 = models.CharField(db_column='Single_Line_BiFen_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi_3 = models.CharField(db_column='form_SaiShi_3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    url_3 = models.TextField(db_column='URL_3', blank=True, null=True)  # Field name made lowercase.
    single_line_bifen_3 = models.CharField(db_column='Single_Line_BiFen_3', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShengLv_ZuHe'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Form(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_jiguan = models.CharField(db_column='Single_Line_JiGuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_minzu = models.CharField(db_column='Single_Line_MinZu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_yundongdengji = models.CharField(db_column='Dropdown_YunDongDengJi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_kaishixunlian = models.CharField(db_column='Date_field_KaiShiXunLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_qimengjiaolian = models.CharField(db_column='Single_Line_QiMengJiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_shengduijiaolian = models.CharField(db_column='Single_Line_ShengDuiJiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_guojiaduijiaolian = models.CharField(db_column='Single_Line_GuoJiaDuiJiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_laiyuandanwei = models.CharField(db_column='form_LaiYuanDanWei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    rich_text_rongyu = models.TextField(db_column='Rich_Text_RongYu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form'


class Form3000M(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_3000M'


class Form30M(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_30M'


class Form4000M(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_4000M'


class Form400Mx5(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_dropdown_xingbie = models.CharField(db_column='form_YunDongYuan_Dropdown_XingBie', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_1 = models.CharField(db_column='Decimal_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_2 = models.CharField(db_column='Decimal_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_3 = models.CharField(db_column='Decimal_3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_4 = models.CharField(db_column='Decimal_4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_5 = models.CharField(db_column='Decimal_5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingjunchengji = models.CharField(db_column='Formula_PingJunChengJi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_400Mx5'


class Form5000M(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_5000M'


class FormBmi(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_checkbox_yundongxiangmu = models.CharField(db_column='form_YunDongYuan_Checkbox_YunDongXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshiriqi = models.CharField(db_column='Date_field_CeShiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_shengao = models.CharField(db_column='Decimal_ShenGao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_tizhong = models.CharField(db_column='Decimal_TiZhong', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_pingfen = models.CharField(db_column='Number_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_BMI'


class FormBeijinaili(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_BeiJiNaiLi'


class FormBisaijieguoDanda(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi = models.CharField(db_column='form_SaiShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_lunci = models.CharField(db_column='Dropdown_LunCi', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date_field_bisairiqi = models.CharField(db_column='Date_field_BiSaiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a2 = models.CharField(db_column='form_YunDongYuan_A2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b1 = models.CharField(db_column='form_YunDongYuan_B1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_huosheng = models.CharField(db_column='form_YunDongYuan_HuoSheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaijieguo = models.CharField(db_column='Dropdown_BiSaiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_bifen = models.CharField(db_column='Single_Line_BiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_shipin = models.CharField(db_column='form_ShiPin', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_BiSaiJieGuo_DanDa'


class FormBisaijieguoShuangda(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishi = models.CharField(db_column='form_SaiShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_lunci = models.CharField(db_column='Dropdown_LunCi', max_length=64, blank=True, null=True)  # Field name made lowercase.
    date_field_bisairiqi = models.CharField(db_column='Date_field_BiSaiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_a = models.CharField(db_column='form_ShuangDaZuHe_A', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_b1 = models.CharField(db_column='form_ShuangDaZuHe_B1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_shengli = models.CharField(db_column='form_ShuangDaZuHe_ShengLi', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaijieguo = models.CharField(db_column='Dropdown_BiSaiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_bifen = models.CharField(db_column='Single_Line_BiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_shipin = models.CharField(db_column='form_ShiPin', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_BiSaiJieGuo_ShuangDa'


class FormChuizhizongtiao(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ChuiZhiZongTiao'


class FormDiqu(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_diqu = models.CharField(db_column='Single_Line_DiQu', max_length=64, blank=True, null=True)  # Field name made lowercase.
    image_qizhi = models.TextField(db_column='Image_QiZhi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_DiQu'


class FormFujinaili(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_FuJiNaiLi'


class FormJifen(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_nian = models.CharField(db_column='Number_Nian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_zhou = models.CharField(db_column='Number_Zhou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    query_saishi = models.CharField(db_column='Query_SaiShi', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dropdown_xiangmu = models.CharField(db_column='Dropdown_XiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_mingci = models.CharField(db_column='Dropdown_MingCi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_JiFen'


class FormKecheng(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_mingcheng = models.CharField(db_column='Single_Line_MingCheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_jieshao = models.CharField(db_column='Multi_Line_JieShao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_fenlei = models.CharField(db_column='Dropdown_FenLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_xunlianliang = models.CharField(db_column='Dropdown_XunLianLiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subform_single_line_jieduan = models.CharField(db_column='SubForm_Single_Line_JieDuan', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_KeCheng'


class FormLaiyuandanwei(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_mingcheng = models.CharField(db_column='Single_Line_MingCheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_LaiYuanDanWei'


class FormLidingtiaoyuan(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_LiDingTiaoYuan'


class FormPaiming(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_paimingriqi = models.CharField(db_column='Date_field_PaiMingRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_riqi = models.CharField(db_column='Formula_RiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_paimingfenlei = models.CharField(db_column='Dropdown_PaiMingFenLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paiming = models.CharField(db_column='Number_PaiMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paimingbianhua = models.CharField(db_column='Number_PaiMingBianHua', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_cansaizhanshu = models.CharField(db_column='Number_CanSaiZhanShu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_PaiMing'


class FormSaishi(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    image_logo = models.CharField(db_column='Image_LOGO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_saishizhongwenming = models.CharField(db_column='Single_Line_SaiShiZhongWenMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_saishiyingwenming = models.CharField(db_column='Single_Line_SaiShiYingWenMing', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dropdown_saishijibie = models.CharField(db_column='Dropdown_SaiShiJiBie', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_kaishiriqi = models.CharField(db_column='Date_field_KaiShiRiQi', max_length=128, blank=True, null=True)  # Field name made lowercase.
    date_field_jieshuriqi = models.CharField(db_column='Date_field_JieShuRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_diqu = models.CharField(db_column='form_DiQu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_diqu_single_line_diqu = models.CharField(db_column='form_DiQu_Single_Line_DiQu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_chengshi = models.CharField(db_column='Single_Line_ChengShi', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_SaiShi'


class FormShendun60Kg(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ceshijieguo = models.CharField(db_column='Number_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShenDun_60KG'


class FormShendun90Kg(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ceshijieguo = models.CharField(db_column='Number_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShenDun_90KG'


class FormShendunMax(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ceshijieguo = models.CharField(db_column='Number_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_xiangduililiang = models.CharField(db_column='Decimal_XiangDuiLiLiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShenDun_MAX'


class FormShenglishenghua(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshiriqi = models.CharField(db_column='Date_field_CeShiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_ceshixiangmu = models.CharField(db_column='Formula_CeShiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShengLiShengHua'


class FormShijiepaimingDandaZuixin(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_paimingriqi = models.CharField(db_column='Date_field_PaiMingRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_riqi = models.CharField(db_column='Formula_RiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_paimingfenlei = models.CharField(db_column='Dropdown_PaiMingFenLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paiming = models.CharField(db_column='Number_PaiMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paimingbianhua = models.CharField(db_column='Number_PaiMingBianHua', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_cansaizhanshu = models.CharField(db_column='Number_CanSaiZhanShu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShiJiePaiMing_DanDa_ZuiXin'


class FormShijiepaimingShuangdaZuixin(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_shuangdazuhe = models.CharField(db_column='form_ShuangDaZuHe', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_id = models.CharField(db_column='form_ShuangDaZuHe_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_single_line_mingcheng = models.CharField(db_column='form_ShuangDaZuHe_Single_Line_MingCheng', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_form_zuzhijiagou = models.CharField(db_column='form_ShuangDaZuHe_form_ZuZhiJiaGou', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_formula_zuzhijiagou = models.CharField(db_column='form_ShuangDaZuHe_Formula_ZuZhiJiaGou', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_paimingriqi = models.CharField(db_column='Date_field_PaiMingRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_riqi = models.CharField(db_column='Formula_RiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_paimingfenlei = models.CharField(db_column='Dropdown_PaiMingFenLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paiming = models.CharField(db_column='Number_PaiMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paimingbianhua = models.CharField(db_column='Number_PaiMingBianHua', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_cansaizhanshu = models.CharField(db_column='Number_CanSaiZhanShu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShiJiePaiMing_ShuangDa_ZuiXin'


class FormShipinReport(models.Model):
    id = models.CharField(db_column='ID', max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    dropdown_bisaijieguo = models.CharField(db_column='Dropdown_BiSaiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_bisairiqi = models.CharField(db_column='Date_field_BiSaiRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.
    query_saishimingcheng_id = models.CharField(db_column='Query_SaiShiMingCheng_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b1_id = models.CharField(db_column='form_YunDongYuan_B1_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b2_id = models.CharField(db_column='form_YunDongYuan_B2_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_shipinmingcheng = models.CharField(db_column='Single_Line_ShiPinMingCheng', max_length=255, blank=True, null=True)  # Field name made lowercase.
    query_saishimingcheng = models.CharField(db_column='Query_SaiShiMingCheng', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formula_inputtimdate = models.CharField(db_column='Formula_InputTimDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_lunci = models.CharField(db_column='Dropdown_LunCi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_shengli_2 = models.CharField(db_column='form_YunDongYuan_ShengLi_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_queshi = models.CharField(db_column='Dropdown_QueShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a2 = models.CharField(db_column='form_YunDongYuan_A2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_shengli_1 = models.CharField(db_column='form_YunDongYuan_ShengLi_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a1 = models.CharField(db_column='form_YunDongYuan_A1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b2 = models.CharField(db_column='form_YunDongYuan_B2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b1 = models.CharField(db_column='form_YunDongYuan_B1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a1_id = models.CharField(db_column='form_YunDongYuan_A1_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a2_id = models.CharField(db_column='form_YunDongYuan_A2_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_bifen = models.CharField(db_column='Single_Line_BiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    added_time = models.CharField(db_column='Added_Time', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShiPin_Report'


class FormShuangdazuhe(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_mingcheng = models.CharField(db_column='Single_Line_MingCheng', max_length=64, blank=True, null=True)  # Field name made lowercase.
    single_line1 = models.CharField(db_column='Single_Line1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dropdown_xiangmu = models.CharField(db_column='Dropdown_XiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a = models.CharField(db_column='form_YunDongYuan_A', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_a_id = models.CharField(db_column='form_YunDongYuan_A_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b = models.CharField(db_column='form_YunDongYuan_B', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_b_id = models.CharField(db_column='form_YunDongYuan_B_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_diqu = models.CharField(db_column='form_DiQu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou = models.CharField(db_column='form_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou_id = models.CharField(db_column='form_ZuZhiJiaGou_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_zuzhijiagou = models.CharField(db_column='Formula_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShuangDaZuHe'


class FormShuangdazuhejifen(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_shuangdazuhe = models.CharField(db_column='form_ShuangDaZuHe', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_single_line_mingcheng = models.CharField(db_column='form_ShuangDaZuHe_Single_Line_MingCheng', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number_nian = models.CharField(db_column='Number_Nian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_zhou = models.CharField(db_column='Number_Zhou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_saishimingcheng = models.CharField(db_column='form_SaiShiMingCheng', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_mingci = models.CharField(db_column='Dropdown_MingCi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShuangDaZuHeJiFen'


class FormShuangdazuhepaiming(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_shuangdazuhe = models.CharField(db_column='form_ShuangDaZuHe', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_single_line_mingcheng = models.CharField(db_column='form_ShuangDaZuHe_Single_Line_MingCheng', max_length=64, blank=True, null=True)  # Field name made lowercase.
    form_shuangdazuhe_single_line1 = models.CharField(db_column='form_ShuangDaZuHe_Single_Line1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dropdown_bisaixiangmu = models.CharField(db_column='Dropdown_BiSaiXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_paimingriqi = models.CharField(db_column='Date_field_PaiMingRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_riqi = models.CharField(db_column='Formula_RiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_paimingfenlei = models.CharField(db_column='Dropdown_PaiMingFenLei', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paiming = models.CharField(db_column='Number_PaiMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_paimingbianhua = models.CharField(db_column='Number_PaiMingBianHua', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ying = models.CharField(db_column='Number_Ying', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shu = models.CharField(db_column='Number_Shu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_jifen = models.CharField(db_column='Number_JiFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_cansaizhanshu = models.CharField(db_column='Number_CanSaiZhanShu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShuangDaZuHePaiMing'


class FormShuangyao1500(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ShuangYao_1500'


class FormSijiaopao20(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_SiJiaoPao_20'


class FormWotuiMax(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_xiangduililiang = models.CharField(db_column='Decimal_XiangDuiLiLiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_WoTui_MAX'


class FormXunlianjihua(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    date_field_xunlianri = models.CharField(db_column='Date_field_XunLianRi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    time_kaishi = models.CharField(db_column='Time_KaiShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    time_jieshu = models.CharField(db_column='Time_JieShu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zhiyuan_zhujiaolian = models.CharField(db_column='form_ZhiYuan_ZhuJiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zhiyuan_jiaolianzu = models.CharField(db_column='form_ZhiYuan_JiaoLianZu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou = models.CharField(db_column='form_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_zuzhijiagou = models.CharField(db_column='Formula_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_biangeng = models.CharField(db_column='Dropdown_BianGeng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_kecheng = models.CharField(db_column='form_KeCheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_zhuangtai = models.CharField(db_column='Dropdown_ZhuangTai', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_biangengyuanyin = models.CharField(db_column='Single_Line_BianGengYuanYin', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_yingdao = models.CharField(db_column='Number_YingDao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shidao = models.CharField(db_column='Number_ShiDao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_shijia = models.CharField(db_column='Number_ShiJia', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_bingjia = models.CharField(db_column='Number_BingJia', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_zhiliang = models.CharField(db_column='Dropdown_ZhiLiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_XunLianJiHua'


class FormXunlianliang(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_zuzhijiagou = models.CharField(db_column='Formula_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_xunlianriqi = models.CharField(db_column='Date_field_XunLianRiQi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_xunliankemu = models.CharField(db_column='Dropdown_XunLianKeMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xunlianshichang = models.CharField(db_column='Number_XunLianShiChang', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_XunLianLiang'


class FormYintixiangshang(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_ceshijieguo = models.CharField(db_column='Number_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_YinTiXiangShang'


class FormYonghu(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_yonghuming = models.CharField(db_column='Single_Line_YongHuMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_dianhuahaoma = models.CharField(db_column='Single_Line_DianHuaHaoMa', max_length=32, blank=True, null=True)  # Field name made lowercase.
    query_yundongyuan = models.CharField(db_column='Query_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    query_yundongyuan_id = models.CharField(db_column='Query_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_juese = models.CharField(db_column='Dropdown_JueSe', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_jiaolian = models.CharField(db_column='form_JiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_jiaolian_id = models.CharField(db_column='form_JiaoLian_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=32, blank=True, null=True)
    date_joined = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_YongHu'


class FormYuandierjitiaoYou(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_YuanDiErJiTiao_You'


class FormYuandierjitiaoZuo(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_YuanDiErJiTiao_Zuo'


class FormYundongyuanReport(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_zhongwenming = models.CharField(db_column='Single_Line_ZhongWenMing', max_length=64, blank=True, null=True)  # Field name made lowercase.
    single_line_yingwenming = models.CharField(db_column='Single_Line_YingWenMing', max_length=64, blank=True, null=True)  # Field name made lowercase.
    image_touxiang = models.TextField(db_column='Image_TouXiang', blank=True, null=True)  # Field name made lowercase.
    checkbox_yundongxiangmu = models.CharField(db_column='Checkbox_YunDongXiangMu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_chipaishou = models.CharField(db_column='Dropdown_ChiPaiShou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_xingbie = models.CharField(db_column='Dropdown_XingBie', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_chusheng = models.CharField(db_column='Date_field_ChuSheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_diqu = models.CharField(db_column='form_DiQu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    radio_guojiaduichengyuan = models.CharField(db_column='Radio_GuoJiaDuiChengYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou = models.CharField(db_column='form_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou_id = models.CharField(db_column='form_ZuZhiJiaGou_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_zuzhijiagou = models.CharField(db_column='Formula_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_menhuyonghuming = models.CharField(db_column='Single_Line_MenHuYongHuMing', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_YunDongYuan_Report'


class FormZhiyuan(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    image_touxiang = models.CharField(db_column='Image_TouXiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_xingming = models.CharField(db_column='Single_Line_XingMing', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_zhiwu = models.CharField(db_column='Dropdown_ZhiWu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_jianjie = models.CharField(db_column='Single_Line_JianJie', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou = models.CharField(db_column='form_ZuZhiJiaGou', max_length=255, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou_id = models.CharField(db_column='form_ZuZhiJiaGou_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ZhiYuan'


class FormZhoujihua(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    date_field_kaishi = models.CharField(db_column='Date_field_KaiShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_jieshu = models.CharField(db_column='Date_field_JieShu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zuzhijiagou = models.CharField(db_column='form_ZuZhiJiaGou', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zhiyuan_zhujiaolian = models.CharField(db_column='form_ZhiYuan_ZhuJiaoLian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_zhiyuan_jiaolianzu = models.CharField(db_column='form_ZhiYuan_JiaoLianZu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_zhidaosixiang = models.TextField(db_column='Single_Line_ZhiDaoSiXiang', blank=True, null=True)  # Field name made lowercase.
    single_line_yaoqiujimudi = models.TextField(db_column='Single_Line_YaoQiuJiMuDi', blank=True, null=True)  # Field name made lowercase.
    number_keshi = models.CharField(db_column='Number_KeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_cishu = models.CharField(db_column='Number_CiShu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_jishu = models.CharField(db_column='Dropdown_JiShu', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_liliangshenti = models.CharField(db_column='Dropdown_LiLiangShenTi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_zhuanxiangtineng = models.CharField(db_column='Dropdown_ZhuanXiangTiNeng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_yundongliang = models.CharField(db_column='Dropdown_YunDongLiang', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_qiangdu = models.CharField(db_column='Dropdown_QiangDu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ZhouJiHua'


class FormZuzhijiagou(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    single_line_mingcheng = models.CharField(db_column='Single_Line_MingCheng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_suoxie = models.CharField(db_column='Single_Line_SuoXie', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ZuZhiJiaGou'


class FormZuoweitiqianqu(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=32, blank=True, primary_key=True)  # Field name made lowercase.
    form_yundongyuan = models.CharField(db_column='form_YunDongYuan', max_length=32, blank=True, null=True)  # Field name made lowercase.
    form_yundongyuan_id = models.CharField(db_column='form_YunDongYuan_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    date_field_ceshi = models.CharField(db_column='Date_field_CeShi', max_length=32, blank=True, null=True)  # Field name made lowercase.
    single_line_ceshididian = models.CharField(db_column='Single_Line_CeShiDiDian', max_length=32, blank=True, null=True)  # Field name made lowercase.
    decimal_ceshijieguo = models.CharField(db_column='Decimal_CeShiJieGuo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number_xintiao = models.CharField(db_column='Number_XinTiao', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dropdown_pingfen = models.CharField(db_column='Dropdown_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formula_pingfen = models.CharField(db_column='Formula_PingFen', max_length=32, blank=True, null=True)  # Field name made lowercase.
    multi_line_beizhu = models.CharField(db_column='Multi_Line_BeiZhu', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_ZuoWeiTiQianQu'


class JiaTest(models.Model):
    c1 = models.IntegerField(blank=True, null=True)
    c2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jia_test'


class VideoHit(models.Model):
    videoid = models.CharField(max_length=14, blank=True, null=True)
    c_frame = models.IntegerField(blank=True, null=True)
    c_action = models.CharField(max_length=40, blank=True, null=True)
    c_x = models.FloatField(blank=True, null=True)
    c_y = models.FloatField(blank=True, null=True)
    c_w = models.FloatField(blank=True, null=True)
    c_h = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_hit'


class VideoRoute(models.Model):
    videoid = models.CharField(max_length=14, blank=True, null=True)
    c_frame = models.IntegerField(blank=True, null=True)
    c_updown = models.CharField(max_length=10, blank=True, null=True)
    c_position = models.CharField(max_length=10, blank=True, null=True)
    c_hand = models.CharField(max_length=10, blank=True, null=True)
    c_route = models.CharField(max_length=10, blank=True, null=True)
    c_action = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_route'


class VideoScore(models.Model):
    videoid = models.CharField(max_length=14, blank=True, null=True)
    c_start = models.IntegerField(blank=True, null=True)
    c_end = models.IntegerField(blank=True, null=True)
    c_game = models.IntegerField(blank=True, null=True)
    c_total = models.IntegerField(blank=True, null=True)
    c_score_a = models.IntegerField(blank=True, null=True)
    c_score_b = models.IntegerField(blank=True, null=True)
    c_serve = models.CharField(max_length=100, blank=True, null=True)
    c_goal = models.CharField(max_length=100, blank=True, null=True)
    c_goal_class = models.CharField(max_length=40, blank=True, null=True)
    c_third = models.CharField(max_length=40, blank=True, null=True)
    c_second = models.CharField(max_length=40, blank=True, null=True)
    c_first = models.CharField(max_length=40, blank=True, null=True)
    c_updown = models.IntegerField(blank=True, null=True)
    c_checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_score'
