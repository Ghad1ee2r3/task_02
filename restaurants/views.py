from django.shortcuts import render
def home(request):
    context = {
        "msg": "hello world ",
    }
    return render(request, 'home_page.html', context)
