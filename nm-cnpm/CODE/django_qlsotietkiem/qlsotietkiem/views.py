from django.shortcuts import render

# Create your views here.

def render_dong_mo_so_thang(request):
    return render(request, 'admin/DongMoSoThang.html')

def render_doanh_thu_ngay(request):
    return render(request, 'admin/DoanhThuNgay.html')