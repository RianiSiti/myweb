# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    nama = "RIANI SITI N"
    buah = ['Apel', 'Anggur', 'Kelengkeng', 'Durian']
    return render(request,'index.html',{'nama':nama, 'buah':buah})

def about(request):
    return render(request, 'about.html')

def kontak(request):
    return render(request, 'kontak.html')      

def blog(request):
    return render(request, 'blog.html')       
