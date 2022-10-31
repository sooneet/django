from django.shortcuts import render,HttpResponse
# from . forms import ProductForm
# from . forms import StudentForm
from . forms import *
# from django.forms import modelformset_factory

# Create your views here.
def index(request):
    form = TimeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            temp = form.cleaned_data.get('time')
            print(temp)
    return render(request,'main/index.html',{'form':form})


# def index(request):
#     form = AddressForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             temp = form.cleaned_data.get('address')
#             print(temp)
#     return render(request,'main/index.html',{'form':form})


# def index(request):
#     form = ProductsForm(None)
#     if request.method == 'POST':
#         form = ProductsForm(request.POST ,request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             pic = form.cleaned_data.get('pic')
#             data = Products.objects.create(name=name,pic=pic)
#             data.save()     
#             print(data)       
#     return render(request,'main/index.html',{'form':form})


# def handle_uploaded_file(f):  
#     with open('main/upload/'+f.name, 'wb+') as destination:  
#         for chunk in f.chunks():
#             destination.write(chunk)  

# # Create your views here.
# def index(request):
#     context = {}
#     if request.POST:
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["geeks_field"])
#     else:
#         form = PostForm()
#     context['form'] = form
#     return render(request, "main/index.html", context)



# def index(request):
#     form = PostForm()
#     return render(request,'main/index.html',{'form':form})

# def index(request):
#     formset = modelformset_factory(Category,fields =['name'], extra = 3)
#     return render(request,'main/index.html',{'form':formset})

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


