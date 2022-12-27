from django.shortcuts import render
from stores.models import Product, ReviewRating
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    title = 'Hello World'
    product = Product.objects.all().filter(is_available=True).order_by('created_date')
    paginator = Paginator(product, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    for products in product:
        reviews = ReviewRating.objects.filter(product_id=products.id, status=True)

    context = {
        'title': title,
        'product': paged_products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)


def footer(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'includes/footer.html', context)
