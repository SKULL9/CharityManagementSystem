from django.contrib import admin
from django.urls import path
from charity.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('all_logins',all_logins,name='all_logins'),
    
    
    path('volunteer_login',volunteer_login,name='volunteer_login'),
    path('volunteer_reg',volunteer_reg,name='volunteer_reg'),
    path('admin_login',admin_login,name='admin_login'),
    
    
    path('donor_login',donor_login,name='donor_login'),    
    path('donor_reg',donor_reg,name='donor_reg'),
    path('donor_home',donor_home,name='donor_home'),
    
    
    
    path('logout/',Logout,name='logout'),
    path('donate_now',donate_now,name='donate_now'),
    path('donation_history',donation_history,name='donation_history'),
    path('admin_home',admin_home,name='admin_home'),
    path('pending_donation',pending_donation,name='pending_donation'),
    path('view_donationdetail/<int:pid>',view_donationdetail,name='view_donationdetail'),
    path('accepted_donation',accepted_donation,name='accepted_donation'),
    path('add_area',add_area,name='add_area'),
    path('manage_area',manage_area,name='manage_area'),
    path('edit_area/<int:pid>',edit_area,name='edit_area'),
    path('delete_area/<int:pid>',delete_area,name='delete_area'),
    path('manage_donor',manage_donor,name='manage_donor'),
    path('view_donordetail/<int:pid>',view_donordetail,name='view_donordetail'),
    path('delete_donor/<int:pid>',delete_donor,name='delete_donor'),
    path('volunteer_home',volunteer_home,name='volunteer_home'),
    path('new_volunteer',new_volunteer,name='new_volunteer'),
    path('view_volunteerdetail/<int:pid>',view_volunteerdetail,name='view_volunteerdetail'),
    path('accepted_volunteer',accepted_volunteer,name='accepted_volunteer'),
    path('rejected_volunteer',rejected_volunteer,name='rejected_volunteer'),
    path('all_volunteer',all_volunteer,name='all_volunteer'),
    path('delete_volunteer/<int:pid>',delete_volunteer,name='delete_volunteer'),
    path('accepted_donationdetail/<int:pid>',accepted_donationdetail,name='accepted_donationdetail'),

    path('donationcollection_detail/<int:pid>',donationcollection_detail,name='donationcollection_detail'),


    path('volunteer_assign/<int:pid>',volunteer_assign,name='volunteer_assign'),

    path('col_req',col_req,name='col_req'),

    path('voldonation_rec',voldonation_rec,name='voldonation_rec'),

    path('voldonation_details/<int:pid>',voldonation_details,name='voldonation_details'),

    path('view_alldetail/<int:pid>',view_alldetail, name='view_alldetail'),

    path('allocatedvolunteer_donation', allocatedvolunteer_donation, name='allocatedvolunteer_donation'),
    path('donationvolunteerallocated_detail/<int:pid>', donationvolunteerallocated_detail,name='donationvolunteerallocated_detail'),


    path('vol_Del',vol_Del,name='vol_Del'),

    path('all_donation',all_donation,name='all_donation'),

    path('view_alldetail1/<int:pid>',view_alldetail1, name='view_alldetail1'),
    path('view_alldetail2/<int:pid>',view_alldetail2, name='view_alldetail2'),

    path('voldonation_notrec',voldonation_notrec,name='voldonation_notrec'),


    path('gallery/<int:pid>',gallery,name='gallery'),

    path('gallery_ind',gallery_ind,name='gallery_ind'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)