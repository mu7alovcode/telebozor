from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from .models import Phone, Category
from .forms import ContactForm
from phone_project.custom_permissions import OnlyLoggedSuperUser


def phone_list(request):
    phone_list = Phone.published.all()
    context = {
        "phone_list": phone_list
    }
    return render(request, 'phone/phone_list.html', context)




def phone_detail(request, id):
    phone = get_object_or_404(Phone, id=id, status=Phone.Status.Published)
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(phone)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['hit_counted'] = hits


    context = {
        "phone": phone
    }
    return render(request, 'phone/detail.html', context)


class HomePageView(ListView):
    model = Phone
    template_name = 'phone/home.html'
    context_object_name = 'phone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['phone_list'] = Phone.published.all().order_by('-publish_time')[:16]
        context['apple_list'] = Phone.objects.all().filter(category__name='Apple')
        return context


class ContactPageView(TemplateView):
    template_name = 'phone/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'phone/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakur!")
        context = {
            'form': form
        }
        return render(request, 'phone/contact.html', context)


def phoneAllList(request):
    phone_list = Phone.published.all()
    context = {
        "phone_list": phone_list
    }
    return render(request, 'phone/phone_all.html', context)



class SamsungPhoneView(ListView):
    model = Phone
    template_name = 'category/samsung.html'
    context_object_name = 'samsung'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Samsung')
        return phone


class ApplePhoneView(ListView):
    model = Phone
    template_name = 'category/apple.html'
    context_object_name = 'apple'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Apple')
        return phone


class XiaomiPhoneView(ListView):
    model = Phone
    template_name = 'category/xiaomi.html'
    context_object_name = 'xiaomi_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Xiaomi')
        return phone


class HuaweiPhoneView(ListView):
    model = Phone
    template_name = 'category/huawei.html'
    context_object_name = 'huawei_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Huawei')
        return phone


class LenovoPhoneView(ListView):
    model = Phone
    template_name = 'category/lenovo.html'
    context_object_name = 'lenovo_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Lenovo')
        return phone


class ArtelPhoneView(ListView):
    model = Phone
    template_name = 'category/artel.html'
    context_object_name = 'artel_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Artel')
        return phone


class SonyPhoneView(ListView):
    model = Phone
    template_name = 'category/sony.html'
    context_object_name = 'sony_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Sony')
        return phone


class LGPhoneView(ListView):
    model = Phone
    template_name = 'category/lg.html'
    context_object_name = 'lg_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='LG')
        return phone


class VivoPhoneView(ListView):
    model = Phone
    template_name = 'category/vivo.html'
    context_object_name = 'vivo_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Vivo')
        return phone


class NokiaPhoneView(ListView):
    model = Phone
    template_name = 'category/nokia.html'
    context_object_name = 'nokia_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Nokia')
        return phone


class OppoPhoneView(ListView):
    model = Phone
    template_name = 'category/oppo.html'
    context_object_name = 'oppo_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Oppo')
        return phone


class BoshqalarPhoneView(ListView):
    model = Phone
    template_name = 'category/boshqalar.html'
    context_object_name = 'boshqalar_phone'

    def get_queryset(self):
        phone = self.model.published.all().filter(category__name='Boshqalar')
        return phone


class PhoneUpdateView(OnlyLoggedSuperUser, ListView):
    model = Phone
    fields = ('title', 'body', 'image1', 'image2', 'image3', 'image4', 'category', 'status', 'price', 'phonenumber')
    template_name = 'crud/phone_edit.html'


class PhoneDeleteView(OnlyLoggedSuperUser, ListView):
    model = Phone
    template_name = 'crud/phone_delete.html'
    success_url = reverse_lazy('home_page')


class PhoneCreateView(LoginRequiredMixin, CreateView):
    model = Phone
    success_url = reverse_lazy('home_page')
    template_name = 'crud/phone_create.html'
    fields = (
        'title', 'slug', 'body', 'image1', 'image2', 'image3', 'price', 'phonenumber', 'category')


class SearchResultsList(ListView):
    model = Phone
    template_name = 'phone/search_result.html'
    context_object_name = "phone_list"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Phone.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query))

