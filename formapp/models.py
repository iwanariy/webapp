from django.db import models


class Contact(models.Model):
    name = models.CharField(u"Name", max_length=256)
    title = models.CharField(u"Title", max_length=256)
    description = models.TextField(u"Description")
    mail_address = models.CharField(u"Mail Address", max_length=256)

    def __unicode__(self):
        return self.item_code

    class Meta:
        db_table = 'contact'
        verbose_name = u"お問い合わせ"
        vervose_name_plural = u"お問い合わせ"
