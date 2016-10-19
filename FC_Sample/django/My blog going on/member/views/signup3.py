from django.shortcuts import render, redirect
from django.contrib.auth import login
from member.forms import SignupModelForm


def signup3(request):
    context = {}
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('blog:post_list')
        context['form'] = form
    else:
        form = SignupModelForm()
        context['form'] = form
    return render(request, 'member/signup2.html', context)
