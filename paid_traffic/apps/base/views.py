# Imports related with Django render
from django.shortcuts import render

# Imports related with groups
from django.contrib.auth.decorators import user_passes_test
from libs.scripts.userpermits import in_group

@user_passes_test(lambda u: in_group(u, 'reader'))
def change_me(request):
    context = {}
    return render(request, 'base.html', context)