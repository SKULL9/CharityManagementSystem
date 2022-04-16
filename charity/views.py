from telnetlib import STATUS
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import date


# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_logins(request):
    return render(request, 'all_logins.html')


def donor_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'donor_login.html', locals())


def donor_reg(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Donor.objects.create(user=user, contact=contact, userpic=userpic, address=address)
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor_reg.html', locals())


def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_home.html')






def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method == "POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        try:
            Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,collectionloc=collectionloc,description=description,status="pending")
            error = "no"
        except:
            error = "yes"

    return render(request, 'donate_now.html', locals())


def volunteer_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'volunteer_login.html', locals())


def volunteer_reg(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address,
                                     aboutme=aboutme, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'volunteer_reg.html', locals())


def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    return render(request, 'volunteer_home.html')


def admin_login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def Logout(request):
    logout(request)
    return redirect('index')


def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donation_history.html', locals())


def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="pending")
    return render(request, 'pending_donation.html', locals())



def view_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']
        try:
            donation.adminremark = adminremark
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error="yes"

    return render(request, 'view_donationdetail.html', locals())


def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.filter(status="accept")
    return render(request, 'accepted_donation.html', locals())


def add_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    areaname = DonationArea.objects.all()

    if request.method == "POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
    try:
        DonationArea.objects.create(areaname=areaname, description=description)
        error = "no"
    except:
        error="yes"

    return render(request, 'add_area.html', locals())


def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.all()
    return render(request, 'manage_area.html', locals())


def edit_area(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.get(id=pid)
    if request.method == "POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        area.areaname = areaname
        area.description = description
    try:
        area.save()

        error = "no"
    except:
        error = "yes"

    return render(request, 'edit_area.html', locals())


def delete_area(request, pid):
    DonationArea.objects.get(id=pid).delete()
    return redirect('manage_area')


def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all()
    return render(request, 'manage_donor.html', locals())


def view_donordetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request, 'view_donordetail.html', locals())


def delete_donor(request, pid):
    User.objects.get(id=pid).delete()
    return redirect('manage_donor')


def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="pending")
    return render(request, 'new_volunteer.html', locals())


def view_volunteerdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

    try:
        volunteer.adminremark = adminremark
        volunteer.status = status
        volunteer.updationdate = date.today()
        volunteer.save()
        error = "no"
    except:
        error = "yes"
    return render(request, 'view_volunteerdetail.html', locals())


def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="accept")
    return render(request, 'accepted_volunteer.html', locals())


def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(status="reject")
    return render(request, 'rejected_volunteer.html', locals())


def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.all()
    return render(request, 'all_volunteer.html', locals())


def delete_volunteer(request, pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')


def accepted_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)
    try:
        donation.volunteer = v
        donation.donationarea = da
        donation.status = "volunteer allocated"
        donation.updationdate = date.today()
        donation.save()
        error = "no"
    except:
        error = "yes"
    return render(request, 'accepted_donationdetail.html', locals())



def col_req(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user= request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Volunteer Allocated")

    return render(request, 'col_req.html', locals())



def donationcollection_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        volunteerremark = request.POST['volunteerremark']

        try:
            donation.status = status
            donation.volunteerremark = volunteerremark
            donation.save()
            error="no"
        except:
            error="yes"
    return render(request,'donationcollection_detail.html',locals())



def voldonation_rec(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation Received")
    return render(request, 'voldonation_rec.html', locals())



def voldonation_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

    try:
        donation.status = status
        donation.save()
        Gallery.objects.create(donation=donation,deliverypic=deliverypic)
        error = "no"

    except:
        error = "yes"

    return render(request, 'voldonation_details.html', locals())





def volunteer_assign(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)
        try:
            donation.donationarea = da
            donation.volunteer = v
            donation.status = "Volunteer Allocated"
            donation.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'volunteer_assign.html',locals())





def view_alldetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation = Donation.objects.get(id=pid)
    gallery = Gallery.objects.get(donation=donation)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

    try:

        Gallery.objects.get(donation=donation,deliverypic=deliverypic)
        error = "no"

    except:
        error = "yes"

    return render(request, 'view_alldetail.html', locals())











def allocatedvolunteer_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation =Donation.objects.filter(status="Volunteer Allocated")
    return render(request, 'allocatedvolunteer_donation.html',locals())

def donationvolunteerallocated_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation =Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)
    try:
        donation.volunteer = v
        donation.donationarea = da
        donation.status = "volunteer allocated"
        donation.save()
        error = "no"
    except:
        error = "yes"
    return render(request, 'donationvolunteerallocated_detail.html',locals())



def all_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.all()
    return render(request, 'all_donation.html', locals())







def vol_Del(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation Delivered Succesfully")
    return render(request, 'vol_del.html', locals())





def view_alldetail1(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation = Donation.objects.get(id=pid)
    gallery = Gallery.objects.get(donation=donation)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

    try:

        Gallery.objects.get(donation=donation,deliverypic=deliverypic)
        error = "no"

    except:
        error = "yes"

    return render(request, 'view_alldetail1.html', locals())



def view_alldetail2(request, pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    donation = Donation.objects.get(id=pid)
    gallery = Gallery.objects.get(donation=donation)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

    try:

        Gallery.objects.get(donation=donation,deliverypic=deliverypic)
        error = "no"

    except:
        error = "yes"

    return render(request, 'view_alldetail2.html', locals())



def voldonation_notrec(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer,status="Donation NotReceived")
    return render(request, 'voldonation_notrec.html', locals())





def gallery(request, pid):

    donation = Donation.objects.get(id=pid)
    gallery = Gallery.objects.get(donation=donation)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

    try:

        Gallery.objects.get(donation=donation,deliverypic=deliverypic)
        error = "no"

    except:
        error = "yes"

    return render(request, 'gallery.html', locals())




def gallery_ind(request):

    donor = Donor.objects.all()
    donation = Donation.objects.filter(status="Donation Delivered Succesfully")
    gallery = Gallery.objects.all()
    return render(request, 'gallery_ind.html', locals())

