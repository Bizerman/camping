from django.shortcuts import render, redirect
from django.utils import timezone

from bmstu.gateway.models import Gateway_el, Gateway_el_mission
from bmstu.gateway.models import Gateway_mission
from django.contrib.auth.models import User
def gateway_products_page_render(request):
    #gateway_mission = Gateway_mission.objects.get(mission_id=1)
    if (request.GET.get('gateway_el') != None): search_gateway_el = str(request.GET.get('gateway_el'))
    else: search_gateway_el = ''
    filtered_gateway_el = [
        product for product in Gateway_el.objects.all()
        if search_gateway_el.lower() in product.title.lower()
        ]
    return render(request, 'gateway_products.html', {'data' : {'gateway_el' : filtered_gateway_el, 'mission' : None, 'search':search_gateway_el}})
def gateway_product_page_render(request,id):
    element = next((item for item in Gateway_el.objects.all() if item.gateway_el_id == id), None)
    return render(request, 'gateway_product.html',{'product': element})
def mission_page_render(request, id):
    order = next((item for item in Gateway_mission.objects.all() if item['mission_id'] == id), None)
    return render(request, 'mission.html', {'order': order})
def add_to_mission(request,el_id):
    el_name = request.POST.get("title")
    redirect_url = f"/?el_name={el_name}" if el_name else "/"
    gateway_el = Gateway_el.objects.get(pk=el_id)
    draft_mission = get_draft_mission()
    if draft_mission is None:
        draft_mission = Gateway_mission.objects.create()
        draft_mission.creator = get_current_user()
        draft_mission.create_date = timezone.now()
        draft_mission.save()
    if Gateway_el_mission.objects.filter(mission=draft_mission,el=gateway_el).exists():
        return redirect(redirect_url)
    item = Gateway_el_mission(
        mission=draft_mission,
        el=gateway_el
    )
    item.save()
    return redirect(redirect_url)
def get_draft_mission():
    return  Gateway_mission.objects.filter(status=1).first()
def get_current_user():
    return User.objects.filter(is_superuser=False).first()