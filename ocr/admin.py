from django.contrib import admin
from ocr.models import *
# Register your models here.

@admin.register(user)
class OcrUser(admin.ModelAdmin):
    list_display = ['username','firstname','lastname','password','role','age','gender','email','picture','address','tel','stack']

@admin.register(officer)    
class OcrOfficer(admin.ModelAdmin): 
    list_display = ['username','firstname','lastname','password','gender','age','email','tel','picture','address']

@admin.register(car) 
class OcrCar(admin.ModelAdmin):
    list_display = ['user','car_type','brand','cc_type','color','license_plate','license_plate_color','picture_car']

@admin.register(notification)
class OcrNoti(admin.ModelAdmin):
    list_display = ['user','officer','date','location','picture',]
     
@admin.register(report_problem)
class OcrReport(admin.ModelAdmin):
    list_display = ['user','officer','date','pic','pic_plate','license_plate','message']

@admin.register(payment)
class OcrReport(admin.ModelAdmin):
    list_display = ['user','traffic_ticket1','date','photo_evidence','price','status']

@admin.register(traffic_ticket)
class OcrReport(admin.ModelAdmin):
    list_display = ['officer','user','car','accusation','location','picture_evidence','price','filePath']

@admin.register(student_discipline)
class OcrReport(admin.ModelAdmin):
    list_display = ['officer','user','location','message','picture_evidence','date','status']

