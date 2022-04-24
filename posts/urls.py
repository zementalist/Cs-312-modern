from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('create', views.create, name="create_post"), # GET
    path('store', views.store, name="store_post"),
    path('<int:id>', views.show, name='show_post'), # GET  (READ)
    path('<int:id>/edit', views.edit, name='edit_post'), # GET
path('findby/<str:username>', views.search_user, name='show_post'),
    path('<int:id>/update', views.update, name='update_post'), # PUT (UPDATE)
    path('<int:id>/delete', views.destroy, name='delete_post'),  # Delete (DELETE)

path('findby/user', views.find_by_user),
path('findby/title', views.find_by_title),
path('findby/<str:username>/<int:likes>/', views.find_by),

]
