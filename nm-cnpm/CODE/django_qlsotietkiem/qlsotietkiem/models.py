# -*- coding: utf-8 -*-
from django.db import models


class KhachHang(models.Model):
    ten = models.CharField(max_length=50, verbose_name=u'Tên KH')
    dia_chi = models.CharField(max_length=150, verbose_name=u'Địa chỉ')
    cmnd = models.CharField(max_length=10, verbose_name='CMND')

    def __unicode__(self):
        return u'%s - %s'%(self.ten, self.cmnd)

    class Meta:
        verbose_name = u'Khách hàng'
        verbose_name_plural = u'Khách hàng'


class LoaiTietKiem(models.Model):
    ky_han = models.CharField(max_length=100, verbose_name=u'Kỳ hạn')
    lai_suat = models.FloatField(verbose_name=u'Lãi suất')
    tg_gui_toi_thieu = models.IntegerField(verbose_name=u'TG gửi tối thiểu (ngày)', default=0)
    tien_gui_toi_thieu = models.FloatField(verbose_name=u'Tiền gửi tối thiểu', default=100000)

    def __unicode__(self):
        return u'%s - %s%%'%(self.ky_han, self.lai_suat)

    class Meta:
        verbose_name = u'Loại tiết kiệm'
        verbose_name_plural = u'Loại tiết kiệm'


class SoTietKiem(models.Model):
    TINH_TRANG_CHOICES = (
        ('DONG', u'Đóng'),
        ('MO', u'Mở'),
    )
    khach_hang = models.ForeignKey(KhachHang, verbose_name=u'Khách hàng')
    loai_tiet_kiem = models.ForeignKey(LoaiTietKiem, verbose_name=u'Loại tiết kiệm')
    ngay_mo = models.DateTimeField(verbose_name=u'Ngày mở sổ', auto_now_add=True)
    tien_gui = models.FloatField(verbose_name=u'Số dư', default=100000)
    tinh_trang = models.CharField(max_length=5, choices=TINH_TRANG_CHOICES, default='MO', verbose_name=u'Tình trạng sổ')

    def __unicode__(self):
        return u'STK %s - %s - %s - Số dư: %s'%(self.pk, self.khach_hang, self.loai_tiet_kiem, self.tien_gui)

    class Meta:
        verbose_name = u'Sổ tiết kiệm'
        verbose_name_plural = u'Sổ tiết kiệm'


class Phieu(models.Model):
    LOAI_PHIEU_CHOICES = (
        ('RUT', u'Phiếu rút tiền'),
        ('GUI', u'Phiếu gửi tiền'),
    )
    so_tiet_kiem = models.ForeignKey(SoTietKiem, verbose_name=u'Sổ tiết kiệm')
    khach_hang = models.ForeignKey(KhachHang, verbose_name=u'Khách hàng')
    loai_phieu = models.CharField(verbose_name=u'Loại phiếu', max_length=3, choices=LOAI_PHIEU_CHOICES)
    ngay_lap_phieu = models.DateTimeField(verbose_name=u'Ngày lập phiếu', auto_now_add=True)
    so_tien = models.FloatField(verbose_name=u'Số tiền', default=0)

    def __unicode__(self):
        return u'Phiếu %s'%(self.loai_phieu)

    class Meta:
        verbose_name = u'Phiếu gửi tiền - rút tiền'
        verbose_name_plural = u'Phiếu gửi tiền - rút tiền'

