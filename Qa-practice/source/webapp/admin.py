from django.contrib import admin

from .models import *

class FrontAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    list_filter = ('white_name_button', 'black_name_button', 'title')

    def save_model(self, request, obj, form, change):
        existing_record = Front.objects.filter(id__lte=1).first()
        if existing_record:
            if obj.id != existing_record.id:
                return

        super().save_model(request, obj, form, change)

admin.site.register(Front, FrontAdmin)

class AdminDatasets(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title', 'content')

admin.site.register(Datasets, AdminDatasets)

class AdminStatistics(admin.ModelAdmin):
    list_display = ('numbers', 'title')
    list_filter = ('numbers', 'title')

admin.site.register(Statistics, AdminStatistics)

class AdminMentors(admin.ModelAdmin):
    list_display = ('full_name', 'description')
    list_filter = ('full_name', 'description')

admin.site.register(Mentors, AdminMentors)

class AdminCourses(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title', 'content', 'course_type')

admin.site.register(Courses, AdminCourses)

class AdminOffersBlack(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title', 'content', 'subtitle')

admin.site.register(OffersBlack, AdminOffersBlack)

class AdminOffers(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title', 'content')

admin.site.register(Offers, AdminOffers)

admin.site.register(Gratitude)

class AdminSpeakers(admin.ModelAdmin):
    list_display = ('title', 'offer_1')
    list_filter = ('title', 'offer_1')

admin.site.register(Speakers, AdminSpeakers)
