from django.shortcuts import render
from appone.models import User,Product
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.



def auth_user(req):
    msg = " "
    if req.method == "POST":
        formdata = req.POST
       # user=formdata.cleaned_data['username'],
        #pwd=formdata.get('password'),
        instance= User.objects.filter(username=user,password=pwd).first()
        if instance:
            return render(req, 'home.html', {'user: instance'})
        msg = 'Invalid Login Credentials.......!'
    return render(req, 'login.html', {'resp': msg})



def register_user(req):
    msg=" "
    if req.method=="POST":
        formdata = req.POST
        login= User(fullname=formdata.get('fullname'),
                    username=formdata.get('username'),
                    password=formdata.get('password'),
                    email=formdata.get('email'))

        login.save()
        msg='User Registration Successfully.......!'
    return render(req,'register.html',{'resp':msg})








def add_or_update_Product(req):
    msg = ""
    if req.method == "POST":
        data = req.POST
        pid = data.get('id')
        prod = Product.objects.filter(id=pid).first()
        pro = Product(name=data.get('productName'), desc=data.get('description'),
                       price=data.get('price'))
        if prod:
            prod.name = pro.name
            prod.desc = pro.desc
            prod.price = pro.price
            prod.save()
            msg = f"Product ({prod.id}) record Updated.."
        else:
            pro.save()
            msg = f"Product ({pro.id}) record Added.."
    return render(request=req, template_name='home.html',
                  context={
                    'prodlist': Product.objects.all(),

                    'message': msg
            })


def edit_product(req,pid):
    return render(request=req, template_name='home.html',
                  context={
                    'prodlist':Product.objects.all(),
                    'pro': Product.objects.filter(id=pid).first(),
                    'message' : ''
                })


def delete_product(req,pid):
   prod = Product.objects.filter(id=pid).first()
   msg = ''
   if prod:
        prod.delete()
        msg = f'Product({pid}) record removed..!'
   return render(request=req, template_name='employee.html', context={
        'prodlist': Product.objects.all(),

        'message' : msg
    })
