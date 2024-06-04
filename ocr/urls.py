from django.urls import path
from ocr import views
from .views import *

urlpatterns = [
  path('',views.login), 
  path('home',views.home,name='home'),
#   path('home2',views.home2,name='home2'), 

        #SEND EMAIL
  path('send_email',views.send_email,name='send_email'), 

        #Create a PDF file
  path('pdf_user/<id>',views.pdf_user,name='pdf_user'),
  path('pdf_outsider/<id>',views.pdf_outsider),
#   path('pdf_',views.pdf_outsider),

  path('login',views.login, name='login'), 
  path('check/',views.logincheck,name='check'), 
  path('sing_up',views.sing_up,name='sing_up'),
  path('forgot',views.forgot),

  path('report',views.report),
  path('check_report_user',views.check_report_user,name='check_report_user'),
  path('check_report_user_more/<id>/',views.check_report_user_more,name='check_report_user_more'),

  
  path('report_sd',views.report_sd,name='report_sd'),
  path('check_sd',views.check_sd),
  path('check_sd_us',views.check_sd_us,name='check_sd_us'),
  path('check_sd_us_mr/<id>',views.check_sd_us_mr,name='check_sd_us_mr'),


  path('edit_user',views.edit_user,name="edit_user"),
  path('edit_user2',views.edit_user2),
  path('edit_user/edit/<id>/',views.edit_user2), 
  path('edit_user/delete/<id>',views.del_user),
  path('edit_user_save',views.edit_user_save,name="edit_user_save"),

  path('payment1/',views.payment1),
  path('check_payment',views.check_payment),
  path('check_payment_user',views.check_payment_user),
  path('check_payment_user_more',views.check_payment_user_more),

  path('profile/',views.profile,),
  path('edit_pf',views.edit_pf,name="edit_pf"),
  path('edit_pf_save',views.edit_pf_save,name="edit_pf_save"),

  path('officer',views.edit_officer,name="officer_list"),
  path('ed_officer1/<id>',views.ed_officer1),
  path('officer/edit/<id>/',views.edit_officer),
  path('officer/delete/<id>/',views.del_officer),
  path('edit_officer_save',views.edit_officer_save,name="edit_officer_save"),
]
