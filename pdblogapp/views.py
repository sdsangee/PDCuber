from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'pdblogapp/post_list.html', {'posts': posts})

#create a 2nd view called post_detail
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'pdblogapp/post_detail.html', {'post': post})

# Create your views here.
