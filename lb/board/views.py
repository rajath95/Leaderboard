from django.shortcuts import HttpResponse
from django.shortcuts import render



# Create your views here.

def ref_board(request):
    return HttpResponse("Welcome")

def board(request):
    return render(request,'board/board.html',context=None)
