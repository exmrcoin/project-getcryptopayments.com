from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from apps.coins.models import Coin

# Create your models here.


class ButtonMaker(models.Model):
    merchant_id = models.CharField(
        verbose_name=_('merchant id'), max_length=128)
    item_name = models.CharField(max_length=128, null=False)
    item_amount = models.CharField(max_length=128, null=False)
    item_number = models.CharField(max_length=128, null=False)
    item_qty = models.CharField(max_length=128, null=False)
    buyer_qty_edit = models.BooleanField(default=False)
    invoice_number = models.CharField(max_length=128, null=False)
    tax_amount = models.CharField(max_length=128, null=False)
    allow_shipping_cost = models.BooleanField(default=False)
    shipping_cost = models.CharField(max_length=128, null=False)
    shipping_cost_add = models.CharField(max_length=128, null=False)
    success_url_link = models.CharField(max_length=128, null=False)
    cancel_url_link = models.CharField(max_length=128, null=False)
    ipn_url_link = models.CharField(max_length=128, null=False)
    btn_image = models.ForeignKey('ButtonImage', on_delete=models.CASCADE)
    allow_buyer_note = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name


class ButtonImage(models.Model):
    label = models.CharField(max_length=128, null=False)
    btn_img = models.ImageField(upload_to='button_maker/')

    def __str__(self):
        return self.label

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

class CryptoPaymentRec(models.Model):
    merchant_id = models.CharField(
        verbose_name=_('merchant id'), max_length=128)
    item_name = models.CharField(max_length=128, null=False)
    item_amount = models.CharField(max_length=128, null=False)
    item_number = models.CharField(max_length=128, null=False)
    item_qty = models.CharField(max_length=128, null=False)
    invoice_number = models.CharField(max_length=128, null=False)
    unique_id = models.CharField(max_length=128, null=False)
    
    tax_amount = models.CharField(max_length=128, null=False)
    shipping_cost = models.CharField(max_length=128, null=False)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    email_addr = models.CharField(max_length=128, null=False)
    addr_l1 = models.CharField(max_length=128, null=False)
    addr_l2 = models.CharField(max_length=128, null=False)
    country = models.CharField(max_length=128, null=False)
    city = models.CharField(max_length=128, null=False)
    state = models.CharField(max_length=128, null=False)
    zipcode = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=128, null=False)    
    buyer_note = models.CharField(max_length=128, null=True) 
    selected_coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.item_name

    

class MercSidebarTopic(models.Model):
    """
    Model to save frequently asked questions
    """
    merc_side_topic = models.CharField(max_length=512)

    def __str__(self):
        return self.merc_side_topic


class MercSidebarSubTopic(models.Model):
    """
    Model to save help sidebar topics and their answers
    """
    main_topic = models.ForeignKey(MercSidebarTopic, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=64)
    help_answer = RichTextUploadingField()
    order_index = models.IntegerField()
    slug = models.SlugField(default=slugify(sub_topic))
    
    def __str__(self):
        return self.sub_topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sub_topic)
        super(MercSidebarSubTopic, self).save(*args, **kwargs)


class URLMaker(models.Model):
    merchant_id = models.CharField(
        verbose_name=_('merchant id'), max_length=128)
    unique_id = models.CharField(max_length=128, null=False, unique=True)
    item_name = models.CharField(max_length=128, null=False)
    item_desc = models.CharField(max_length=512, null=False)
    item_amount = models.CharField(max_length=128, null=False)
    item_number = models.CharField(max_length=128, null=False)
    item_qty = models.CharField(max_length=128, null=False)
    invoice_number = models.CharField(max_length=128, null=False)
    tax_amount = models.CharField(max_length=128, null=False)
    shipping_cost = models.CharField(max_length=128, null=False)
    ipn_url_link = models.CharField(max_length=128, null=False)
    URL_link = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.item_name
