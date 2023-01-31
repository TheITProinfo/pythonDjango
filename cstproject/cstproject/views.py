from django.shortcuts import HttpResponse, render


def page_2003(request):
    html = "<h1>this is page 2003! eric run testing</h1>"
    return HttpResponse(html)


def page_2023_view(request):
    html = "<h2>this is page 2023 <br>, <color red> Happy new year 2023!</red></h2>"
    return HttpResponse(html)


def page_index(request):
    html = "<h2> this is index page</h2>"
    return HttpResponse(html)


from django.template import loader


def test_html(request):
    t = loader.get_template('test.html')
    html = t.render()
    return HttpResponse(html)

def page_2(request):
    html="<h2>this is No.2 pages</h2><br>"
    return HttpResponse(html)
def page_3(request):
    html="<h2>this is No.3 page</h2><br>"
    return HttpResponse(html)
def pagen_view(request,pg):
    html='<h1>this is NO{} page<h1> <hr>'.format(pg)
    return HttpResponse(html)
def cal_view(request,n,op,m):
    if op not in ['add','sub','mul']:
        return HttpResponse('operator is invalid')
    result = 0
    if op=='add':
        result= n+m
    elif op=='sub':
        result=n-m
    elif op=='mul':
        result=n*m
    return HttpResponse('the result is {}'.format(result))
# def cst_index(request):
#     t=loader.get_template('cstindex.html')
#     html=t.render()
#     return HttpResponse(html)
def cst_index(request):
    # dic ={}
    # dic ['int']=2023
    # dic['str']='Happy Chinese new year 2023'
    # # dict ['lst'] =['cstcollege','computer course','network technical support']
    # # dict ['func'] = hello

    dic ={}
    dic['flag']=200
    return render(request,'cstindex.html',dic)
# def hello():
#     return 'Happy Chinese new year 2023!'
def aboutus_view(request):
    return render(request, 'aboutus.html')





