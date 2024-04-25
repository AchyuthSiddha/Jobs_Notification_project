from django.contrib import admin

# Register your models here.


from app.models import Hyd_job,Pune_jobs,Bang_jobs

class Hyderabad(admin.ModelAdmin):
    list_display=['date','company','title','Eligibilty','Address','Email','Phone']

admin.site.register(Hyd_job,Hyderabad)


class Pune(admin.ModelAdmin):
    list_display=['date','company','title','Eligibilty','Address','Email','Phone']

admin.site.register(Pune_jobs,Pune)


class Bangalore(admin.ModelAdmin):
    list_display=['date','company','title','Eligibilty','Address','Email','Phone']

admin.site.register(Bang_jobs,Bangalore)