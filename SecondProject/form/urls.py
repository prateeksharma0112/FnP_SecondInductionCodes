from django.urls import path
from . import views

# url patterns for CRUD App
urlpatterns = [
        path('', views.crudoperation, name="crud_operation"),             # Path define for Home Page
        path('request/', views.getPostMethod, name="get_post_method"),    # Path Define for Home Page/request
        path('layout/', views.layout, name="layout_design"),              # Path Define for Home Page/layout
    ]
