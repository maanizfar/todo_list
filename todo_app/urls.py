from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from todo_app.views import home_view, CreatTaskView, EditTaskView, DeleteTaskView


urlpatterns = [
    path('', home_view, name='home'),
    path('new_task/', CreatTaskView.as_view(), name='new_task'),
    path('<int:pk>/edit_task/', EditTaskView.as_view(), name='edit_task'),
    path('<int:pk>/delete_task/', DeleteTaskView.as_view(), name='delete_task'),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
