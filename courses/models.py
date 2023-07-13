from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=512)
    code = models.IntegerField(default=1)
    start_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'speciality'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    ASISTENT = 'Asistent'
    PROFESSOR = 'Professor'
    DOCTOR = 'Doctor'
    role = (
        (ASISTENT, 'Asistent'),
        (PROFESSOR, 'Professor'),
        (DOCTOR, 'Doctor'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=10, choices=role)

    def __str__(self):
        return f"{self.degree} {self.first_name} {self.last_name}"

    class Meta:
        db_table = 'teacher'

class Subject(models.Model):
    name = models.CharField(max_length=200)
    specialities = models.ManyToManyField(Speciality)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fan(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fan'

