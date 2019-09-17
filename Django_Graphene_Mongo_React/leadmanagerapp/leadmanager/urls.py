from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('', include('leadmanager.frontend.urls')),
    path('', include('leadmanager.lead.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
