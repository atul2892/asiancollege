from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homePage),
    # path('', views.whyPage),
    path('about-detail/<int:id>/',views.aboutDetail),
    path('program-detail/<int:id>/',views.programDetail),
    path('subprogram1/<int:id>/', views.subprogramOne),
    path('subprogram2/<int:id>/', views.subprogramTwo),
    path('subprogram3/<int:id>/', views.subprogramThree),
    path('academics-detail/<int:id>/',views.academicsDetail),
    path('student-detail/<int:id>/',views.studentDetail),
    path('facility-detail/<int:id>/',views.facilityDetail),
    path('legal-aid-cell/',views.legalAidCell),
    path('anti-ragging/',views.antiRaggingCell),
    path('notice-board/',views.noticeBoard),
    path('admission/',views.admission),
    path('career2/', views.careerTwoPage),
    path('dress2/', views.dressTwoPage),
    path('program2/', views.programTwoPage),
    path('principal-desk/',views.principalsDesk),
    path('admission-years/',views.admissionYears),
    path('personal-interview/',views.personalInterview),
    path('important-link/',views.importantLinks),
    path('contact/', views.contectPage),
    path('gallery/', views.galleryPage),
    
    
    
    path('mission/', views.missionPage),
    path('principal/', views.principalPage),
    path('programs1/', views.programOne),
    path('programs2/', views.programTwo),
    path('programs3/', views.programThree),
    path('academic1/', views.academicOne),
    path('academic2/', views.academicTwo),
    path('academic3/', views.academicThree),
    path('studentpro/', views.studentOne),
    path('studentreg/', views.studentTwo),
    path('studentsta/', views.studentThree),
    path('facility1/', views.facilityOne),
    path('facility2/', views.facilityTwo),
    path('facility3/', views.facilityThree),
    path('facility4/', views.facilityFour),
    path('legal/', views.legalPage),
    path('student/', views.studentPage),
    path('anti/', views.antiPage),
    path('notice/', views.noticePage),
    path('llb5/', views.llbPage),
    path('adm/', views.admPage),
    path('interview/', views.interviewPage),
    path('links/', views.linksPage),
    
    
    # path('index/', views.indexPage),
    # path('about/', views.aboutPage),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
