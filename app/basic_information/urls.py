from django.urls import path
from .views import test, mypage, LoginView, SignUpView, QuestionCreateView
from django.contrib.auth.views import LogoutView
from .views import question_view


urlpatterns = [
    path('', mypage, name='mypage'),
    path('test/', test, name='test'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('question/', question_view, name='question'),
    path('question/create/', QuestionCreateView.as_view(), name='question_create'),
    ]