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
        if name and phone and loan_money:
            name = name.strip()
            phone = phone.strip()
            loan_money = loan_money.strip()
            try:
                # 验证姓名
                if len(name)>=5:
                    raise Exception("name:%s error"%name)

                # 验证电话
                m = re.match(r"13\d{9}|14\d{9}|15\d{9}|16\d{9}|17\d{9}|18\d{9}|19\d{9}", phone)
                if not m:
                    raise Exception("phone:%s error"%phone)

                # 验证借款金额
                key_words = ["元","万","千","百","十","亿","RMB","人民币"]
                for i in key_words:
                    loan_money = loan_money.replace(i,"")


                APILoan.objects.create(
                    name=name,
                    phone = phone,
                    loan_money=float(loan_money)
                )
            except:
                logger.exception("存储出错")


    return HttpResponseRedirect("/")