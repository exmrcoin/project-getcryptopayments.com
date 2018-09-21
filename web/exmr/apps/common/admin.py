from django.contrib import admin

from apps.common.models import Currency, SocialLink, HelpSidebar, FAQ, LegalSidebar,\
                               PluginDownload, StaticPage, ContactUs, CoinRequest

admin.site.register(Currency)
admin.site.register(SocialLink)
admin.site.register(HelpSidebar)
admin.site.register(FAQ)
admin.site.register(LegalSidebar)
admin.site.register(PluginDownload)
admin.site.register(StaticPage)
admin.site.register(ContactUs)
admin.site.register(CoinRequest)