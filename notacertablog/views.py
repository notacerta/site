from django.shortcuts import render
from .models import post
from .forms import PostForm
from django.utils import timezone
from django.contrib import messages


def index(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.ip = str(get_client_ip(request))
			post.created_date = timezone.now()
			messages.success(request, 'Obrigado!')
			post.save()
			form = PostForm()
		else:
			messages.warning(request, 'Ocorreu um erro no preenchimento do formulário. Por favor, revise as informações inseridas.') 
			form = PostForm(request.POST)
	else:
		form = PostForm()
	return render(request, 'notacertablog/index.html', {'form': form})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def sobre(request):
	return render(request, 'notacertablog/sobre.html')

def produto(request):
	return render(request, 'notacertablog/produto.html')