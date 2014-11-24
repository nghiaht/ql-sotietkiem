# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu


class UserTopMenu(Menu):

    def my_user_check(self, user):
        """
        Custom helper method for hiding some menu items from not allowed users.
        """
        return user.groups.filter(name='users').exists()

    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)

        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            from django.contrib.sites.models import Site
            site_name = Site.objects.get_current().name
            site_url = 'http://' + Site.objects.get_current().domain
        else:
            site_name = ('Quỹ Tiết Kiệm')
            site_url = '/admin/'

        self.children += [
            items.MenuItem(
                title=site_name,
                url=site_url,
                icon='fa-bank',
                css_styles='font-size: 1.5em;',
            ),
            items.MenuItem(
                title=('Sổ tiết kiệm'),
                icon='fa-book',
                #url=reverse('%s:index' % admin_site_name),
                description=('Sổ tiết kiệm'),

                children= [
                    items.MenuItem(
                        title='Mở Sổ tiết kiệm',
                        url=reverse('admin:qlsotietkiem_khachhang_add'),
                        description=('Mở sổ tiết kiệm cho khách hàng')
                    ),

                    items.MenuItem(
                        title='Tra cứu Sổ tiết kiệm',
                        url=reverse('admin:qlsotietkiem_sotietkiem_changelist'),
                        description=('Tra cứu danh sách sổ tiết kiệm')
                    ),
                    ]
            ),

            items.MenuItem(
                title=('Phiếu gửi tiền - rút tiền'),
                icon='fa-tasks',
                #url=reverse('%s:index' % admin_site_name),
                description=('Lập phiếu gửi tiền - rút tiền cho khách hàng sở hữu sổ tiết kiệm'),

                children= [
                    items.MenuItem(
                        title='Lập phiếu gửi tiền',
                        url=reverse('admin:qlsotietkiem_phieu_add') + '?loai_phieu=GUI',
                        description=('Lập phiếu gửi tiền đối với loại tiết kiệm không kỳ hạn')
                    ),

                    items.MenuItem(
                        title='Lập phiếu rút tiền',
                        url=reverse('admin:qlsotietkiem_phieu_add') + '?loai_phieu=RUT',
                        description=('Lập phiếu rút tiền từ sổ tiết kiệm')
                    ),
                    ]
            ),

            items.MenuItem(
                title=('Báo cáo'),
                icon='fa-files-o',
                #url=reverse('%s:index' % admin_site_name),
                description=('Báo cáo doanh thu theo ngày và tình trạng đóng/mở sổ tiết kiệm theo tháng'),

                children= [
                    items.MenuItem(
                        title='Báo cáo doanh thu ngày',
                        url='/admin/qlsotietkiem/baocao/DoanhThuNgay/',
                        description=('Báo cáo tổng thu, chi các loại tiết kiệm')
                    ),

                    items.MenuItem(
                        title='Báo cáo đóng/mở sổ tháng',
                        url='/admin/qlsotietkiem/baocao/DongMoSoThang/',
                        description=('Báo cáo về số sổ tiết kiệm được mở/đóng trong tháng')
                    ),
                    ]
            ),

            items.MenuItem(
                title=('Cấu hình'),
                icon='fa-gears',
                description=('Các thay đổi về loại tiết kiệm: kỳ hạn, lãi suất, tiền gửi/thời gian gửi tối thiểu'),

                children=[
                    items.MenuItem(
                        title='Thay đổi kỳ hạn, lãi suất, tiền gửi/thời gian gửi tối thiểu',
                        url=reverse('admin:qlsotietkiem_loaitietkiem_changelist'),
                        description=('Thay đổi kỳ hạn, lãi suất, tiền gửi/thời gian gửi tối thiểu')
                    ),
                    ]
            ),

            items.MenuItem(
                title=('Thoát'),
                icon='fa-moon-o',
                url=reverse('admin:logout'),
                css_styles='float:right',
                description=('Thoát ứng dụng Web'),

                children= [
                    items.MenuItem(
                        title='Đổi mật khẩu',
                        url=reverse('admin:password_change'),
                        description=('Đổi mật khẩu người dùng')
                    )
                ]
            ),
        ]

        if self.my_user_check(context.get('request').user):
            self.children += [
                items.AppList(
                    title=_('Applications'),
                    icon='fa-tasks',
                    exclude=('django.contrib.*',),
                ),
                items.AppList(
                    title=_('Administration'),
                    icon='fa-cog',
                    models=('django.contrib.*',),
                ),
                items.UserTools(
                    css_styles='float: right;',
                ),
            ]

        # self.children += [
        #     items.MenuItem(
        #         title=_('Color theme'),
        #         icon='fa-spinner',
        #         description=_('Change color theme'),
        #         css_styles='float: right;',
        #         children=[
        #             items.MenuItem(
        #                 title='Blue',
        #                 url='javascript:change_color_theme("blue");',
        #             ),
        #             items.MenuItem(
        #                 title='Coffee',
        #                 url='javascript:change_color_theme("coffee");',
        #             ),
        #             items.MenuItem(
        #                 title='Default',
        #                 url='javascript:change_color_theme("default");',
        #             ),
        #             items.MenuItem(
        #                 title='Ectoplasm',
        #                 url='javascript:change_color_theme("ectoplasm");',
        #             ),
        #             items.MenuItem(
        #                 title='Light',
        #                 url='javascript:change_color_theme("light");',
        #             ),
        #             items.MenuItem(
        #                 title='Milo',
        #                 url='javascript:change_color_theme("milo");',
        #             ),
        #             items.MenuItem(
        #                 title='Milo Light',
        #                 url='javascript:change_color_theme("milo-light");',
        #             ),
        #             items.MenuItem(
        #                 title='Midnight',
        #                 url='javascript:change_color_theme("midnight");',
        #             ),
        #             items.MenuItem(
        #                 title='Ocean',
        #                 url='javascript:change_color_theme("ocean");',
        #             ),
        #             items.MenuItem(
        #                 title='Sunrise',
        #                 url='javascript:change_color_theme("sunrise");',
        #             ),
        #         ]
        #     ),
        # ]


class UserLeftMenu(Menu):

    def is_user_allowed(self, user):
        """
        Only users that are in 'users' group are allowed to see this menu.
        """
        return user.groups.filter(name='users').count()

    def init_with_context(self, context):

        if self.is_user_allowed(context.get('request').user):

            admin_site_name = get_admin_site_name(context)

            self.children += [
                items.MenuItem(
                    title=_('Dashboard'),
                    icon='fa-tachometer',
                    url=reverse('%s:index' % admin_site_name),
                    description=_('Dashboard'),
                ),
                items.MenuItem(
                    title=_('Books'),
                    icon='fa-book',
                    url=reverse('%s:books_book_changelist' % admin_site_name),
                ),
                items.MenuItem(
                    title=_('CDs'),
                    icon='fa-music',
                    url=reverse('%s:cds_cd_changelist' % admin_site_name),
                ),
                items.MenuItem(
                    title=_('DVDs'),
                    icon='fa-film',
                    url=reverse('%s:dvds_dvd_changelist' % admin_site_name),
                ),
            ]
