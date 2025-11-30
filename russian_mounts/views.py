from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'russian.html')


def russian_mounts_pages(request,pk):
    if pk == 'elbrus':
        return render(request, 'elbrus.html')
    elif pk == 'dykhtau':
        return render(request, 'dykhtau.html')
    elif pk == 'koshtan_tau':
        return render(request, 'koshtan_tau.html')
    elif pk == 'mizhirgi':
        return render(request, 'mizhirgi.html')
    elif pk == 'pushkin_peak':
        return render(request, 'pushkin_peak.html')
    elif pk == 'dzhangi_tau':
        return render(request, 'dzhangi_tau.html')
    elif pk == 'shkhara':
        return render(request, 'shkhara.html')
    elif pk == 'kazbek':
        return render(request, 'kazbek.html')
    elif pk == 'klyuchevskaya_sopka':
        return render(request, 'klyuchevskaya_sopka.html')
    elif pk == 'belukha':
        return render(request, 'belukha.html')