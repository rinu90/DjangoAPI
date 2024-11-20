from blog.models import Post
from django import forms
import django_filters

class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}), lookup_expr='date__exact')

    class Meta:
        model = Post
        fields = ['created_on']