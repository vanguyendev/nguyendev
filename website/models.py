from django.db import models


class HomePage(models.Model):
    site_name = models.CharField(max_length=100)
    background_picture = models.ImageField(upload_to='img', default='default.jpg')
    home_heading = models.CharField(max_length=200)
    home_description = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = "Home Page"


class About(models.Model):
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()

    class Meta:
        verbose_name_plural = "About"


class Services(models.Model):
    service_title = models.CharField(max_length=20)
    service_description = models.CharField(max_length=200)
    service_icon = models.CharField(max_length=60, default='')

    class Meta:
        verbose_name_plural = "Services"


class Portfolio(models.Model):
    category = models.CharField(max_length=20)
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='img', default='default.jpg')

    class Meta:
        verbose_name_plural = "Portfolio"


class Contact(models.Model):
    contact_title = models.CharField(max_length=50)
    contact_description = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=150)
    contact_email = models.EmailField(max_length=254, default='')

    class Meta:
        verbose_name_plural = "Contact"
