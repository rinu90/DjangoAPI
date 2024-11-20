from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from blog.serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsPostPossessor
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from blog.filter import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class PostView(ModelViewSet):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsPostPossessor]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = PostFilter
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.all()
        #return Post.objects.filter(created_by=self.request.user)


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Change the number per page as needed
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    return render(request, 'index.html', {'posts': posts})

from django.shortcuts import render

@api_view(['GET'])
def indexR(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    postss = serializer.data
    #return render(request, 'indexR.html', {'posts': postss})
    return Response(postss)






'''def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})'''
