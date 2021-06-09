from django.shortcuts import render

def arya(request):
    return render(request,"main.html")

def registercheck(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    if username== "hari" and password=="1234":
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")


