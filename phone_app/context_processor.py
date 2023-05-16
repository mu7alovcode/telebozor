from .models import Phone, Category


def latest_phone(request):
    latest_phone = Phone.published.all().order_by('-publish_time')
    categories = Category.objects.all()

    context = {
        'latest_phone': latest_phone,
        'categories': categories,
    }
    return context