def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)