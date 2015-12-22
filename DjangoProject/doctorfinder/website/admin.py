from django.contrib import admin
from .models import Insurance, Review, User, Doctor, FavoriteDoctors


class InsuranceAdmin (admin.ModelAdmin):
	list_display=['name','doctor']
admin.site.register(Insurance, InsuranceAdmin)

class ReviewAdmin (admin.ModelAdmin):
	list_display=['rating','comment', 'doctor','patient','date']
admin.site.register(Review, ReviewAdmin)

class UserAdmin (admin.ModelAdmin):
	list_display=['name','username','password','type']
admin.site.register(User, UserAdmin)

class DoctorAdmin (admin.ModelAdmin):
	list_display=['username','phoneNumber','officeHours','speciality','rating','availability','state','city','zip','street','education','awards','experience']
admin.site.register(Doctor, DoctorAdmin)

class FavoriteDoctorsAdmin (admin.ModelAdmin):
	list_display=['patient','doctor']
admin.site.register(FavoriteDoctors, FavoriteDoctorsAdmin)

