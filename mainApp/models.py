from django.db import models
from ckeditor.fields import RichTextField

class about(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    
class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    career_opportunities = RichTextField(default="",blank=True,null=True)
    dress_code = RichTextField(default="",blank=True,null=True)
    program_content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Academic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Facilitie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Legal_Aid_Cell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Student_Registration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Anti_Ragging_Cell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Notice_Board(models.Model):
    id = models.AutoField(primary_key=True)
    ref_no = models.CharField(max_length=10)
    details = models.TextField()
    date = models.CharField(max_length=100)
    downloads = models.FileField(upload_to="uploads/")
    
    
    def __str__(self):
        return "Notice"+" "+self.ref_no
    
class Admission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    career_opportunities = RichTextField(default="",blank=True,null=True)
    dress_code = RichTextField(default="",blank=True,null=True)
    program_content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Principals_Desk(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class AdmissionYears(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Personal_Interview(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField(default="",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Important_Links(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    link = models.TextField()
    
    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads")
    
    def __str__(self):
        return "Image"+" "+str(self.id)
    
class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()    
    
    def __str__(self):
        return self.name
    
class StudentRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    high_school = models.CharField(max_length=15)
    intermediate = models.CharField(max_length=15)
    graduation = models.CharField(max_length=15)
    post_graduation = models.CharField(max_length=15)
    gender = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    applying_for = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_name
    
class Admission_Prospectus(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="uploads/")
    
    def __str__(self):
        return "File"+" "+str(self.id)
    
class Holiday_List(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to="uploads/")
    
    def __str__(self):
        return "File"+" "+str(self.id)

    



