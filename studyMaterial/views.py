from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pre_Q_Paper, Gate, Indian_Engineering_Services, Subject,Universitie
from collections import defaultdict


def Universitie(request):
    universitie = Universitie.objects.all()
    context = {"universities":Universitie}
    return render(request,"main.html", context)

@login_required(login_url="/myAccount/LogIn/")
def previousYear(request):
    papers = Pre_Q_Paper.objects.all()
    Subjects = Subject.objects.all()
    data = {}
    if request.method == "POST":
        a = request.POST.get("Year")
        b = request.POST.get("Department")
        if (request.POST.get("Year") != "") & (request.POST.get("Department") != ""):
            subjects = Subjects.filter(Year=a,Department_id=b)
            for i in subjects:
                Papers = papers.filter(Subjects=i)
                if Papers.exists():
                    data[i.Subjects] = {}
                    for j in Papers:
                        for i in data:
                            if i == str(j.Subjects):
                                datas = { j.Subject_Name : j.papers }
                                data[i].update(datas)
    return render(request,"Previous.html", {"data":data})

@login_required(login_url="/myAccount/LogIn/")
def Gates(request):
    exams = Gate.objects.all()
    filters = None
    if request.method == "POST":
        if (request.POST.get("Gate") != ""):
            b = request.POST.get("Gate")
            filters = exams.filter(Department_id=b)
    return render(request,"Gate.html", {"Gate":filters})

@login_required(login_url="/myAccount/LogIn/")
def EngineeringServices(request):
    exams = Indian_Engineering_Services.objects.all()
    filters = None
    if request.method == "POST":
        if (request.POST.get("EngineeringServices") != ""):
            b = request.POST.get("EngineeringServices")
            filters = exams.filter(Department_id=b)
    return render(request,"EngineeringServices.html", {"Service":filters})

