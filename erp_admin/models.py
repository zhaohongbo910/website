from django.db import models

# Create your models here.
class Mainannouncements(models.Model):
    title = models.CharField(max_length=50, verbose_name='公告标题')
    desc = models.CharField(max_length=50, verbose_name='公告描述')
    content = models.TextField(verbose_name='公告内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name
        #ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

class Wayout(models.Model):
      out_singlenum =models.CharField(max_length=50,verbose_name="出库单号")
      out_theme=models.CharField(max_length=50,verbose_name="出库主题")
      sales_invoice=models.CharField(max_length=50,verbose_name="销售发货单")
      customer_name=models.CharField(max_length=50,verbose_name="客户名称")
      modules=models.CharField(max_length=50,verbose_name="源单类型")
      class Meta(object):
         verbose_name = "库存管理"
         verbose_name_plural=verbose_name
      def  __unicode__(self):
         return self.out_singlenum
         return self.title  
