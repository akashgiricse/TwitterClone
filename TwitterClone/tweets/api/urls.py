from django.conf.urls import url
# from .views import tweet_detail_view, tweet_list_view
from django.views.generic.base import RedirectView
from .views import (
    TweetListAPIView
)


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'),
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
