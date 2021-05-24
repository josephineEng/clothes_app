from django.shortcuts import render
from django.http import HttpResponse
from .forms import select_cloth, male_selection, select_clotha, male_selectionn
# Create your views here.

def my_view(request): 
    return render(request, "home.html")
    #return HttpResponse(""" """)
    
def female(request): 
    sz = None
    if request.method=="POST":
        form = select_cloth(request.POST)
        if form.is_valid():
            dress=form.cleaned_data['DRESS']
        
            if dress=="1":
                chest = form.cleaned_data['CHEST']
                if chest == '1':
                    sz = 'DRESS:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif chest =='2':
                    sz='DRESS:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif chest =='3':
                    sz='DRESS:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='DRESS:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'

            elif dress=="2":
                waist = form.cleaned_data['WAIST']
                if waist == '1':
                    sz = 'SKIRT:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif waist=='2':
                    sz='SKIRT:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif waist=='3':
                    sz='SKIRT:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='SKIRT:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'                

            elif dress=="3":
                hips = form.cleaned_data['HIPS']
                if hips == '1':
                    sz = 'PANTS:SKIRT:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif hips=='2':
                    sz='PANTS:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif hips=='3':
                    sz='PANTS:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='PANTS:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'                        

            else:
                print('haha')
       
    else:
        form = select_cloth(request.POST)
    return render(request, "female.html",{'form':form, 'sz':sz})

def male(request):
    sz = None
    if request.method=="POST":
        form =male_selection(request.POST)
        if form.is_valid():
            dress=form.cleaned_data['SHIRT_SHORT']
            print(dress)
            if dress=="1":
                chest = form.cleaned_data['CHEST_M']
                if chest == '1':
                    sz = 'shirt_short:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif chest =='2':
                    sz='shirt_short:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif chest =='3':
                    sz='shirt_short:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='shirt_short:GENERAL:XL UK-SIZE:38  US-SIZE:36'

            elif dress=="2":
                waist = form.cleaned_data['WAIST_M']
                if waist == '1':
                    sz = 'Shirt_long:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif waist=='2':
                    sz='shirt_long:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif waist=='3':
                    sz='shirt_log:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='shirt_long:GENERAL:XL UK-SIZE:38  US-SIZE:36'                

            elif dress=="3":
                hips = form.cleaned_data['HIPS_M']
                if hips == '1':
                    sz = 'PANTS:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif hips=='2':
                    sz='PANTS:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif hips=='3':
                    sz='PANTS:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='PANTS:GENERAL:XL UK-SIZE:38  US-SIZE:36'                        

            else:
                print('haha')
       
    else:
        form = male_selection(request.POST)
    return render(request,"male.html",{'form':form, 'sz':sz})

def select(request):
    pass    


    
def femaleb(request): 
    sz = None
    if request.method=="POST":
        form = select_clotha(request.POST)
        if form.is_valid():
            dress=form.cleaned_data['DRESS']
            if dress=="1":
                chest = form.cleaned_data['CHEST']
                if chest == '1':
                    sz = 'DRESS:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif chest =='2':
                    sz='DRESS:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif chest =='3':
                    sz='DRESS:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='DRESS:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'

            elif dress=="2":
                waist = form.cleaned_data['WAIST']
                if waist == '1':
                    sz = 'SKIRT:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif waist=='2':
                    sz='SKIRT:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif waist=='3':
                    sz='SKIRT:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='SKIRT:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'                

            elif dress=="3":
                hips = form.cleaned_data['HIPS']
                if hips == '1':
                    sz = 'PANTS:SKIRT:GENERAL-SIZE:XS  UK-SIZE:4  US-SIZE:2'
                elif hips=='2':
                    sz='PANTS:GENERAL-SIZE:S UK-SIZE:6   US-SIZE:4'
                elif hips=='3':
                    sz='PANTS:GENERAL-SIZE:M UK-SIZE:8   US-SIZE:6'
                else:
                    sz='PANTS:GENERAL-SIZE:L  UK-SIZE:10  US-SIZE:8'                            

            else:
                print('haha')
       
    else:
        form = select_clotha(request.POST)
    return render(request,"femaleb.html",{'form':form, 'sz':sz})

    
def maleb(request):
    sz = None
    if request.method=="POST":
        form =male_selectionn(request.POST)
        if form.is_valid():
            dress=form.cleaned_data['SHIRT_SHORT']
            
            if dress=="1":
                
                chest = form.cleaned_data['CHEST_M']
                if chest == '1':
                    sz = 'shirt_short:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif chest =='2':
                    sz='shirt_short:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif chest =='3':
                    sz='shirt_short:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='shirt_short:GENERAL:XL UK-SIZE:38  US-SIZE:36'

            elif dress=="2":
                waist = form.cleaned_data['WAIST_M']
                if waist == '1':
                    sz = 'Shirt_long:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif waist=='2':
                    sz='shirt_long:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif waist=='3':
                    sz='shirt_log:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='shirt_long:GENERAL:XL UK-SIZE:38  US-SIZE:36'                

            elif dress=="3":
                hips = form.cleaned_data['HIPS_M']
                if hips == '1':
                    sz = 'PANTS:GENERAL:S UK-SIZE:30   US-SIZE:28'
                elif hips=='2':
                    sz='PANTS:GENERAL:M UK-SIZE:32   US-SIZE:30'
                elif hips=='3':
                    sz='PANTS:GENERAL:L UK-SIZE:34   US-SIZE:32'
                else:
                    sz='PANTS:GENERAL:XL UK-SIZE:38  US-SIZE:36'                        
            else:
                print('haha')
       
    else:
        form = male_selectionn(request.POST)
    return render(request,"maleb.html",{'form':form, 'sz':sz})