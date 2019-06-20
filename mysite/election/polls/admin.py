from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):

	search_fields = ["question_text"]
	#list_display = ('question_text')
	fieldsets = [
		(Question, {'fields' : ['question_text']}),
	]
	inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)