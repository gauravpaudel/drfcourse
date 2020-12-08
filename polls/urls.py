from django.urls import path
from polls.views import PollListG,PollDetailG,ChoiceList, CreateVote


urlpatterns = [
    path('polls/',PollListG.as_view(),name='polls_list'),
    path('polls/<int:pk>/',PollDetailG.as_view(),name='polls_detail'),
    path('polls/<int:pk>/choices/',ChoiceList.as_view(),name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',CreateVote.as_view(),name='create_vote')
]