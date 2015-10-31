from django.db import models

# Create your models here.
#sample:
class Person(models.Model):
	fbid 		= models.CharField(max_length=20)		#facebook id
	fbusername 	= models.CharField(max_length=20)
	firstname 	= models.CharField(max_length=50)
	lastname 	= models.CharField(max_length=50)
	chain 		= models.ForeignKey('self', null=True, blank=True)	#immediate discipler id as Person object. to access down the chain, use person_set
	discipler	= models.CharField(max_length=50)		#first and last name of discipler.
	def __unicode__(self):
		return self.firstname + " " + self.lastname