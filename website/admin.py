from django.contrib import admin
from website.models import *


class HomeAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'background_picture', 'home_heading', 'home_description')

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = HomePage.objects.all().count()
        if count == 0:
            return True

        return False


class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'about_description')

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = About.objects.all()[:4].count()
        if count == 0:
            return True

        return False


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_description')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('category', 'project_name')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_title', 'contact_description', 'phone_number')

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Contact.objects.all().count()
        if count == 0:
            return True

        return False


admin.site.register(HomePage, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact,ContactAdmin)
