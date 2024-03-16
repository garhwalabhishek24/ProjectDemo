from django.shortcuts import render

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def home(request):
    return render(request,"index.html")

def price(request):
    return render(request,"price.html")

def service(request):
    return render(request,"service.html")

def userform(request):
    try:
        if request.method=='POST':
            n1=request.POST.get('name')
            n2=request.POST.GET('email')
            n3=request.POST.GET('phone')
            print(n1);
            print(n2);
            print(n3);
    except:
        pass
    return render(request,"userfrom.html",{'output':'name'})
   
    