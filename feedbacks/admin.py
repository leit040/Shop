from django.contrib import admin

from feedbacks.models import Feedback


# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    ...

