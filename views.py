from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse


from .models import Category, Product, Comment
from .forms import UserCommentForm

def simple_ajax(request):
    form = UserCommentForm
    return render(request, 'store/simple_ajax.html', {"UserCommentForm": form})

def simple_ajax_test(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == "POST" and is_ajax:
        form = UserCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
    else:
        form = UserCommentForm()
