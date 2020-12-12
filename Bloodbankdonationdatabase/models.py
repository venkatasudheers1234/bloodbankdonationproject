from django.db import models

class donor(models.Model):
    donor_id=models.CharField(max_length=20)
    donorname=models.CharField(max_length=25)
    donor_age=models.IntegerField()
    gender=models.CharField(max_length=10)
    medical_history=models.CharField(max_length=20)
    weight=models.IntegerField()
    donor_phone_no=models.CharField(max_length=10)
    donor_address=models.CharField(max_length=25)

    def __str__(self):
        return self.donorname


class blood(models.Model):
    blood_Id=models.CharField(max_length=15)
    blood_Type=models.CharField(max_length=5)
    date=models.DateField()
    time=models.TimeField()
    donor_id=models.CharField(max_length=15)
    blood_Quantity = models.CharField(max_length=15)
    bloodBank_id = models.CharField(max_length=15)


    def __str__(self):
        return self.blood_Type
#

#
class bloodBank(models.Model):
    bloodBank_Id = models.CharField(max_length=20)
    bloodBank_Name = models.CharField(max_length=30)
    bloodBank_Phone_no=models.CharField(max_length=15)
    bloodBank_Address=models.CharField(max_length=40)
    bloodBank_Email=models.CharField(max_length=15)


    def __str__(self):
        return self.bloodBank_Name

#

#
class hospital(models.Model):
    hospital_Id = models.CharField(max_length=20)
    hospital_Name = models.CharField(max_length=30)
    hospital_Phone_no=models.CharField(max_length=15)
    hospital_Address=models.CharField(max_length=40)
    blood_Type_Request=models.CharField(max_length=15)
    quantity=models.CharField(max_length=15)


    def __str__(self):
        return self.hospital_Name
#

#
class Employee(models.Model):
    employee_Id = models.CharField(max_length=20)
    employee_Name = models.CharField(max_length=30)
    employee_Phone_no=models.CharField(max_length=15)
    employee_Address=models.CharField(max_length=40)
    employee_Email=models.CharField(max_length=40)
    position=models.CharField(max_length=20)
    bloodBank_ID=models.CharField(max_length=20)


    def __str__(self):
        return self.employee_Name
#

class orders(models.Model):
    hospital_Id = models.CharField(max_length=20)
    BloodBank_Id = models.CharField(max_length=30)
    Blood_Type_Request=models.CharField(max_length=15)

    def __str__(self):
        return self.hospital_Id











# Create your models here.
