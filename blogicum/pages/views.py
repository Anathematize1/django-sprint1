from django.shortcuts import render


def about(request):
    """отображает страницу 'О нас'."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страницу с правилами проекта."""
    return render(request, 'pages/rules.html')
