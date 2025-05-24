from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    
class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    # students = models.ManyToManyField(Student, through="CourseStudent")

    def __str__(self):
        return self.title

# s1 =  Student.objects.get(id=1)
# s1.courses

# s1.dept.student_set.all()

class Student(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='students')
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='default.png', upload_to='images/student_images', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(Course, through='StudentCourse')

    def __str__(self):
        return f"{self.name} | {self.phone}"

class StudentCourse(models.Model):
    GRADE_CHOICES = (
        ("Excellent", "Excellent"),
        ("Very Good", "Very Good"),
        ("Good", "Good"),
        ("Fair", "Fair"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10,choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.student.name} | {self.course.title} | {self.grade}"

# class CourseStudent(models.Model):
#     GRADE_CHOICES = (
#         ("Excellent", "Excellent"),
#         ("Very Good", "Very Good"),
#         ("Good", "Good"),
#         ("Fair", "Fair"),
#     )
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
#     grade = models.CharField(max_length=200, choices=GRADE_CHOICES, null=True, blank=True)
#     fees = models.IntegerField(default=0)
    
#     def __str__(self):
#         return f"{self.course} | {self.student.name} | {self.grade}"
    
#     class Meta:
#         unique_together = ('course', 'student')
