from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class House(models.Model):
    country = models.CharField(max_length=200)
    state   = models.CharField(max_length=200)
    city    = models.CharField(max_length=200)
    street  = models.CharField(max_length=200)
    unit    = models.CharField(max_length=200)
    zip     = models.CharField(max_length=200)

    def __unicode__(self):
    	return str(self.id)

class People(models.Model):
	GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('DND', 'I do not want to disclose'),)

	AGE = (
		('A1', '18-21'),
		('A2', '26-30'),
		('A3', '31-40'),
		('A4', '41-50'),
		('A5', '51-60'),
		('A6', '60+'),
		('DND', 'I do not want to disclose'),)

	INCOME = (
		('I1', 'Less than $10,000'),
		('I2', '$10,000-$19,999'),
		('I3', '$20,000-$29,999'),
		('I4', '$30,000-$39,999'),
		('I5', '$40,000-$49,999'),
		('I6', '$50,000-$59,999'),
		('I7', '$60,000-$69,999'),
		('I8', '$70,000-$79,999'),
		('I9', '$80,000-$89,999'),
		('I10', '$90,000-$99,999'),
		('I11', '$100,000-$149,000'),
		('I12', 'More than $150,000'),
		('DND', 'I do not want to disclose'),)

	EDUCATION = (
		('E1', 'Less than High School'),
		('E2', 'High School / GED'),
		('E3', 'Some College'),
		('E4', '2-Year College Degree(Associates)'),
		('E5', '4-Year College Degree(BA,BS)'),
		('E6', 'Masters Degree'),
		('E7', 'Doctoral Degree'),
		('E8', 'Professional Degree(MD,JD)'),
		('DND', 'I do not want to disclose'),)

	ETHINICITY = (
		('ET1', 'White'),
		('ET2', 'White, non-Hispanic'),
		('ET3', 'African-American'),
		('ET4', 'Hispanic'),
		('ET5', 'Native American'),
		('ET6', 'Asian-Pacific Islander'),
		('DND', 'I do not want to disclose'),
		)

	
	user = models.OneToOneField(User)
	
	gender = models.CharField(max_length=10, default='DND',choices = GENDER)
	age    = models.CharField(max_length=100,default='DND', choices = AGE)
	income = models.CharField(max_length=100,default='DND',choices = INCOME)
	education = models.CharField(default='DND',max_length=200, choices = EDUCATION)
	ethnicity = models.CharField(default='DND',max_length=200, choices = ETHINICITY)


class Review_Code(models.Model):
	FACTOR_TYPE = (
    ('integer', 'INTEGER'),
    ('text', 'TEXT'), )

	factor_name = models.CharField(max_length=200)
	factor_type = models.CharField(max_length=200, choices = FACTOR_TYPE)
	factor_value = models.CharField(max_length=200)

	def __unicode__(self):
		return self.factor_name

class Review(models.Model):
	uid = models.ForeignKey(User)
	hid = models.ForeignKey(House)
	code = models.ForeignKey(Review_Code)
	value = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	unique_together = ("uid", "hid", "code")
	def __unicode__(self):
		return str(self.id)


    


