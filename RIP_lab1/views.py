from django.shortcuts import render
def main_page_render(request):
    return render(request, 'products.html')
def product_page_render(request):
    return render(request, 'product.html', {'data' : {'products' : [
        {'title': 'Gateway cosmonaut figure', 'id': 1},
        {'title': 'Gateway mission patch', 'id': 2},
        {'title': 'Gateway mission T-shirt', 'id': 3},
    ]}})