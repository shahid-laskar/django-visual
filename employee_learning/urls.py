from django.urls import path
from .views import CourseCreate, CourseDelete, CourseDetail, CourseList, CourseUpdate

urlpatterns=[
    path('course-list/', CourseList.as_view(), name='course_list'),
    path('course-create/', CourseCreate.as_view(), name='course_create'),
    path('course-update/<int:pk>/',CourseUpdate.as_view(), name='course_update'),
    path('course-detail/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('course-delete/<int:pk>/', CourseDelete.as_view(), name='course_delete'),
]