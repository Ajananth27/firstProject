
from django.db.models.query_utils import Q
from calc.models import covidreport, feedback, hospitallist
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from calc.scrap import getCovidCase


# Create your views here.

def index(request):
    return render(request, 'index.html')

def adminInserts(request):
    return render(request, 'admin.html')

def retrieve(request):
    return render(request, 'demo.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('adminInserts')
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 == password2:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
    return redirect('/home')

def logout(request):
    auth.logout(request)
    return redirect('/home')

def adminretrieve(request):
    data = hospitallist.objects.all()
    return render(request, 'admin_edit.html', {'data' : data})

def searchMain(request):
    if request.method == "POST":
        search_d1 = request.POST.get('hname')
        search_d2 = request.POST.get('loc')
        result_data = hospitallist.objects.filter(Q(hospitalname=search_d1) | Q(district=search_d2))
    return render(request, 'filter_result.html', {'result_data' : result_data})

def searchhospital(request):
    if request.method == "POST":
        search_d1 = request.POST.get('hname')
        data = hospitallist.objects.filter(Q(hospitalname=search_d1))
    return render(request, 'admin_edit.html', {'data' : data})

def insertFBrecord(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        ins = feedback(name = name, email = email, comments = comments)
        ins.save()
    return render(request, 'index.html')

def insertadminrecord(request):
    if request.method == "POST":
        hospitalname = request.POST.get('HospitalName')
        hospital = request.POST.get('Hospital')
        specialty = request.POST.get('Specialty')
        address1 = request.POST.get('Address1')
        address2 = request.POST.get('Address2')
        district = request.POST.get('District')
        state = request.POST.get('State')
        contactno = request.POST.get('PhoneNo')
        mailid = request.POST.get('mailid')
        location = request.POST.get('location')
        insadmin = hospitallist(hospitalname = hospitalname, hospital = hospital, specialty = specialty, address1 = address1,
                                address2 = address2, district = district, state = state, contactno = contactno, mailid = mailid,
                                location = location)
        insadmin.save()
    return render(request, 'admin.html')

def editadminrecord(request, id):
    edit_data = hospitallist.objects.get(id=id)
    if request.method == "POST":
        edit_data.hospitalname = request.POST.get('HospitalName')
        edit_data.hospital = request.POST.get('Hospital')
        edit_data.specialty = request.POST.get('Specialty')
        edit_data.address1 = request.POST.get('Address1')
        edit_data.address2 = request.POST.get('Address2')
        edit_data.district = request.POST.get('District')
        edit_data.state = request.POST.get('State')
        edit_data.contactno = request.POST.get('PhoneNo')
        edit_data.mailid = request.POST.get('mailid')
        edit_data.location = request.POST.get('location')
        
        edit_data.save()
        return redirect('/adminInserts/retrieve/')
    return render(request, 'admin_edit_id.html', {'edit_data' : edit_data})

def deleterecord(request, id):
    delete_rec = hospitallist.objects.get(id=id)
    delete_rec.delete()
    return redirect('/adminInserts/retrieve/')

def searcheye(request, speciality):
    # speciality = "eye"
    result_data = hospitallist.objects.filter(specialty=speciality)
    return render(request, 'filter_result.html', {'result_data' : result_data})

def getlocation(request, id):
    result_data = hospitallist.objects.get(id=id)
    return render(request, 'filter_result_view.html', {'result_data' : result_data})

def covidcase(request):
    data = getCovidCase()
    db_data = covidreport.objects.all()
    db_data.delete()
    for i in data:
        for k in i:
            country = i[0]
            totalcases = i[1]
            newcases = i[2]
            totaldeaths = i[3]
            newdeaths = i[4]
            totalrecovered = i[5]
            newrecovered = i[6]
            activecases = i[7]
        datainsert = covidreport(country = country, totalcases=totalcases, newcases=newcases, totaldeaths=totaldeaths, newdeaths=newdeaths,
                                totalrecovered=totalrecovered, newrecovered=newrecovered, activecases=activecases)
        datainsert.save()

    covidrec = covidreport.objects.all()
    return render(request, 'covidreport.html', {'covidrec':covidrec})

def searchcountry(request):
    if request.method == "POST":
        coun1 = request.POST.get('country')
        coun2 = request.POST.get('country1')
        coun3 = request.POST.get('country2')
        re1 = covidreport.objects.filter(Q(country=coun1))
        re2 = covidreport.objects.filter(Q(country=coun2))
        re3 = covidreport.objects.filter(Q(country=coun3))
        c = []
        c.append(re1)
        c.append(re2)
        c.append(re3)
    return render(request, 'covidreport_mul_chart.html', {'c':c})

def chartdatamax(request):
    if request.method == "POST":
        coun1 = request.POST.get('country')
        # coun2 = request.POST.get('country1')
        # coun3 = request.POST.get('country2')
        c = covidreport.objects.filter(Q(country=coun1))
        # c1 = covidreport.objects.filter(Q(country=coun2))
        # c2 = covidreport.objects.filter(Q(country=coun3))
    return render(request, 'covidreport_chart.html', {'c' :c})
