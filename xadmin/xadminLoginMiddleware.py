from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin
# from common import client
from django.conf import settings
from django.http import HttpResponseRedirect
class AutomaticLoginUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.user.is_authenticated():
                return
        except AttributeError:
            pass
        if not request.path_info.startswith('/xadmin'):
            return

        try:
            username = request.GET["username"]
            password = request.GET["password"]
        except:
            return

        user = auth.authenticate(username=username, password=password)
        # user = auth.authenticate(username='weiying', password='ab123456')
        xadminExitLocalUrl = settings.XADMIN.get("ExitLocalUrl")
        # print(user,'uuuuuuu')
        if user:
            request.session['xadminExitLocalUrl'] = xadminExitLocalUrl
            # print(xadminExitLocalUrl)
            request.user = user
            auth.login(request, user)
        #     return
        else:
            # 如果这样会有bug，所有xadmin里面的东西，都会直接跳转到报表系统  已修复
            return HttpResponseRedirect(xadminExitLocalUrl)