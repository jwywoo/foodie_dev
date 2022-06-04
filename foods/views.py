from django.shortcuts import render

from django.http import HttpResponse

# showing the main page
def main(request):
    return render(request, 'main.html', {})
