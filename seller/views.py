from django.shortcuts import render

# Create your views here.
def seller_dashboard_view(request):
    return render(request , 'seller_dashboard.html')

def profile_view(request):
    return render(request , 'seller_profile.html')



