from django.db import models

# Create your models here.
class Universitie(models.Model):
    Universities = [("Savitribai Phule Pune Universities","Savitribai Phule Pune Universities"),
    ("Gate","Gate"),
    ("Indian Engineering Services","Indian Engineering Services"),]

    universitie = models.CharField(max_length=100,choices=Universities)
    def __str__(self):
        return self.universitie

class Department(models.Model):
    Departments = [('First Year','First Year'),
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
    Year = models.CharField(max_length=100,choices=Class)
    Sem = models.CharField(max_length=50,choices=SEM)
    Subjects = models.CharField(max_length=100)

    def __str__(self):
        return self.Subjects

class Pre_Q_Paper(models.Model):
    Semester = [("Winter","Winter"),
                ("Summer","Summer"),]
    pattern = [("2015","2015"),
               ("2019","2019"),]
    semester = models.CharField(max_length=50,choices = Semester)
    Subjects = models.ForeignKey(to=Subject,on_delete=models.CASCADE, related_name="subjects")
    patterns = models.CharField(max_length=50,choices = pattern)
    Subject_Name = models.CharField(max_length=100)
    papers = models.FileField(upload_to="Previous/")

    def __str__(self):
        return str(self.papers) + " --> " + str(self.Subjects)

class Gate(models.Model):
    Year = [("2016","2016"),
            ("2017","2017"),
            ("2018","2018"),
            ("2019","2019"),]
    Years = models.CharField(max_length=50,choices = Year)
    Department = models.ForeignKey(to=Department,on_delete=models.CASCADE)
    Subjects = models.CharField(max_length=30)
    papers = models.FileField(upload_to="Competative/")

    def __str__(self):
        return str(self.Department) + " " + str(self.Subjects)

class Indian_Engineering_Services(models.Model):
    Year = [("2016","2016"),
            ("2017","2017"),
            ("2018","2018"),
            ("2019","2019"),]
    Years = models.CharField(max_length=50,choices = Year)
    Department = models.ForeignKey(to=Department,on_delete=models.CASCADE)
    Subjects = models.CharField(max_length=30)
    papers = models.FileField(upload_to="Indian_Engineering_Services/")

    def __str__(self):
        return str(self.Department) + " " + str(self.Subjects)