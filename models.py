from django.db import models

# Create your models here.

class bookMark(models.Model):
    diff = (
	    ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
         )

    title = models.CharField(max_length=100)
    link = models.CharField(max_length=400) #trim the vlink generate id
    cate = models.ForeignKey('catego' )
    rate = models.CharField(max_length=20 , choices=diff)
    vid = models.CharField(max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):


        sss = self.link
        str = '';
        count = 0;

        for a in sss:

        	if a == '&':
        		count = 2
        	if count == 1:
        		str += a
        	if a == "=" and count == 0:
        		count = 1


        self.vid = str
        super(bookMark, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#########################
#sub catego
#########################
class catego(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
