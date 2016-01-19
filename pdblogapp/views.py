
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

#from django documentation for paginator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
	posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	paginator = Paginator(posts_list, 25) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	#return render(request, 'pdblogapp/post_list.html', {'posts': posts})
	return render(request, 'pdblogapp/index.html', {'posts': posts})




#create a 2nd view called post_detail
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'pdblogapp/post_detail.html', {'post': post})
	#return render(request, 'pdblogapp/index.html', {'post': post})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request,'pdblogapp/post_edit.html',{'form' : form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST or None, request.FILES or None, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'pdblogapp/post_edit.html' ,{'form' : form})
	
			

#