from django.shortcuts import render,HttpResponse
# from . forms import ProductForm
# from . forms import StudentForm
from . forms import *
from django.forms import modelformset_factory

# Create your views here.

def index(request):
    formset = modelformset_factory(Category,fields =['name'], extra = 3)
    return render(request,'main/index.html',{'form':formset})

# def index(request):
#     form = ProductForm()
#     return render(request,'main/index.html',{'form':form})

# def index(request):
#     form = StudentForm()
#     return render(request,'main/index.html',{'form':form})


# def index(request):
#     form = ProductForm()
#     return render(request,'main/index.html',{'form':form})


# def index(request):
#     # print(request.GET)
#     print(request.POST)
#     return render(request,'main/index.html')

# def index(request):
#     context = {}
#     form = ProductForm(request.POST or None)
#     context['form'] = form
#     return render(request,'main/index.html',context)

# def index(request):
#     post = PostForm()

#     if request.method == 'POST':
#         post = PostForm(request.POST)

#         if post.is_valid:
#             post = post.save(commit=False)
#             post.save()
#             return HttpResponse('<h3>form submited</h3>')
#         else:
#             return HttpResponse('<h3>unable to submit form</h3>')
#     return render(request,'main/index.html',{'form':post})


