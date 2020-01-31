"""Define padrões de URL para learnin_logs."""

from django.urls import path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    re_path(r'^$', views.index, name='index'),

    # Mostra todos os assuntos
    re_path(r'^topics/$', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
