from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email =request.POST['email']                            
        subject = request.POST['subject']
        message1 =request.POST['message']
        message= "name: " + name + ",  " + "email:  "+email + ",  " + "message :" + message1

        
        send_mail(subject, message, email,['umaxconstructions@gmail.com'], fail_silently=True)
        #send_mail(subject,message,email,['*****************@gmail.com'], fail_silently=True)
        #name
         #   subject,#subject
          #  message,#message
           # email,#from email
            #['venvim52459@glenwoodave.com'],#to email
            #)


        
        return render(request, 'home.html')


    else:
        return render(request, 'home.html', {})


    
    


'''def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email =request.POST['email']                            
        subject = request.POST['subject']
        message =request.POST['message']
        send_mail(subject,message,email,['888888888@gmail.com'], fail_silently=True)
        #name
         #   subject,#subject
          #  message,#message
           # email,#from email
            #['venvim52459@glenwoodave.com'],#to email
            #)


        
        return render(request, 'contact.html')


    else:
        return render(request, 'contact.html', {})
'''
