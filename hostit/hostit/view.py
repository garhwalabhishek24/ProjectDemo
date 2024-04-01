from django.shortcuts import render
from .forms import userform
from features.models import services

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"index.html")

def price(request):
    return render(request,"price.html")

def service(request):
    service_data=services.objects.all()
    if request.method=="GET":
        st=request.GET.get("servicename")
        if st!=None:
            service_data=services.objects.filter( tittle__icontains=st)

    data={
        'service_data':service_data
    }

    return render(request,"service.html",data)

def userform(request):
    fn=userform
    data={'form':fn}
    try:
        if request.method=='POST':
            n1=request.POST.get('num1')
            n2=request.POST.GET('num2')
            fine=n1+n2
            data={
                'form':fn,
                'output':fine
                
            }
    except:
        pass
    return render(request,"userfrom.html",data)
def calculator (request):
    try:
        c=''
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2           
                
    except:        
        c='invalid operation'
    
    return render(request,"calculator.html")
def evenodd(request):
    
    if request.method =="POST":
        c=''
        n=int(request.POST.get('num2'))
        if n%2==0:
            c="even number"
        else:
            c='odd number'    
    return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get("sub1"))
        s2=eval(request.POST.get("sub2"))
        s3=eval(request.POST.get("sub3"))
        s4=eval(request.POST.get("sub4"))
        t=s1+s2+s3+s4
        p=t*100/400
        if p>=65:
            d="first division"
        elif p>=49:
            d='second division'
        else:
            d='failed'
        data={
            'total':t,
            'percent':p,
            'div':d
        }            


    return render(request,"marksheet.html",data)   
    