from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Tweet
# Create your views here.


class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()


# def tweet_detail_view(request, id=1):

#     obj = Tweet.objects.get(id=id)  # GET from database
#     print(obj)
#     context = {
#         "object": obj
#     }

#     return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):

#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset

#     }

#     return render(request, "tweets/list_view.html", context)
