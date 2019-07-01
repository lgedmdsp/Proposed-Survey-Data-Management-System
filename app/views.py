from django.shortcuts import render,redirect
from .models import data,district,upazilla
from .forms import BaseForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage
)
from django.db.models import Avg
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from django.views import View

from .forms import PhotoForm
from .models import Photo

def edit_data(request, data_id):
    dt = data.objects.get(id=data_id)
    if request.POST:
        form = BaseForm(request.POST, instance=dt)
        if form.is_valid():
            if form.save():
                return redirect('/mdsp/showdata', messages.success(request, 'Data was successfully updated.', 'alert-success'))
            else:
                return redirect('/mdsp/showdata', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/mdsp/showdata', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        base_form = BaseForm(instance=dt) 
        
       
        return render(request, 'app/edit.html', {'base_form':base_form})


# Show data in short form
@login_required
def show_data(request):
    queryset_list = data.objects.all().order_by('id')
    

    # Searching
    query_dis = request.GET.get('qd', None)
    query_upz = request.GET.get('qup', None)
    query_uni = request.GET.get('qun', None)
    query_moz = request.GET.get('qm', None)
    query_vil = request.GET.get('qv', None)
    

    if query_dis and query_upz and query_uni and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  &
            Q(mouza__icontains=query_moz)   &
            Q(village__icontains=query_vil)

        )   
    
    elif query_dis and query_upz and query_uni and query_moz:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  &
            Q(mouza__icontains=query_moz)   
        ) 
    
    elif query_dis and query_upz and query_uni and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  &
            Q(village__icontains=query_vil)   
        )

    elif query_dis and query_uni and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(s_union__icontains=query_uni) &
            Q(mouza__icontains=query_moz)  &
            Q(village__icontains=query_vil)   
        )

    elif query_upz and query_uni and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni) &
            Q(mouza__icontains=query_moz)  &
            Q(village__icontains=query_vil)   
        )    
    
    
    elif query_dis and query_uni and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(s_union__icontains=query_uni) &
            Q(mouza__icontains=query_moz)  &
            Q(village__icontains=query_vil)   
        )
    
    elif query_uni and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(s_union__icontains=query_uni) &
            Q(mouza__icontains=query_moz)  &
            Q(village__icontains=query_vil)   
        )
    
    elif query_upz and query_uni and query_vil:

        queryset_list = queryset_list.filter(      
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  &
            Q(village__icontains=query_vil)   
        )
    
    elif query_upz and query_uni and query_moz:

        queryset_list = queryset_list.filter(      
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  &
            Q(mouza__icontains=query_moz)   
        )
    
    elif query_dis and query_moz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(mouza__icontains=query_moz)  &
            Q(village__icontains=query_vil)   
        )
    
    elif query_dis and query_uni and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(s_union__icontains=query_uni)  &
            Q(village__icontains=query_vil)   
        )
    
    elif query_dis and query_uni and query_moz:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(s_union__icontains=query_uni)  &
            Q(mouza__icontains=query_moz)   
        ) 
    
    elif query_dis and query_upz and  query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(village__icontains=query_vil)   
        ) 
    
    elif query_dis and query_upz and  query_moz:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(mouza__icontains=query_moz)   
        ) 
    
    elif query_dis and query_upz and query_uni:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  
               
        ) 
    
    elif query_moz and query_vil:

        queryset_list = queryset_list.filter(     
            Q(mouza__exact=query_moz)  &
            Q(village__exact=query_vil)   
       
        ) 
    
    elif query_uni and query_vil:

        queryset_list = queryset_list.filter(     
            Q(s_union__icontains=query_uni)  &
            Q(village__icontains=query_vil)   
       
        ) 
    
    
    elif query_uni and query_moz:

        queryset_list = queryset_list.filter(     
            Q(s_union__icontains=query_uni)  &
            Q(mouza__icontains=query_moz)   
       
        ) 

    elif query_upz and query_vil:

        queryset_list = queryset_list.filter(      
            Q(upazilla__icontains=query_upz) &
            Q(village__icontains=query_vil)  
       
        ) 

    elif query_upz and query_moz:

        queryset_list = queryset_list.filter(      
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  
       
        ) 

    
    elif  query_upz and query_uni:

        queryset_list = queryset_list.filter(      
            
            Q(upazilla__icontains=query_upz) &
            Q(s_union__icontains=query_uni)  
              
        ) 
    
    elif query_dis and query_vil:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(village__icontains=query_vil)   
        ) 
    
    elif query_dis and query_moz:

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(mouza__icontains=query_moz)   
        ) 

    elif query_dis and query_uni :

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(s_union__icontains=query_uni)  
             
        ) 
    
    elif query_dis and query_upz :

        queryset_list = queryset_list.filter(      
            Q(district__icontains=query_dis) &
            Q(upazilla__icontains=query_upz) 
               
        )

    elif query_vil:
        queryset_list = queryset_list.filter(
            Q(village__exact = query_vil)
        ) 
    
    elif  query_moz:

        queryset_list = queryset_list.filter(    
            Q(mouza__exact=query_moz)   
        ) 
    
    elif query_uni:
        queryset_list = queryset_list.filter(
            Q(s_union__exact=query_uni)
        )

    elif query_upz:
        queryset_list = queryset_list.filter(
            Q(upazilla__exact=query_upz)
        )
    
    elif query_dis:
        queryset_list = queryset_list.filter(
            Q(district__exact=query_dis)
        ) 
    
     
    
    queryset_count = queryset_list.count()
    population = list(queryset_list.aggregate(Sum('expectedpopulation')).values())[0]
    waterlevel = list(queryset_list.aggregate(Avg('waterlevel')).values())[0]
    pucca = list(queryset_list.aggregate(Sum('pucca')).values())[0]
    semipucca = list(queryset_list.aggregate(Sum('semipucca')).values())[0]
    wooden = list(queryset_list.aggregate(Sum('wooden')).values())[0]
    bamboo = list(queryset_list.aggregate(Sum('bamboo')).values())[0]
    thatched = list(queryset_list.aggregate(Sum('thatched')).values())[0]
    shanty = list(queryset_list.aggregate(Sum('shanty')).values())[0]

    dist = district.objects.all() #dropdown


    # Paginator shows 100 contacts per page
    paginator = Paginator(queryset_list, 25)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    

    template = 'app/showdata.html'
    context = {
        'Sdata': queryset,
        'page': page, 
        'qd_value' : query_dis,
        'qup_value' : query_upz,
        'qun_value' : query_uni,
        'qm_value' : query_moz,
        'qv_value' : query_vil,
        'cnt' : queryset_count,
        'population' : population,
        'waterlevel' : waterlevel,
        'pucca' : pucca,
        'semipucca' : semipucca,
        'wooden': wooden,
        'bamboo' : bamboo,
        'thatched' : thatched,
        'shanty' : shanty,
        'districts': dist,
        
    }

    return render(request, template, context)


def gallery_display(self, request):
    photos_list = Photo.objects.all()
    return render(self.request, 'gallery/index.html', {'li_photo': photos_list})

def upload(request, data_id):
    form = PhotoForm(request.POST, request.FILES)
    
    if form.is_valid():        
        photo = form.save()
    else:
        form = PhotoForm()
    return render(request, 'gallery/index.html', {'form': form}) 

     




    