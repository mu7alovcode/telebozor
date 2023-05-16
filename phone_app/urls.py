from django.urls import path

from .models import Contact
from .views import phone_list, phone_detail, ContactPageView, HomePageView, SamsungPhoneView, ApplePhoneView, \
    XiaomiPhoneView, HuaweiPhoneView, LenovoPhoneView, ArtelPhoneView, SonyPhoneView, LGPhoneView, VivoPhoneView, \
    NokiaPhoneView, OppoPhoneView, BoshqalarPhoneView,PhoneCreateView,PhoneUpdateView,PhoneDeleteView,SearchResultsList,phoneAllList

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('phone/', phone_list, name='all_phone_list'),
    path('phone/<int:id>/', phone_detail, name='detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('phone/create/', PhoneCreateView.as_view(), name='phone_create'),
    path('phone/<int:id>/update/', PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/<int:id>/delete/', PhoneDeleteView.as_view(), name='phone_delete'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
    path('all-phone/', phoneAllList, name='all_phone'),

    # Category list
    path('samsung-phone/', SamsungPhoneView.as_view(), name='samsung_page'),
    path('apple-phone/', ApplePhoneView.as_view(), name='apple_page'),
    path('xiaomi-phone/', XiaomiPhoneView.as_view(), name='xiaomi_page'),
    path('huawei-phone/', HuaweiPhoneView.as_view(), name='huawei_page'),
    path('lenovo-phone/', LenovoPhoneView.as_view(), name='lenovo_page'),
    path('artel-phone/', ArtelPhoneView.as_view(), name='artel_page'),
    path('sony-phone/', SonyPhoneView.as_view(), name='sony_page'),
    path('lg-phone/', LGPhoneView.as_view(), name='lg_page'),
    path('vivo-phone/', VivoPhoneView.as_view(), name='vivo_page'),
    path('nokia-phone/', NokiaPhoneView.as_view(), name='nokia_page'),
    path('oppo-phone/', OppoPhoneView.as_view(), name='oppo_page'),
    path('boshqalar-phone/', BoshqalarPhoneView.as_view(), name='boshqalar_page'),
]
