from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nepal.html')


def mount_page(request,pk):
    if pk == 'chomolungma':
        return render(request, 'chomolungma.html')

