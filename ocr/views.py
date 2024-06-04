import cv2
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from ocr.models import *
from django.http import HttpResponseRedirect
# from django.core.mail import EmailMessage
from django.core.mail import send_mail,BadHeaderError,EmailMultiAlternatives
from django.conf import settings

from weasyprint import HTML
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string  #
from django.utils.html import strip_tags #
import json
import os 
import pdfkit
# from ironpdf import *


# Create your views here.

                #----------Home----------
def home(request):
    return render(request,"home.html")
def home2(request):
    return render(request,"home2.html")

                #***********SEND MAIL*****************
                
def send_email(request):
    
    ticket = traffic_ticket.objects.all().order_by("-id")[0]
    userrole = ticket.user.role
    print(userrole)
    if (userrole == "outsider"):
        subject = " ใบสั่งจากเจ้าหน้าที่จราจร"
        msg = "คุณได้รับใบสั่ง เนื่องจากคุณได้ทำผิดกฎจราจรภายในมหาวิทยาลัย"
    else:
        subject = " ใบเตือนจากเจ้าหน้าที่จราจร"
        msg = "คุณได้รับใบเตือน เนื่องจากคุณได้ทำผิดกฎจราจรภายในมหาวิทยาลัย"
    context = {'subject':subject,'msg':msg,'ticket':ticket}
    # PDFticket = "http://127.0.0.1:8000/static/ocr/pdf/" + ticket.filePath
    # print(PDFticket)
    if request.method == "POST":
        pdf = "localhost:8000/media/PDF/" + request.FILES['attachment'].name
        if (userrole == "outsider"):
                temp = render_to_string(context={'temp':pdf},template_name='tempmail.html')
        else:
                temp = render_to_string(context={'temp':pdf},template_name='tempmail2.html')
        pm = strip_tags(temp)
        try:
            message = EmailMultiAlternatives(
                subject = request.POST['subject'],
                body=pm,
                from_email = 'djangopj2023@gmail.com',
                to = [request.POST['recipient']]
            )

            message.attach_alternative(temp, "text/html")
            message.send()
            # send_mail(subject, message, from_email, recipient_list)
            return HttpResponse('The email has been sent successfully !!!!!')
        except BadHeaderError:
            return HttpResponse('Email sending failed !!!!!')
    # return render(request,"send_mail.html",context)
    return render(request,"send_mail.html",context)

                #**********Register*************
                
def login(request):
    return render(request,"login.html")
def logincheck(request):
    user1 = request.POST['username']
    password1 = request.POST['password']
    print("login")
    try:
        u = user.objects.get(username=user1,password=password1)
        request.session['userid'] = u.id
        request.session['username'] = u.username
        request.session['email'] = u.email
        request.session['firstname'] = u.firstname
        request.session['lastname'] = u.lastname
        request.session['role'] = u.role
        request.session['picture'] = str(u.picture)[4:]

        # print(u.username)
        return redirect('home')
    except:
        pass
    try:
        of = officer.objects.get(username=user1,password=password1)
        request.session['userid'] = of.id
        request.session['username'] = of.username
        request.session['email'] = of.email
        request.session['firstname'] = of.firstname
        request.session['lastname'] = of.lastname
        # request.session['role'] = of.role
        request.session['picture'] = str(of.picture)[4:]

        # print(of.username)
        return redirect('check_report_user')
    
    except:
        return redirect('login')
    
def forgot(request):
    return render(request,"forgot_password.html")

def sing_up(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        role = request.POST['role']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        picture = request.FILES['picture']
        password = request.POST['password']
        tel = request.POST['tel']
        picture_car = request.FILES['picture_car']
        brand = request.POST['brand']
        cc_type = request.POST['cc_type']
        car_color = request.POST['car_color']
        plate = request.POST['plate']
        license_plate_color = request.POST['license_plate_color']
        open('media/picture_car/'+ picture_car.name, 'wb').write(picture_car.file.read())
        open('media/picture_user/'+ picture.name, 'wb').write(picture.file.read())
        # print(request.POST)
        # print(license_plate_color)
        # print(car_color)

        su=user()
        su.username=username
        su.firstname=firstname
        su.lastname=lastname
        su.role=role
        su.gender=gender
        su.age=age
        su.address=address
        su.tel=tel
        su.picture=picture
        su.email=email
        su.password=password
        su.save() 

        ca=car()
        ca.user=user.objects.filter(username=username).last()
        ca.picture_car=picture_car
        ca.brand=brand
        ca.color=car_color
        ca.license_plate=plate
        ca.cc_type=cc_type
        ca.license_plate_color=license_plate_color
        ca.save()

        return redirect("login")
    return render(request,"sing_up.html")

            #----------Report----------
def report(request):
    if request.method=="POST":
        if 'confirm' in request.POST:
            pic_plate = request.POST['pic_plate']
            text_plate = request.POST['num_plate']
            message = request.POST['message']
            pic = request.POST['pic']

            rp = report_problem()
            rp.user=user.objects.get(id=request.session['userid']) 
            rp.pic=pic[5:]
            rp.pic_plate=pic_plate[5:]
            rp.license_plate = text_plate
            rp.message=message
        
            rp.save()

            return render(request,"report_problem.html")
    
        pic = request.FILES['reportPic']
        file_path = 'media/picture_car/' + pic.name
        cropped_path = 'media/picture_crop_car' + pic.name
        import ocr.filePlateModule as fPM
        open(file_path, 'wb').write(pic.file.read())

        image,x,y,w,h = fPM.findPlate(file_path) # รูปปกติ
        cropped_image = fPM.crop_plate(image,x,y,w,h) #รูปที่ครอปแล้ว
        character =  fPM.findNumber(cropped_image) # รายการตัวอักษร
        # import ocr.plate_ocr as pl
        # print(os.system('dir'))
        
        cv2.imwrite(cropped_path,cropped_image)

        text_plate = ""
        for i in character:
            text_plate += i + " "

        print(text_plate)
       
        # text_plate = pl.ocr(file_path)
        # print("text:",text_plate[0])
        # context = {'text_plate':character[0]+character[1],'pic_path':file_path,'pic':file_path}
        context = {'text_plate':text_plate,'pic_path':cropped_path,'pic':file_path}
        return render(request,"report_problem.html",context)
    return render(request,"report_problem.html")

def check_report_user(request):
    report_user = report_problem.objects.all().order_by('-id')
    user1 = user.objects.all()
    of = officer.objects.all()
    
    #  rp_outsider = report_problem.objects.filter(user=users_outsider.id).first()
    context = {'report_user':report_user,'user1':user,'of':of}
    return render(request,"check_report.html",context)

def check_report_user_more(request,id):
    um = report_problem.objects.get(id=id)
    # print(car.objects.get(license_plate=um.license_plate))
    try:
        us = car.objects.get(license_plate=um.license_plate)
        has = True
        context ={'um':um,'ff':has,'us':us}
        # print(us)
    except:
        has = False
        context ={'um':um,'ff':has}
        pass
    return render(request,"check_report_user_more.html",context)

            # **********ส่งผลวินัย**********
def report_sd(request):
    if request.method=="POST":
        location = request.POST['location']
        message = request.POST['message']
        picture_evidence = request.FILES['reportPic']
        open('media/picture_evidence_sd/'+ picture_evidence.name, 'wb').write(picture_evidence.file.read())
       
        sd=student_discipline()
        sd.user=user.objects.get(id=request.session['userid']) 
        sd.location=location
        sd.message=message
        sd.picture_evidence=picture_evidence
        sd.status="รออนุมัติ"
        sd.save()

    return render(request,"student_discipline.html")
def check_sd(request):
    sd = student_discipline.objects.all().order_by('-id')
    context = {'sd':sd}
    return render(request,"check_student_discipline.html",context)

def check_sd_us(request):
    sd = student_discipline.objects.filter(user=request.session['userid'])
    context = {'sd':sd}
    return render(request,"check_sd_us.html",context)

def check_sd_us_mr(request,id):
    sd = student_discipline.objects.filter(id=id).first()
    if 'confirm' in request.POST:
        if request.POST['confirm']=='confirm':
            sd.officer=officer.objects.get(id=request.session['userid']) 
            sd.status="ผ่าน"
        else:
            sd.officer=officer.objects.get(id=request.session['userid'])
            sd.status="ไม่ผ่าน"
        sd.save()
    context = {'sd':sd}
        # return render(request,"check_student_discipline.html",context)

    return render(request,"check_student_discipline_more.html",context)

             #**********ชำระเงิน************
def payment1(request):
    tf  = traffic_ticket.objects.filter(user=request.session['userid']).first()


    if request.method=="POST":
        sp = request.FILES['slip']
        file_path = 'media/slip/' + sp.name
        # print(request.FILES)
        open(file_path, 'wb').write(sp.file.read())

        suc = payment.objects.get(user=request.session['userid'])
        suc.photo_evidence = sp
        suc.status="ชำระเงินเเล้ว"
        suc.save()
        
    return render(request,"payment.html",{'tf':tf})


def check_payment(request):
    pay = payment.objects.filter(user=request.session['userid'])
    context = {'pay':pay}
    return render(request,"check_payment.html",context)

def check_payment_user(request):
    pay = payment.objects.all()
    context = {'pay':pay}
    # print(pay)
    return render(request,"check_payment_user.html",context)

def check_payment_user_more(request):
    return render(request,"check_payment_user_more.html")


             #*********เเก้ไขข้อมูลพนักงาน***********

def edit_officer(request):
    officer1 = officer.objects.all()
    context = {'officer1':officer1}
    return render(request,"officer.html",context)
def del_officer(request,id):   
    user1 = officer.objects.get(id=id)
    user1.delete()
    return redirect("officer_list")
def ed_officer1(request,id):
    officer1 = officer.objects.get(id=id)
    context = {'officer1':officer1}
    return render(request,"edit_officer.html",context)

def edit_officer_save(request):   
    officer1 = officer.objects.get(id= request.POST['id'])

    officer1.username = request.POST['username']
    officer1.firstname = request.POST['firstname']
    officer1.lastname = request.POST['lastname']
    officer1.gender = request.POST['gender']
    officer1.age = request.POST['age']
    officer1.email = request.POST['email']
    officer1.tel = request.POST['tel']
    officer1.address = request.POST['address']

    officer1.save()
    return redirect("officer_list")

              #*********เเก้ไขข้อมูลผู้ใช้**********

def edit_user(request):
    users = user.objects.all()
    context = {'users':users}
    return render(request,"edit_user.html",context)
def edit_user2(request,id):
    user1 = user.objects.get(id=id)
    context = {'user1':user1}
    # print(user1)
    return render(request,"edit_user2.html",context)
def del_user(request,id):
    users = user.objects.get(id=id)
    users.delete()
    return redirect("edit_user")
def edit_user_save(request):   
    user1 = user.objects.get(id= request.POST['id'])

    user1.username = request.POST['username']
    user1.firstname = request.POST['firstname']
    user1.lastname = request.POST['lastname']
    user1.gender = request.POST['gender']
    user1.age = request.POST['age']
    user1.email = request.POST['email']
    user1.tel = request.POST['tel']
    user1.address = request.POST['address']

    user1.save()
    return redirect("edit_user")

              #********โปรไฟล์**********

def profile(request):
    user1 = user.objects.get(id=request.session['userid'])
    context = {'user':user1}
    return render(request,"profile.html",context)
def edit_pf(request):
    user1 = user.objects.get(id=request.session['userid'])
    context = {'user':user1}
    return render(request,"edit_pf.html",context)
def edit_pf_save(request):   
    user1 = user.objects.get(id=request.session['userid'])

    user1.firstname = request.POST['firstname']
    user1.lastname = request.POST['lastname']
    user1.gender = request.POST['gender']
    user1.age = request.POST['age']
    user1.email = request.POST['email']
    user1.tel = request.POST['tel']
    user1.address = request.POST['address']

    user1.save()
    return redirect("profile")


    #***********create PDF**********

def pdf_user(request,id):
    car_student = car.objects.filter(id=id).first()
    user_student = user.objects.get(id=car_student.user.id)
    rp_student = report_problem.objects.filter(license_plate=car_student.license_plate).first()
    context = {'users':user_student,'car_student':car_student,'rp_student':rp_student}
    
    if request.method == 'POST':
        if request.POST['submit'] == 'submit':
            user_name = request.POST['user_name']
            date = request.POST['date']       
            license_plate = request.POST['license_plate']
            officer = request.POST['officer']

            body =f""" ใบเตือนวินัยจราจร เรียน 
{ user_name } \n

เลขทะเบียนรถ 
{ license_plate }

วันที่ 
{ date }

เนื่องจากนักศึกษาได้กระทำความผิดกฎจราจรของมหาวิทลัยเกิน 3 ครั้งเเล้ว ณ ที่นี้ข้าพเจ้าขอแจ้งให้ทราบว่า เมื่อวันที่ 17 มีนาคม 2567 เวลาประมาณ 09:30 น. ท่านได้ขับขี่รถยนต์ทะเบียน 
1กท กระบี่ 7313  โดยมีการจอดรถในที่ห้ามจอด   การกระทำผิดดังกล่าวเป็นการละเมิดกฎหมายจราจร มีความเสี่ยงต่อการเกิดอุบัติเหตุและเป็นอันตรายต่อความปลอดภัยของผู้ใช้ถนนและสังคมได้ 
ข้าพเจ้าขอเรียนเตือนให้ทราบและให้ระมัดระวังในการขับขี่ในอนาคต ขอบคุณมากครับ/ค่ะ

ศรัน จันเเก้ว

เจ้าหน้าที่ """

            message = EmailMultiAlternatives(
                subject = "ใบวินัยจากเจ้าหน้าที่จราจร",
                body=body,
                from_email = 'djangopj2023@gmail.com',
                to = [user_student.email]
            )
            message.send()
            return redirect('check_report_user')
        # print(request.POST)
        from datetime import datetime
        from django.template.loader import get_template 
        from django.template import Context

        ##edit here
        
        user_name = request.POST['user_name']
        car_type = request.POST['car_type']
        brand = request.POST['brand']
        cc_type = request.POST['cc_type']
        car_color = request.POST['car_color']
        license_plate_color = request.POST['license_plate_color']
        offenses = request.POST['offenses']
        license_plate = request.POST['license_plate']
        stack = request.POST['stack']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        offenses = request.POST['offenses']
        image = request.POST['image']

        user_student.stack = user_student.stack + 1 
        user_student.save()

        if (request.POST['submit']  ==  'send'):
            file = request.FILES['filename'].name

            import hashlib
            date = datetime.now()
            def hash_md5(data):
                return hashlib.md5(data.encode()).hexdigest()
            # print(request.POST['template'])
            fname = hash_md5(user_name)
            filePath = '/PDF/'+ file

            addTT = notification()
            user_id = user.objects.get(firstname=user_name.split()[0])
            addTT.user = user_id
            addTT.officer = officer.objects.get(id=request.session['userid'])
            addTT.car =car.objects.filter(id=id).first()
            addTT.filePath = filePath
            
            #edit here to save in database 
            addTT.save()
            return redirect('send_email')  
        
        context = {'user_name':user_name,'car_type':car_type,'cc_type':cc_type,'car_color':car_color,
                   'license_plate_color':license_plate_color,'brand':brand,'offenses':offenses,
                   'license_plate':license_plate,'stack':stack,'date':date,'time':time,'location':location,
                   'offenses':offenses,'image':image,}
    return render(request,"create_pdf_user.html",context)


def pdf_outsider(request,id):
    tf = traffic_ticket.objects.all().last()
    # print(tf)
    if(tf != None):
        lastID = tf.id +1
    else:
        lastID = 1

    car_outsider = car.objects.filter(id=id).first()
    users_outsider =  user.objects.get(id=car_outsider.user.id)
    rp_outsider = report_problem.objects.filter(license_plate=car_outsider.license_plate).first()
    context = {'id':lastID,'users':users_outsider,'car':car_outsider,'rp_outsider':rp_outsider}
    

    # users_outsider =  user.objects.get(id=id)
    # car_outsider = car.objects.filter(user=users_outsider.id).first()
    # rp_outsider = report_problem.objects.filter(license_plate=car_outsider.license_plate).first()
    # context = {'id':lastID,'users':users_outsider,'car':car_outsider,'rp':rp_outsider}
 
    if request.method == 'POST':
        # print(request.POST)
        from datetime import datetime
        from django.template.loader import get_template 
        from django.template import Context
        ##edit here
        
        numtftk = request.POST['numtftk']
        driver = request.POST['driver_name']
        date = request.POST['date']
        typecar = request.POST['cc_type']
        marque = request.POST['marque']
        plate = request.POST['licensePlate']
        location = request.POST['location']
        price = request.POST['price']
        license_pc = request.POST['license_plate_color']
        image = request.POST['image']
        accusation = request.POST['accusation']

        if ('submit' in request.POST):
            file = request.FILES['filename'].name

            import hashlib
            date = datetime.now()
            def hash_md5(data):
                return hashlib.md5(data.encode()).hexdigest()
            # print(request.POST['template'])
            fname = hash_md5(driver)
            filePath = '/PDF/'+ file


            addTT = traffic_ticket()
            user_id = user.objects.get(firstname=driver.split()[0])
            addTT.user = user_id
            addTT.officer = officer.objects.get(id=request.session['userid'])
            addTT.car =car.objects.filter(id=id).first()
            addTT.price =  price
            addTT.type_car = typecar
            addTT.location = location
            addTT.accusation = accusation


            
            #edit here to save in database 
            addTT.save()

            pm = payment()
            pm.user=user_id
            pm.traffic_ticket1= traffic_ticket.objects.all().last()
            pm.price=price
            pm.status="รอชำระเงิน"
            pm.save()
            
            return redirect('send_email')  

        context = {'image':image,'driver':driver,'plate':plate,'numtftk':numtftk,'date': date,'typecar':typecar,'marque':marque,'accusation':accusation,'location':location,'price':price}
        return render(request,"create_pdf_outsider.html",context)
    return render(request,"create_pdf_outsider.html",context)