from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.


def index(request):

    

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})
    
    
    #index.html

    # user_input_name = request.POST['name']
    # user_input_text = request.POST['text']

    # new_row = GuessNumbers(name=user_input_name, text=user_input_text, num_lotto=10)

    # print(new_row.num_lotto)
    # print(new_row.name)

    # new_row.name = new_row.name.upper()
    # new_row.lottos = [ np.randint(1,50) for i in range(6) ]

    # new_row.save()

def post(request) :

    if request.method == "POST" : 
        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form' : form})



def hello(request):
    return HttpResponse("<h1 style='color:red;'> Hello World </h1>")


def detail(request,lottokey):
    lotto = GuessNumbers.objects.get(id=lottokey)
    return render(request, "lotto/detail.html",{"lotto":lotto})