from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City
from cities_light.models import Region
from jobportal.apps.accounts.models import RecruiterDetail
from jobportal.apps.common.models import Education, Industry, JobRole, JobType, SubRole, Language, Machine, Skills


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(('email'), max_length=254)
    city = models.ForeignKey(City)
    location = models.ForeignKey(Region)
    role = models.ForeignKey(JobRole)
    pin_code = models.CharField(max_length=30, blank=False)
    landmark = models.CharField(max_length=50, blank=True)


class Plan(models.Model):
    FREE = 'FREE'
    GOLD = 'GOLD'
    GOLD_URGENT = 'GOLD_URGENT'
    SPOTLIGHT = 'SPOTLIGHT'

    CHOICES = (
        (FREE, 'Free'),
        (GOLD, 'Gold'),
        (GOLD_URGENT, 'Gold and urgent'),
        (SPOTLIGHT, 'Spotlight'),
    )
    company_name = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='documents/')
    duration = models.CharField(max_length=20)
    type = models.CharField( max_length=20, blank=True, choices=CHOICES)


class JobApplication(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(JobRole)




class JobSeeker(models.Model):
    PART_TIME = 'PART_TIME'
    FULL_TIME = 'FULL_TIME'

    CHOICES = (
        (PART_TIME, 'Part time.'),
        (FULL_TIME, 'Full time'),
    )

    monthly_salary = models.CharField(help_text='per month', max_length=200, null=False)
    job_mode = models.CharField(('job_mode'), max_length=20, blank=True, choices=CHOICES)
    height = models.CharField(('height'), max_length=20)
    address_proof = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    languages = models.ManyToManyField(Language)
    machines_used = models.ForeignKey(Machine)
    licence = models.FileField(upload_to='documents/')
    job_title = models.CharField(max_length=100, blank=True)
    police_verification = models.BooleanField(default=False)
    skills = models.ForeignKey(Skills)
    smart_phone = models.BooleanField(default=False)
    criminal = models.BooleanField(default=False)
    cases_complaints = models.BooleanField(default=False)
    desired_location = models.ForeignKey(City)
    education = models.ForeignKey(Education)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(('email'), max_length=254)
    hello_english_score = models.DecimalField(blank=True)
    industry = models.ForeignKey(Industry)

    def __str__(self):
        return self.user


class PostJob(models.Model):
    job_title = models.CharField(max_length=200, blank=False)
    job_type = models.ForeignKey(JobType)
    role = models.ForeignKey(JobRole)
    sub_role = models.ForeignKey(SubRole)
    min_salary = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    hiring_company = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    locality = models.ForeignKey(Region)
    max_experience = models.CharField(max_length=20, blank=False)
    min_experience = models.CharField(max_length=20, blank=False)
    job_description = models.TextField(max_length=3000, blank=False)
    recruiter_detail = models.ForeignKey(RecruiterDetail)
    membership = models.BooleanField(default=False)



