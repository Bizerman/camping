
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from camping_back.camping_bd.models import CarCamping, OrderCarCamping, Order
from django.contrib.auth.models import User

def car_campings_page_render(request):
    order = get_draft_order()
    car_quantity = len(order.get_cars()) if order else 0
    search_query = request.GET.get('car_camping', '').strip().lower()
    cars = CarCamping.objects.prefetch_related('images').all()
    if search_query:
        cars = cars.filter(title__icontains=search_query)
    return render(request, 'car_campings.html', {
        'data': {
            'car_camping': cars,
            'order': order,
            'quantity': car_quantity,
            'search': search_query
        }
    })
def car_camping_page_render(request, id):
    car = get_object_or_404(
        CarCamping.objects.prefetch_related('images'),
        id=id
    )
    return render(request, 'car_camping.html', {'product': car})
def order_page_render(request, id):
    if not Order.objects.filter(pk=id).exists():
        return render(request,"404.html")
    order = Order.objects.get(id=id)
    if order.status == 5:
        return render(request, "404.html")

    return render(request, 'order.html', {'order': order})
def add_to_order(request,car_id):
    car_name = request.POST.get("title")
    redirect_url = f"/?car_name={car_name}" if car_name else "/"
    car_camping = CarCamping.objects.get(pk=car_id)
    draft_order = get_draft_order()
    if draft_order is None:
        draft_order = Order.objects.create()
        draft_order.creator = get_current_user()
        draft_order.create_datetime = timezone.now()
        draft_order.save()
    if OrderCarCamping.objects.filter(order=draft_order,car=car_camping).exists():
        return redirect(redirect_url)
    item = OrderCarCamping(
        order=draft_order,
        car=car_camping
    )
    item.save()
    return redirect(redirect_url)
def del_order(request,id):
    if not Order.objects.filter(pk=id).exists():
        return redirect("/")
    with connection.cursor() as cursor:
        cursor.execute("UPDATE orders SET status=5 WHERE id=%s",[id])
    return redirect("/")
def get_draft_order():
    return  Order.objects.filter(status=1).first()
def get_current_user():
    return User.objects.filter().first()