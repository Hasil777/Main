from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('<slug:post_id>/comment/', views.post_comment, name='post_comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
