from django.shortcuts import redirect, render
from .forms import TrainerRegistrationForm
from django.shortcuts import render
from .models import Trainer


def register_trainer(request):
    if request.method=="POST":
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_trainer')
        else:
            print(form.errors)
    else:
        form= TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})

def trainer_list(request):
    trainers= Trainer.objects.all()
    return render(request,"trainer_list.html", {"trainers": trainers})

def trainer_profile(request,id):
    trainer= Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})


def edit_trainer(request, id):
    trainer= Trainer.objects.get(id=id)
    if request.method == "POST":
        form=TrainerRegistrationForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
        return redirect("trainer_profile", id=trainer.id)
    else:
        form= TrainerRegistrationForm(instance=trainer)
        return render(request,"edit_trainer.html", {"form":form})

# Create your views here.
