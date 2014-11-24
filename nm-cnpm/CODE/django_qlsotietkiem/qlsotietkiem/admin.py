# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import render
from models import *
# Register your models here.



class SoTietKiemAdmin(admin.ModelAdmin):
    list_display = ['ma_stk', 'loai_tiet_kiem', 'khach_hang', 'tien_gui']
    fields = ['loai_tiet_kiem', 'khach_hang', 'tien_gui']
    readonly_fields = ['ma_stk']

    def ma_stk(self, obj):
        return obj.pk

    ma_stk.short_description = u'Mã STK'


class SoTietKiemInline(admin.TabularInline):
    model = SoTietKiem
    extra = 1


class KhachHangAdmin(admin.ModelAdmin):
    list_display = ['ten', 'dia_chi', 'cmnd']
    inlines = [SoTietKiemInline]

class LoaiTietKiemAdmin(admin.ModelAdmin):
    list_display = ['ky_han', 'lai_suat', 'tg_gui_toi_thieu', 'tien_gui_toi_thieu']

admin.site.register(KhachHang, KhachHangAdmin)
admin.site.register(LoaiTietKiem, LoaiTietKiemAdmin)
admin.site.register(Phieu)
admin.site.register(SoTietKiem, SoTietKiemAdmin)