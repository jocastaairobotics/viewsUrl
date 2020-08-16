from django.db import models

# Create your models here.
from django.db import models

class Universitie(models.Model):
    Universities = [("Savitribai Phule Pune Universities","Savitribai Phule Pune Universities"),]
    universitie = models.CharField(max_length=100,choices=Universities)

    def __str__(self):
        return self.universitie

class Department(models.Model):
    Departments = [ ('First Year','First Year'),
                    ('Mechanical Engineering','Mechanical Engineering'),
                    ('Mechanical Sandwitch Engineering','Mechanical Sandwitch Engineering'),
                    ("Electronics And Telecommunication Engineering","Electronics And Telecommunication Engineering"),
                    ("Electrical Engineering","Electrical Engineering"),
                    ("Computer Engineering","Computer Engineering"),
                    ("Civil Engineering","Civil Engineering"),
                    ("Instrumentation Engineering","Instrumentation Engineering"),
                    ("Chemical Engineering","Chemical Engineering"),
                    ("Information Technology Engineering","Information Technology Engineering"),]
    universities = models.ForeignKey(to=Universitie,null=False, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,choices=Departments)

    def __str__(self):
        return self.department

class Subject(models.Model):
    pattern = [("2015","2015"),
               ("2019","2019"),]
    Class=[("First Year","First Year"),
            ("Second Year","Second Year"),
            ("Third Year","Third Year"),
            ("Fourth Year","Fourth Year"),]
    
    SEM = [("Semester 1","Semester 1"),
           ("Semester 2","Semester 2"),
           ("Semester 3","Semester 3"),
           ("Semester 4","Semester 4"),
           ("Semester 5","Semester 5"),
           ("Semester 6","Semester 6"),
           ("Semester 7","Semester 7"),
           ("Semester 8","Semester 8"),]
    Department = models.ForeignKey(to=Department,on_delete=models.CASCADE)
    patterns = models.CharField(max_length=50,choices = pattern)
    Classes = models.CharField(max_length=100,choices=Class)
    Sem = models.CharField(max_length=50,choices=SEM)
    Subjects = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Department) + "<-" + str(self.patterns) +"<-"+ str(self.Subjects)

class Chapter(models.Model):
    Subjects = models.ForeignKey(to=Subject,on_delete=models.CASCADE)
    Chapter = models.CharField(max_length=100)

    def __str__(self):
        return self.Chapter

class Topic(models.Model):
    subjects = models.ForeignKey(to=Chapter,on_delete=models.CASCADE)
    Topic_Name = models.CharField(max_length=100,null=True)
    Topic_Description = models.TextField(max_length=1000,null=True)
    Topic_video = models.FileField(upload_to="Videos")
    Topic_Notes = models.FileField(upload_to="Notes")

    def __str__(self):
        return self.Topic_Name