from django.shortcuts import render
from django.contrib import admin, auth

# We don't need a user management
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)


def index(request):
    return render(request, 'index.html')


def about_me(request):
    return render(request, 'about-me.html')


def a_lot_tech(request):
    techs = {
        'Language': ['Python', 'HTML', 'JavaScript', 'Sass'],
        'Framework': ['Django', 'Semantic UI'],
        'Package Manager': ['PyPI', 'NPM', 'Bower'],
        'Platform': ['GitHub', 'Heroku', 'Travis-CI'],
        'Database': ['PostgreSQL', 'SQLite']
    }
    return render(request, 'a-lot.html', locals())
