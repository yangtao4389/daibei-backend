from __future__ import absolute_import
import xadmin
# from .models import UserSettings, Log
# from xadmin.layout import *
from xadmin import views
from django.utils.translation import ugettext_lazy as _, ugettext




from api.models import APILoan

class GlobalSetting(object):
    # 参考链接：https://blog.csdn.net/bysjlwdx/article/details/80853199
    site_title = '代贝网后台管理'
    # 后台页脚
    site_footer = '219.153.96.167'
    menu_style = "default"  # default

    # def get_site_menu(self):
    #     '''
    #     这里定义后的菜单，则其他菜单不会显示
    #     :return:
    #     '''
    #     return [{
    #         'title': u'预借款人信息表',
    #         'icon': 'info-sign',
    #         'menus': (
    #             {'title': u'预借款人信息表', 'url': self.get_model_url(APILoan, 'changelist'),
    #              'perm': self.get_model_perm(APILoan, 'view'), },
    #
    #         )
    #     },
    #
    #     ]


xadmin.site.register(views.CommAdminView, GlobalSetting)
