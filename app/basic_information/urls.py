from django.urls import path
from .views import test, mypage, LoginView, SignUpView, QuestionCreateView
from django.contrib.auth.views import LogoutView
from .views import quiz_view


urlpatterns = [
    path('test/', test, name='test'),
    path('login/', LoginView.as_view(), name='login'),
    path('mypage/', mypage, name='mypage'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('quiz/', quiz_view, name='quiz'),
    path('question/create/', QuestionCreateView.as_view(), name='questionCreate'),
    ]