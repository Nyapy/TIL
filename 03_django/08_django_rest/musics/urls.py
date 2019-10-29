from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        # 필수인자
        title = "Music API",
        default_version= "v1",
        # 선ㅌ택인자
        description = "음악 관련 API  ",
        terms_ofservice="https://www.google.com/policies/terms/",
        contact= openapi.Contact(email="nyapy@naver.com"),
        license= openapi.License(name="SSAFY License"),
    
    )
)

app_name = 'musics'

urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_pk>/', views.music_detail, name = 'music_detail'),
    path('musics/<int:music_pk>/comments/', views.comments_create, name = 'comments_create'),

    path('comments/<int:comment_pk>/', views.comments_update_and_delete, name='comments_update_and_delete'),
    path('artists/', views.artist_list, name='music_artists'),
    path('artists/<int:artist_pk>/', views.artist_detail, name = 'artist_detail'),
    path('docs/', schema_view.with_ui, name = 'api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
