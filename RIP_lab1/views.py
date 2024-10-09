from django.shortcuts import render
products = [{'title': 'Gateway cosmonaut figure', 'price': 3000, 'id': 1,
             'info':'• Масштаб 1:6\n'
                    ' • 13,5 дюйма в высоту с основанием\n'
                    ' • 1400 грамм'
             },
        {'title': 'Gateway mission patch', 'price': 400,'id': 2,'info':''},
        {'title': 'Gateway mission T-shirt','price': 1500, 'id': 3,
         'info' : 'Размеры - S-XXL\n'
                  'Состав - Хлопок 60% / Полиэстр 40%'},]
orders = []
selected_products = []
for product in products:
    selected_products.append(product)
orders.append({'id': 1, 'products': selected_products,'quantity': len(selected_products)})

def main_page_render(request):
    order = next((item for item in orders if item['id'] == 1), None)
    search_query = request.GET.get('searchInput', '')
    filtered_products = [
        product for product in products
        if search_query in product['title']
    ]
    return render(request, 'products.html', {'data' : {'products' : filtered_products, 'order' : order, 'search':search_query}})
def product_page_render(request,id):
    product = next((item for item in products if item['id'] == id), None)
    return render(request, 'product.html',{'product': product})
def cart_page_render(request, id):
    order = next((item for item in orders if item['id'] == id), None)
    return render(request, 'cart.html', {'order': order})

