from django.shortcuts import render
from .models import bookMark
from .forms import bookMarkForm


def ytpList(request):


   book = bookMark.objects.all()


   regu = book.filter(cate__title = "music").order_by('-id')
   wier = book.filter(cate__title = "wierd").order_by('-id')
   got = book.filter(cate__title = "GOT").order_by('-id')

   form = bookMarkForm()


   content ={
      "book":book,
      "regu":regu,
      "wier":wier,
      "got":got,
      "form":form,

      }

   if request.method == 'POST':
        form = bookMarkForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bff/ytpList.html', content)
        else:
            return render(request, 'bff/error.html', content)
   else:

        return render(request,'bff/ytpList.html',content)

   return render(request, 'bff/ytpList.html', content )
