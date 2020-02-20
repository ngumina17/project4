# fit/urls.py
from django.urls import path
from . import views

# urlpatterns = [
#     path('/', views.user_dashboard, name='user_dashboard'),
# ]

urlpatterns = [
    path('', views.user_dashboard, name ='user_dashboard'),
    # path('camp/<int:pk>', views.camp_detail, name='camp_detail'),
    # path('camp/new', views.camp_create, name = 'camp_create'),
    # path('review/<int:pk>', views.review_detail, name='review_detail'),
    # path('review/new/<int:pk>', views.review_create, name = 'review_create'),
]