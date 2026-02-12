from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .forms import LoginForm, PostForm
from .models import com, menuu


# ---------------- БАЗОВІ ----------------

def start_page(request):
    if request.user.is_authenticated:
        return redirect('menu')
    return redirect('main')


def main(request):
    return render(request, 'main.html')


def menu(request):
    return render(request, 'menu.html')


def ohibka(request):
    return render(request, 'ohibka.html')








# ---------------- BREAKFEST ----------------

def breakfest(request):
    return render(request, 'breakfest/breakfest.html')


def sirniku(request):
  
    return render(request, 'breakfest/sirniku/sirniku.html',)
##############################

def sirniku_mal(request):
    comm = com.objects.filter(name__name='sirniku_mal')
    return render(request, 'breakfest/sirniku/mal.html', context={'comm': comm})

def sirniku_malcom(request):
    item = get_object_or_404(menuu, name='sirniku_mal')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("mal")
    else:
        form = PostForm()

    return render(request, 'breakfest/sirniku/malcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='sirniku_mal')
    return render(request, 'breakfest/sirniku/comp.html', context={'comm': comm})

###########################

def sirniku_shok(request):
    comm = com.objects.filter(name__name='sirniku_shok')
    return render(request, 'breakfest/sirniku/shok.html', context={'comm': comm})

def sirniku_shokcom(request):
    item = get_object_or_404(menuu, name='sirniku_shok')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("shok")
    else:
        form = PostForm()

    return render(request, 'breakfest/sirniku/shokcom.html', {"form": form, "item": item})


def comp(request):
    comm = com.objects.filter(name__name='sirniku_shok')
    return render(request, 'breakfest/sirniku/comp.html', context={'comm': comm})

###########################


def sol(request):
    comm = com.objects.filter(name__name='sirniku_sol')
    return render(request, 'breakfest/sirniku/sol.html', context={'comm': comm})

def sirniku_solcom(request):
    item = get_object_or_404(menuu, name='sirniku_sol')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sol")
    else:
        form = PostForm()

    return render(request, 'breakfest/sirniku/solcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'breakfest/sirniku/sol.html', context={'comm': comm})







######################

def tostu(request):
    return render(request, 'breakfest/tostu/tostu.html')

########################
def tostu_avo(request):
    comm = com.objects.filter(name__name='tostu_avo')
    return render(request, 'breakfest/tostu/avo.html', context={'comm': comm})

def tostu_avocom(request):
    item = get_object_or_404(menuu, name='tostu_avo')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("avo")
    else:
        form = PostForm()

    return render(request, 'breakfest/tostu/avocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='tostu_avo')
    return render(request, 'breakfest/tostu/comp.html', context={'comm': comm})

###############################


def tostu_chdj(request):
    comm = com.objects.filter(name__name='tostu_chdj')
    return render(request, 'breakfest/tostu/chdj.html', context={'comm': comm})

def tostu_chdjcom(request):
    item = get_object_or_404(menuu, name='tostu_chdj')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("chdj")
    else:
        form = PostForm()

    return render(request, 'breakfest/tostu/chdjcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='tostu_chdj')
    return render(request, 'breakfest/tostu/comp.html', context={'comm': comm})

###########################

def tostu_maldj(request):   
    comm = com.objects.filter(name__name='tostu_maldj')
    return render(request, 'breakfest/tostu/maldj.html', context={'comm': comm})

def tostu_maldjcom(request):
    item = get_object_or_404(menuu, name='tostu_maldj')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("maldj")
    else:
        form = PostForm()

    return render(request, 'breakfest/tostu/maldjcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='tostu_maldj')
    return render(request, 'breakfest/tostu/comp.html', context={'comm': comm})


########################

def tostu_poldj(request):
    comm = com.objects.filter(name__name='tostu_poldj')
    return render(request, 'breakfest/tostu/poldj.html', context={'comm': comm})

def tostu_poldjcom(request):
    item = get_object_or_404(menuu, name='tostu_poldj')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("poldj")
    else:
        form = PostForm()

    return render(request, 'breakfest/tostu/poldjcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='tostu_poldj')
    return render(request, 'breakfest/tostu/comp.html', context={'comm': comm})

######################


def tostu_sur(request):
    comm = com.objects.filter(name__name='tostu_sur')
    return render(request, 'breakfest/tostu/sur.html', context={'comm': comm})

def tostu_surcom(request):
    item = get_object_or_404(menuu, name='tostu_sur')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sur")
    else:
        form = PostForm()

    return render(request, 'breakfest/tostu/surcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='tostu_sur')
    return render(request, 'breakfest/tostu/comp.html', context={'comm': comm})

##############################


def vafli(request):
    return render(request, 'breakfest/vafli/vafli.html')


def vafli_maldjm(request):
    comm = com.objects.filter(name__name='vafli_maldjm')
    return render(request, 'breakfest/vafli/maldjm.html', context={'comm': comm})

def vafli_maldjmcom(request):
    item = get_object_or_404(menuu, name='vafli_maldjm')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("maldjm")
    else:
        form = PostForm()

    return render(request, 'breakfest/vafli/maldjmcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='vafli_maldjm')
    return render(request, 'breakfest/vafli/comp.html', context={'comm': comm})

#################


def vafli_med(request):
    comm = com.objects.filter(name__name='vafli_med')
    return render(request, 'breakfest/vafli/med.html', context={'comm': comm})

def vafli_medcom(request):
    item = get_object_or_404(menuu, name='vafli_med')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("med")
    else:
        form = PostForm()

    return render(request, 'breakfest/vafli/medcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='vafli_med')
    return render(request, 'breakfest/vafli/comp.html', context={'comm': comm})

#########################


def vafli_poldjm(request):
    comm = com.objects.filter(name__name='vafli_poldjm')
    return render(request, 'breakfest/vafli/poldjm.html', context={'comm': comm})

def vafli_poldjmcom(request):
    item = get_object_or_404(menuu, name='vafli_poldjm')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("poldjm")
    else:
        form = PostForm()

    return render(request, 'breakfest/vafli/poldjmcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='vafli_poldjm')
    return render(request, 'breakfest/vafli/poldj.html', context={'comm': comm})
##########################


def vafli_sirop(request):
    comm = com.objects.filter(name__name='vafli_sirop')
    return render(request, 'breakfest/vafli/sirop.html', context={'comm': comm})

def vafli_siropcom(request):
    item = get_object_or_404(menuu, name='vafli_sirop')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sirop")
    else:
        form = PostForm()

    return render(request, 'breakfest/vafli/siropcom.html', {"form": form, "item": item})

def comp(request):
    comp = com.objects.filter(name__name='vafli_sirop')
    return render(request, 'breakfest/vafli/comp.html', context={'comp': comp})

# ---------------- SALAT ----------------

def salat(request):
    return render(request, 'salat/salat.html')

########################################

def ol(request):
    comm = com.objects.filter(name__name='ol')
    return render(request, 'salat/ol/ol.html', context={"comm": comm})


def olcom(request):
    item = get_object_or_404(menuu, name='ol')
    comm = com.objects.filter(name=item)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect('ol')
    else:
        form = PostForm()

    return render(request, 'salat/ol/olcom.html', {'form': form, 'comm': comm})

    

        

##########################################

def shezar(request):
    comm = com.objects.filter(name__name='shezar')
    return render(request, 'salat/shezar/shezar.html', context={"comm": comm})

def shezarcom(request):
    item = get_object_or_404(menuu, name='shezar')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item 
            new_comment.save()
            return redirect('shezar')
    else:
        form = PostForm()  

    return render(request, 'salat/shezar/shezarcom.html', {'form': form})



##########################################

def grech(request):
    comm = com.objects.filter(name__name='grech')
    return render(request, 'salat/grech/gresh.html', context={"comm": comm})



def grechcom(request):
    item = get_object_or_404(menuu, name='grech')  

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect('gresh')
    else:
        form = PostForm()  

    return render(request, 'salat/grech/greshcom.html', {'form': form})




##########################################


def zavok(request):
    comm = com.objects.filter(name__name='zavok')
    return render(request, 'salat/zavok/zavok.html', context={"comm": comm})

def zavokcom(request):
    item = get_object_or_404(menuu, name='zavok')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment = name = item
            new_comment.save()
            return redirect('zavok')
    else:
        return(request, 'salat/zavok/zavok.html')
    
#####################################

def avokado(request):
    comm = com.objects.filter(name__name='avokado')
    return render(request, 'salat/avokado/avokado.html', context={"comm": comm})

def avokadocom(request):
    item = get_object_or_404(menuu, name='avokado')  

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item  
            new_comment.save()
            return redirect('avokado')
    else:
        form = PostForm()

    return render(request, 'salat/avokado/avokadocom.html', {'form': form})


#############################################


def krevetka(request):
    comm = com.objects.filter(name__name='krevetka')
    return render(request, 'salat/krevetka/krevetka.html',  context={"comm": comm})

def krevetkacom(request):
    item = get_object_or_404(menuu, name='krevetka')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item 
            new_comment.save()
            return redirect('krevetka')
    else:
        form = PostForm()  

    return render(request, 'salat/krevetka/krevetkacom.html', {'form': form})


# ---------------- SUP ----------------

def sup(request):
    return render(request, 'sup/sup.html')


def frik(request):
    return render(request, 'sup/frik/frik.html')


def bul(request):
    return render(request, 'sup/bul/bul.html')


def borch(request):
    return render(request, 'sup/borch/borch.html')

def zelborch(request):
    return render(request, 'sup/zelborch/zelborch.html')


# ---------------- DRINK ----------------

def drink(request):
    return render(request, 'drink/drink.html')


def voda(request):
    return render(request, 'drink/voda/voda.html')


def tea(request):
    return render(request, 'drink/tea/tea.html')

def smyzi(request):
    return render(request, 'drink/smyzi/smyzi.html')


def kok(request):
    return render(request, 'drink/kok/kok.html')








def kava(request):
    return render(request, 'drink/kava/kava.html')

############################################

def espresso(request):
    comm = com.objects.filter(name__name='espresso')
    return render(request, 'drink/kava/espresso.html', context={'comm': comm})

def espressocom(request):
    item = get_object_or_404(menuu, name='espresso')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("espresso")
    else:
        form = PostForm()

    return render(request, 'drink/kava/espressocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.filter(name__name='espresso')
    return render(request, 'drink/kava/espresso.html', context={'comm': comm})

#######################################
def americano(request):
    comm = com.objects.filter(name__name='americano')
    return render(request, 'drink/kava/americano.html', context={'comm': comm})


def americanocom(request):
    item = get_object_or_404(menuu, name='americano')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("americano")
    else:
        form = PostForm()

    return render(request, 'drink/kava/americanocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/americano.html', context={'comm': comm})

######################################
    


def kapuchino(request):
    comm = com.objects.filter(name__name='kapuchino')
    return render(request, 'drink/kava/kapuchino.html', context={'comm': comm})

def kapuchinocom(request):
    item = get_object_or_404(menuu, name='kapuchino')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kapuchino")
    else:
        form = PostForm()

    return render(request, 'drink/kava/kapuchinocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/kapuchino.html', context={'comm': comm})

###############################################

def latte(request):
    comm = com.objects.filter(name__name='latte')
    return render(request, 'drink/kava/latte.html', context={'comm': comm})

def lattecom(request):
    item = get_object_or_404(menuu, name='latte')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("latte")
    else:
        form = PostForm()

    return render(request, 'drink/kava/lattecom.html', {"form": form, "item": item})



def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/latte.html', context={'comm': comm})

###################################

def kakao(request):
    comm = com.objects.filter(name__name='kakao')
    return render(request, 'drink/kava/kakao.html', context={'comm': comm})

def kakaocom(request):
    item = get_object_or_404(menuu, name='kakao')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kakao")
    else:
        form = PostForm()

    return render(request, 'drink/kava/kakaocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kava/kakao.html', context={'comm': comm})

##################################

def mol(request):
    comm = com.objects.filter(name__name='mol')
    return render(request, 'drink/kok/mol.html', context={'comm': comm})

def molcom(request):
    item = get_object_or_404(menuu, name='mol')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("mol")
    else:
        form = PostForm()

    return render(request, 'drink/kok/molcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/mol.html', context={'comm': comm})

##################################

def blla(request):
    comm = com.objects.filter(name__name='blla')
    return render(request, 'drink/kok/blla.html', context={'comm': comm})

def bllacom(request):
    item = get_object_or_404(menuu, name='blla')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("blla")
    else:
        form = PostForm()

    return render(request, 'drink/kok/bllacom.html', {"form": form, "item": item})


def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/blla.html', context={'comm': comm})

############################

def mohito(request):
    comm = com.objects.filter(name__name='mohito')
    return render(request, 'drink/kok/mohito.html', context={'comm': comm})

def mohitocom(request):
    item = get_object_or_404(menuu, name='mohito')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("mohito")
    else:
        form = PostForm()

    return render(request, 'drink/kok/mohitocom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/kok/mohito.html', context={'comm': comm})

############################


def cherry(request):
    comm = com.objects.filter(name__name='cherry')
    return render(request, 'drink/smyzi/cherry.html', context={'comm': comm})

def cherrycom(request):
    item = get_object_or_404(menuu, name='cherry')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("cherry")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/cherrycom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/cherry.html', context={'comm': comm})

##############################

def polynisa(request):
    comm = com.objects.filter(name__name='polynisa')
    return render(request, 'drink/smyzi/polynisa.html', context={'comm': comm})

def polynisacom(request):
    item = get_object_or_404(menuu, name='polynisa')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("polynisa")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/polynisacom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/polynisa.html', context={'comm': comm})

#####################

def banan(request):
    comm = com.objects.filter(name__name='banan')
    return render(request, 'drink/smyzi/banan.html', context={'comm': comm})

def banancom(request):
    item = get_object_or_404(menuu, name='banan')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("banan")
    else:
        form = PostForm()

    return render(request, 'drink/smyzi/banancom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/smyzi/banan.html', context={'comm': comm})

#############################################

def green(request):
    comm = com.objects.filter(name__name='green')
    return render(request, 'drink/tea/green.html', context={'comm': comm})

def greencom(request):
    item = get_object_or_404(menuu, name='green')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("green")
    else:
        form = PostForm()

    return render(request, 'drink/tea/greencom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/green.html', context={'comm': comm})

#########################

def black(request):
    comm = com.objects.filter(name__name='black')
    return render(request, 'drink/tea/black.html', context={'comm': comm})

def blackcom(request):
    item = get_object_or_404(menuu, name='black')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("black")
    else:
        form = PostForm()

    return render(request, 'drink/tea/blackcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/black.html', context={'comm': comm})

###############################

def night(request):
    comm = com.objects.filter(name__name='night')
    return render(request, 'drink/tea/night.html', context={'comm': comm})

def nightcom(request):
    item = get_object_or_404(menuu, name='night')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("night")
    else:
        form = PostForm()

    return render(request, 'drink/tea/nightcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/tea/night.html', context={'comm': comm})

##########################

def sik(request):
    comm = com.objects.filter(name__name='sik')
    return render(request, 'drink/voda/sik.html', context={'comm': comm})

def sikcom(request):
    item = get_object_or_404(menuu, name='sik')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sik")
    else:
        form = PostForm()

    return render(request, 'drink/voda/sikcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/sik.html', context={'comm': comm})   

##########################

def sprite(request):
    comm = com.objects.filter(name__name='sprite')
    return render(request, 'drink/voda/sprite.html', context={'comm': comm})    

def spritecom(request):
    item = get_object_or_404(menuu, name='sprite')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("sprite")
    else:
        form = PostForm()

    return render(request, 'drink/voda/spritecom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/sprite.html', context={'comm': comm})
##################################

def kola(request):
    comm = com.objects.filter(name__name='kola')
    return render(request, 'drink/voda/kola.html', context={'comm': comm})

def kolacom(request):
    item = get_object_or_404(menuu, name='kola')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("kola")
    else:
        form = PostForm()

    return render(request, 'drink/voda/kolacom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/kola.html', context={'comm': comm})
#################################


def yzvar(request):
    comm = com.objects.filter(name__name='yzvar')
    return render(request, 'drink/voda/yzvar.html', context={'comm': comm})

def yzvarcom(request):
    item = get_object_or_404(menuu, name='yzvar')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("yzvar")
    else:
        form = PostForm()

    return render(request, 'drink/voda/yzvarcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'drink/voda/yzvar.html', context={'comm': comm})

##########################


# ---------------- DESERT ----------------

def desert(request):
    return render(request, 'desert/desert.html')

###############################
def moroz(request):
    comm = com.objects.filter(name__name='moroz')
    return render(request, 'desert/moroz/moroz.html', context={'comm': comm})

def morozcom(request):
    item = get_object_or_404(menuu, name='moroz')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("moroz")
    else:
        form = PostForm()

    return render(request, 'desert/moroz/morozcom.html', {"form": form, "item": item})


def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/moroz/moroz.html', context={'comm': comm})

#################################


def nap(request):
    comm = com.objects.filter(name__name='nap')
    return render(request, 'desert/nap/nap.html', context={'comm': comm})

def napcom(request):
    item = get_object_or_404(menuu, name='nap')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("nap")
    else:
        form = PostForm()

    return render(request, 'desert/nap/napcom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/nap/nap.html', context={'comm': comm})

##################################

def tir(request):
    comm = com.objects.filter(name__name='tir')
    return render(request, 'desert/tir/tir.html', context={'comm': comm})

def tircom(request):
    item = get_object_or_404(menuu, name='tir')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = item
            new_comment.save()
            return redirect("tir")
    else:
        form = PostForm()

    return render(request, 'desert/tir/tircom.html', {"form": form, "item": item})

def comp(request):
    comm = com.objects.all()
    return render(request, 'desert/tir/tir.html', context={'comm': comm})

# ---------------- AUTH ----------------

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, 'Невірний логін або пароль')
        return self.form_invalid(form)


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

