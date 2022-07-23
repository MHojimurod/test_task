from django.urls import path
from myapp.views import CreateUserView,UpdateUserView,GetUserView

urlpatterns = [
    path("get_user/<int:pk>",GetUserView.as_view()),
    path("create_user",CreateUserView.as_view()),
    path("update_user",UpdateUserView.as_view()),
]