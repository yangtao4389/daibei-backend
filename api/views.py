from django.shortcuts import render,HttpResponseRedirect
from .models import APILoan
from logging import getLogger
import re
logger = getLogger("default")
# Create your views here.

def loan(request):
    '''
    post/get 请求 都跳回到原先的大厅
    text-768:
text-939:
text-268:
    :param request:
    :return:
    '''
    logger.info(request.body)
    if request.method == 'POST':
        name = request.POST.get("text-768")
        phone = request.POST.get("text-939")
        loan_money = request.POST.get("text-268")
        try:
            if len(name)>=5 or len(name)<1:
                raise Exception("name:%s error"%name)

            m = re.findall(r"'13\d{9}|14\d{9}|15\d{9}|16\d{9}|17\d{9}|18\d{9}|19\d{9}'", phone)
            if not m:
                raise Exception("phone:%s error"%phone)


            APILoan.objects.create(
                name=name,
                phone = phone,
                loan_money=float(loan_money)
            )
        except:
            logger.exception("存储出错")


    return HttpResponseRedirect("http://219.153.96.167:8000")