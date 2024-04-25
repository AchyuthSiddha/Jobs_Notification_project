import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Achyuth_jobs_portal.settings')

import django

django.setup()

from faker import Faker

from app.models import *

from random import *

fake=Faker()

def Phonenumber():
    d=randint(6,9)
    num=''+str(d)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def Infor(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','Team Lead','Team Head','Business Analyst','Developer','Tester','HR'))
        felgiblity=fake.random_element(elements=('MBA','MCA','M.Tech','B.Tech','BSC','Bcom','BE'))
        faddr=fake.address()
        femail=fake.email()
        fphone=Phonenumber()
        Hyd_job_record=Hyd_job.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,Eligibilty=felgiblity,Address=faddr,Email=femail,Phone=fphone)
        Pune_job_record=Pune_jobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,Eligibilty=felgiblity,Address=faddr,Email=femail,Phone=fphone)
        Bang_job_record=Bang_jobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,Eligibilty=felgiblity,Address=faddr,Email=femail,Phone=fphone)
    

n=int(input("enter a number of records:"))
Infor(n)
print(f'{n} record sucesfully inserted......')