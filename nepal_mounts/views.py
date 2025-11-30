from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nepal.html')


def nepal_mounts_pages(request,pk):
    if pk == 'chomolungma':
        return render(request, 'chomolungma.html')
    elif pk == 'kanchenjunga':
        return render(request, 'kanchenjunga.html')
    elif pk == 'lhotse':
        return render(request, 'lhotse.html')
    elif pk == 'makalu':
        return render(request, 'makalu.html')
    elif pk == 'cho_oyo':
        return render(request, 'cho_oyo.html')
    elif pk == 'dhaulagiri':
        return render(request, 'dhaulagiri.html')
    elif pk == 'manaslu':
        return render(request, 'manaslu.html')
    elif pk == 'annapurna':
        return render(request, 'annapurna.html')
    elif pk == 'ama_dablam':
        return render(request, 'ama_dablam.html')




