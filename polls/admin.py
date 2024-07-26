from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 Form field의 순서지정
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        ("Main Content", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]
admin.site.register(Question, QuestionAdmin)