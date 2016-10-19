from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def test(request, pk1, pk2):
    ret = '%s %s' % (pk1, pk2)
    return_url = reverse('test', args=(pk1, pk2,))
    print(return_url)
    return HttpResponse(ret)


def error(request):
    error_message = request.POST.get('error_message')
    context = {
        'error_message': error_message
    }
    return render(request, 'common/error.html', context)
