from django.db import models
from jobportal.settings import *
from languages.fields import LanguageField


class Language(models.Model):
    language = LanguageField(max_length=200)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = "Languages"


class Skills(models.Model):
    skills = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.skills

    class Meta:
        verbose_name_plural = "Skills"


class Machine(models.Model):
    machine = models.CharField(max_length=200)

    def __str__(self):
        return self.machine

    class Meta:
        verbose_name_plural = "MachineS"


class Education(models.Model):
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.education

    class Meta:
        verbose_name_plural = "Education"


class Industry(models.Model):
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.industry

    class Meta:
        verbose_name_plural = "Industry"


class JobRole(models.Model):
    job_role = models.CharField(max_length=200)

    def __str__(self):
        return self.job_role

    class Meta:
        verbose_name_plural = "JobRoles"


class SubRole(models.Model):
    sub_role = models.ForeignKey(JobRole)

    def __str__(self):
        return self.sub_role.job_role

    class Meta:
        verbose_name_plural = "SubRoles"


class JobType(models.Model):
    job_type = models.CharField(max_length=20)

    def __str__(self):
        return self.job_type


class FeaturedCompany(models.Model):
    company_name = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_form='documents/')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "FeaturedCompany"


class ProfileServices(models.Model):
    profile_services = models.CharField(max_length=200)

    def __str__(self):
        return self.profile_services

    class Meta:
        verbose_name_plural = "ProfileServices"




