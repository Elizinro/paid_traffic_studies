# Imports related with Django render
from django.shortcuts import render
from django.http import JsonResponse

# Impots realted to tests TODO, change in future
from libs.scripts.facebook_api import ad_account_id
from libs.scripts.facebook_api import AdAccount
import pandas as pd

# Imports related with groups
from django.contrib.auth.decorators import user_passes_test
from libs.scripts.userpermits import in_group

# Show the colors to the developers groups see the color, using the method called as 'ARC(Ajax Render Content)'
# , wrote in 'README.md', in this case when click in a button called #show-colors-button in the header, do the
# ARC of the template colors, if want to change something, just change the template colors.html
@user_passes_test(lambda u: in_group(u, 'developer'))
def colors(request):
    context = {}
    rendered = render(request, "colors.html", context)
    return JsonResponse({'colors_template': rendered.content.decode()})

# Starts dashboard
@user_passes_test(lambda u: in_group(u, 'reader'))
def dashboard(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

# Class that works all the change_dashboard_screens, initialy using the codes inside this class, in a nearly
# future, could use call of defs in the library or other place to resume the code
class DashboardScreens:
    def main_dashboard(self, request):
        context = {}
        return render(request, 'dashboard/main/main.html', context)

# Final function TODO, add a real description about that
@user_passes_test(lambda u: in_group(u, 'dashboard'))
def change_dashboard_screen(request):
    options = request.GET.get('select-dashboard-screen')
    match options:
        case "main":
            dashboard_type = "main_dashboard"
        # Add others buttons inside the aside bar of the dashboard, and add here the option to call the dashboard
        # type in the class DashboardScreens, before that description
        case _:
            pass
    try:
        rendered = getattr(DashboardScreens(), dashboard_type)(request)
    except AttributeError as e:
        raise e
    return JsonResponse({'selected_dashboard_screen': rendered.content.decode()})