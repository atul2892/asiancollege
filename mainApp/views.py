from django.shortcuts import render
from django.contrib import messages
from .models import *

def homePage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()   
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    context = {
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    }
    return render(Request,"home.html",context)

# def whyPage(Request):
#     aboutdata = about.objects.all()
#     return render(Request,"why.html",{"aboutdata":aboutdata})

def aboutDetail(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    abdata = about.objects.get(id=id)    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()
    
    return render(Request,"about-detail.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "abdata":abdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def programDetail(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    prdata = Program.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    return render(Request,"program-detail.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "prdata":prdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def subprogramOne(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    prdata = Program.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    return render(Request,"subprogram1.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "prdata":prdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def subprogramTwo(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    prdata = Program.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    return render(Request,"subprogram2.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "prdata":prdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def subprogramThree(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    prdata = Program.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    return render(Request,"subprogram3.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "prdata":prdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def academicsDetail(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    acddata = Academic.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    return render(Request,"academics-detail.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "acddata":acddata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def studentDetail(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    stddata = Student.objects.get(id=id)
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last()     
    
    
    return render(Request,"student-detail.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "stddata":stddata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def facilityDetail(Request,id):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    facdata = Facilitie.objects.get(id=id)    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"facility-detail.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "facdata":facdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def legalAidCell(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    lacdata = Legal_Aid_Cell.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"legal-aid-cell.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "lacdata":lacdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def antiRaggingCell(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    arcdata = Anti_Ragging_Cell.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"anti-ragging.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "arcdata":arcdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def noticeBoard(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    nbdata = Notice_Board.objects.all()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"notice-board.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "nbdata":nbdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def admission(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admdata = Admission.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"admission.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admdata":admdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def careerTwoPage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admdata = Admission.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"career2.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admdata":admdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def dressTwoPage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admdata = Admission.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"dress2.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admdata":admdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def programTwoPage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admdata = Admission.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"program2.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admdata":admdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def principalsDesk(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    prddata = Principals_Desk.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"principal-desk.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "prddata":prddata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def admissionYears(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    adydata = AdmissionYears.objects.get()   
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"admission-years.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "adydata":adydata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def personalInterview(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    pidata = Personal_Interview.objects.get()    
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"personal-interview.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "pidata":pidata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def importantLinks(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    ildata = Important_Links.objects.all()   
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"important-link.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "ildata":ildata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def studentTwo(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    if(Request.method=="POST"):
        str = StudentRegistration()
        str.student_name = Request.POST.get("name")
        str.fathers_name = Request.POST.get("fname")
        str.mothers_name = Request.POST.get("mname")
        str.dob = Request.POST.get("birthday")
        str.aadhar = Request.POST.get("aadhar")
        str.address = Request.POST.get("address")
        str.email = Request.POST.get("email")
        str.phone = Request.POST.get("mobile")
        str.high_school = Request.POST.get("tenth")
        str.intermediate = Request.POST.get("twelve")
        str.graduation = Request.POST.get("graduation")
        str.post_graduation = Request.POST.get("pgrade")
        str.gender = Request.POST.get("gender")
        str.category = Request.POST.get("cat")
        str.applying_for = Request.POST.get("apply")
        str.save()
        messages.success(Request,"Form Submitted Successfully!!!")
    
    return render(Request,"studentreg.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def contectPage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    if(Request.method=="POST"):
        cd = ContactDetail()
        cd.category = Request.POST.get("cat")
        cd.name = Request.POST.get("name")
        cd.address = Request.POST.get("address")
        cd.phone = Request.POST.get("phone")
        cd.email = Request.POST.get("email")
        cd.subject = Request.POST.get("subject")
        cd.message = Request.POST.get("message")
        cd.save()
        messages.success(Request,"Form Submitted Successfully!!!")
    return render(Request,"contact.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })

def galleryPage(Request):
    aboutdata = about.objects.all()
    facilitydata = Facilitie.objects.all()
    studentdata = Student.objects.all()
    academicdata = Academic.objects.all()
    programdata = Program.objects.all()
    gldata = GalleryImage.objects.all()
    admpdata = Admission_Prospectus.objects.last()
    hlddata = Holiday_List.objects.last() 
    
    return render(Request,"gallery.html",{
        "aboutdata":aboutdata,
        "facilitydata":facilitydata,
        "studentdata":studentdata,
        "academicdata":academicdata,
        "programdata":programdata,
        "gldata":gldata,
        "admpdata":admpdata,
        "hlddata":hlddata,
    })





def missionPage(Request):
    return render(Request,"mission.html")

def principalPage(Request):
    return render(Request,"principal.html")

def programOne(Request):
    return render(Request,"programs1.html")

def programTwo(Request):
    return render(Request,"programs2.html")

def programThree(Request):
    return render(Request,"programs3.html")

def academicOne(Request):
    return render(Request,"academic1.html")

def academicTwo(Request):
    return render(Request,"academic2.html")

def academicThree(Request):
    return render(Request,"academic3.html")

def studentOne(Request):
    return render(Request,"studentpro.html")



def studentThree(Request):
    return render(Request,"studentsta.html")

def facilityOne(Request):
    return render(Request,"facility1.html")

def facilityTwo(Request):
    return render(Request,"facility2.html")

def facilityThree(Request):
    return render(Request,"facility3.html")

def facilityFour(Request):
    return render(Request,"facility4.html")

def legalPage(Request):
    return render(Request,"legal.html")

def studentPage(Request):
    return render(Request,"student.html")

def antiPage(Request):
    return render(Request,"anti.html")

def noticePage(Request):
    return render(Request,"notice.html")

def llbPage(Request):
    return render(Request,"llb5.html")

def admPage(Request):
    return render(Request,"adm.html")

def interviewPage(Request):
    return render(Request,"interview.html")

def linksPage(Request):
    return render(Request,"links.html")





# def indexPage(Request):
#     return render(Request,"index.html")

# def aboutPage(Request):
#     return render(Request,"about.html")

