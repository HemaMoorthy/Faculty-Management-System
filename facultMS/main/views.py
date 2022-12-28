from django.shortcuts import render
from.models import *

def home(request):
    context={}
    return render(request, 'index.html', context)

def allFac(request):
    facs=Faculty.objects.all()
    context={'facs':facs}
    return render(request, 'allFaculties.html', context)


def addFac(request):
    subs=Subject.objects.all()
    dept=Dept.objects.all()
    context={'subs':subs, 'dept':dept}
    return render(request, 'addFaculty.html', context)

def newFac(request):
    if(request.method=='POST'):
        name=request.POST['fname']
        fid=request.POST['fid']
        dept=request.POST['dept']
        sub=list(map(int, request.POST.getlist('sub')))
        exp=request.POST['exp']
        sal=request.POST['sal']
        print(name, fid, dept, sub, exp, sal)
        maind=Dept.objects.get(id=dept)
        mains=''
        for x in sub:
            print(x)
            mains+=f'{Subject.objects.get(id=x)}, '
        ins=Faculty(facId=fid, name=name, subjects=mains, dept=maind, experience=exp, salary=sal)
        ins.save()
    facs=Faculty.objects.all()
    context={'facs':facs}
    return render(request, 'allFaculties.html', context)


def delFac(request, pk):
    if(request.method=='POST'):
        ins=Faculty.objects.get(id=pk)
        ins.delete()
        facs=Faculty.objects.all()
        context={'facs':facs}
        return render(request, 'allFaculties.html', context)


def updateFac(request, pk):
    if(request.method=='POST'):
        ins=Faculty.objects.get(id=pk)
        subs=Subject.objects.all()
        dept=Dept.objects.all()
        context={'fac':ins, 'subs':subs, 'dept':dept}
        return render(request, 'updateFaculty.html', context)


def getUpdate(request, pk):
    if(request.method=='POST'):
        name=request.POST['fname']
        fid=request.POST['fid']
        dept=request.POST['dept']
        sub=list(map(int, request.POST.getlist('sub')))
        exp=request.POST['exp']
        sal=request.POST['sal']
        print(name, fid, dept, sub, exp, sal)
        maind=Dept.objects.get(id=dept)
        mains=''
        for x in sub:
            print(x)
            mains+=f'{Subject.objects.get(id=x)}, '
        
        ins=Faculty.objects.get(id=pk)
        ins.facId=fid
        ins.name=name
        ins.dept=str(maind)
        ins.subjects=mains
        ins.experience=exp
        ins.salary=sal
        ins.save()
       
        facs=Faculty.objects.all()
        context={'facs':facs}
        return render(request, 'allFaculties.html', context)


def subs(request):
    if(request.method=='POST'):
        name=request.POST['name']
        sid=request.POST['sid']
        fname=request.POST['fname']
        tdept=Dept.objects.get(id=request.POST['dept'])
        ins=Subject(subId=sid, name=name, fname=fname, dept=tdept)
        ins.save()
        dept=Dept.objects.all()
        subs=Subject.objects.all()
        context={'dept':dept, 'subs':subs}
        return render(request, 'allSubs.html', context)
    else:
        dept=Dept.objects.all()
        subs=Subject.objects.all()
        context={'dept':dept, 'subs':subs}
        return render(request, 'allSubs.html', context)

def depts(request):
    if(request.method=='POST'):
        name=request.POST['name']
        did=request.POST['did']
        fname=request.POST['fname']
        ins=Dept(deptId=did, name=name, fname=fname)
        ins.save()
        dept=Dept.objects.all()
        context={'dept':dept}
        return render(request, 'allDepts.html', context)
    else:
        dept=Dept.objects.all()
        context={'dept':dept}
        return render(request, 'allDepts.html', context)
        


        