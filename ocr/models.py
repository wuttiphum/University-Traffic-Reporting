from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=20,null=True) 
    firstname=models.CharField(max_length=20,null=True)
    lastname=models.CharField(max_length=20,null=True) 
    role=models.CharField(max_length=20,null=True) 
    age=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=50,null=True)
    picture = models.ImageField(upload_to='./pic',default='./pic')
    address=models.CharField(max_length=100,null=True)
    tel=models.CharField(max_length=20,null=True)
    stack=models.IntegerField(null=True,default=0)

    def __str__(self):
        return str(self.firstname)+" "+ str(self.lastname)

class officer(models.Model):
    username=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=20,null=True)
    firstname=models.CharField(max_length=20,null=True)
    lastname=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=10,null=True)
    age=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=50,null=True)
    tel=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=250,null=True)
    picture = models.ImageField(upload_to='ocr/static/ocr/pic', default='ocr/static/ocr/pic')

    def __str__(self):
        return str(self.firstname)+" "+ str(self.lastname)

class car(models.Model):
    brand=models.CharField(max_length=15,null=True)
    cc_type=models.CharField(max_length=10,null=True)
    car_type=models.CharField(max_length=15,null=True)
    color=models.CharField(max_length=20,null=True)
    license_plate=models.CharField(max_length=100,null=True)
    license_plate_color=models.CharField(max_length=20,null=True)
    picture_car=models.ImageField(upload_to='picture_car',max_length=150,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    
class notification(models.Model): 
    location=models.CharField(max_length=15,null=True)
    accusation=models.CharField(max_length=200,null=True)
    picture=models.FileField(max_length=100,null=True)
    date=models.DateTimeField(auto_now=True,null=True)
    stack=models.CharField(max_length=5,null=True)
    
    filePath=models.FileField(max_length=150,null=True)
    officer=models.ForeignKey(officer,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)

class report_problem(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    officer=models.ForeignKey(officer,on_delete=models.CASCADE,null=True)
    pic=models.ImageField(max_length=250,null=True)
    message=models.CharField(max_length=250,null=True)
    pic_plate=models.ImageField(max_length=250,null=True)
    date=models.DateTimeField(null=True)
    license_plate=models.CharField(max_length=50,null=True)
    


class traffic_ticket(models.Model):
    accusation=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=50,null=True)
    filePath=models.FileField(max_length=150,null=True)
    picture_evidence=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    officer=models.ForeignKey(officer,on_delete=models.CASCADE)
    car=models.ForeignKey(car,on_delete=models.CASCADE,null=True)

class payment(models.Model):
    traffic_ticket1=models.ForeignKey(traffic_ticket,on_delete=models.CASCADE,null=True)
    photo_evidence=models.ImageField(upload_to='slip',max_length=250,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True,null=True)
    price=models.CharField(max_length=250,null=True)
    status=models.CharField(max_length=30,null=True)

class student_discipline(models.Model):  
    status=models.CharField(max_length=20,null=True)
    location=models.CharField(max_length=50,null=True)
    message=models.CharField(max_length=100,null=True)
    picture_evidence=models.FileField(max_length=150,null=True)
    date=models.DateTimeField(auto_now=True,null=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    officer=models.ForeignKey(officer,on_delete=models.CASCADE,null=True)



    
