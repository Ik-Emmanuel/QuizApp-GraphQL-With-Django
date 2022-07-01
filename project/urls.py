from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls'))
]
admin.site.site_header = "GraphQL Quiz APP"
admin.site.site_title = "Quiz APP Admin Portal"
admin.site.index_title = "Welcome to Quizz App Admin Portal"