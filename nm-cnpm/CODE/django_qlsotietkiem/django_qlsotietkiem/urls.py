from django.conf.urls import patterns, include, url

from django.contrib import admin
from qlsotietkiem import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_qlsotietkiem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/qlsotietkiem/baocao/DongMoSoThang', views.render_dong_mo_so_thang, name='render_dong_mo_so_thang'),
    url(r'^admin/qlsotietkiem/baocao/DoanhThuNgay', views.render_doanh_thu_ngay, name='render_doanh_thu_ngay'),
    )
