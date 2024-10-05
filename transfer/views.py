from django.shortcuts import render, get_object_or_404, redirect
from .models import Transfer
# Create your views here.

def processorder(request):
    if request.method == "POST":
        start_calendar = request.POST['startcalendar']
        end_calendar = request.POST['endcalendar']
        user_id = request.POST.get('user_id','')
        warehouse_id = request.POST.get('idnum','')
        rent_price = request.POST['rentval']
        note_val = request.POST['note']
        transferitem = Transfer(warehouse=warehouse_id, note = note_val,user = user_id, rent_paid=rent_price,rent_date=start_calendar, end_date=end_calendar)
        transferitem.save()
        return redirect("index")
    else:
        return render(request,'pages/exception/error_404.html') 
        