from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('own_movie/', views.ListOwnMovieView.as_view(), name='get_own_movies'),
    path('<str:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    path('review',views.ListCreateReviewAPIView.as_view(),name='get_post_review'),
    path('report',views.ListCreateReportAPIView.as_view(),name='get_report'),
    path('review/<str:pk>/',views.RetrieveUpdateDestroyRatingAPIView.as_view(),name='get_post_review_update_delete')
]