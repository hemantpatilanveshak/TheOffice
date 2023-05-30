from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from .serializers import BookListSerailizer

# Create your views here.
def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

# def getList(request):
#     obj = 

def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save() 
                
                return redirect('book-list')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 
                             'description': book.description,
                               'author': book.author, 
                               'year': book.year,
                               'picture':book.picture})
    if request.method == "POST":  
        form = BookForm(request.POST,request.FILES, instance=book )  
        if form.is_valid():  
            try:  
                form.save() 
                return redirect('/book-list')  
            except Exception as e: 
                pass    
    return render(request,'book-update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')


from rest_framework.views import APIView
from rest_framework.response import Response


class BookList(APIView):
    def get(self,request,id=None):
        if id is not None:
            obj = Book.objects.get(id= id)
            serializer = BookListSerailizer(obj,context = {"request":request})
            data = serializer.data
            print(data)
            return Response({"msg":"Data Fetched","data":data})
        
        else:  
            
            obj = Book.objects.all()
            serializer = BookListSerailizer(obj,context = {"request":request},many = True)
            data = serializer.data
            return Response({"msg":"Data Fetched","data":data})
            