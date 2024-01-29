from django.http import  JsonResponse
from django.shortcuts import redirect, render
from voiceapp.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json

from django.http import HttpResponse
from django.db import connection
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['You', 'Me', 'Us'],   
  }
  return HttpResponse(template.render(context, request))

# def dashboard(request):
#   # books is app name and book is model
#     query = "SELECT * FROM voiceapp.voiceapp_audio_user;"
 
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         results = cursor.fetchall()
 
#     table_html = "<table><tr><th>Title</th><th>Author</th><th>Publication Year</th></tr>"
#     for row in results:
#         table_html += f"<tr><td>{row[1]}</td><td>{row[2]}</td><td></td></tr>"
#     table_html += "</table>"
 
#     # Pass the table_html to the template
#     return render(request, 'voiceapp/categories.html', {'table_html': table_html})

def dashboard(request):
#   categories=Audio.objects.select_related('Catagory_name')
#   # categories=Audio_User.objects.select_related('Audio_name').all()
#   print(categories.count())
#   return render(request,"voiceapp/index.html",{"categories":categories})
    
    categorys = Catagory.objects.all()
    audios = Audio.objects.all()
    audio_users = Audio_User.objects.all()

    context = {
        "categorys":categorys,
        'audios':audios,
        'audio_users':audio_users
    }

    return render(request, 'voiceapp/categories.html', context)
 
   
def home(request):
  products=Audio.objects.filter(Catagory_name_id=1)
  return render(request,"voiceapp/index.html",{"products":products})
  return render(request,"voiceapp/index.html")
  #return render(request,"voiceapp/login.html")
 
# def favviewpage(request):
#   if request.user.is_authenticated:
#     fav=Favourite.objects.filter(user=request.user)
#     return render(request,"voiceapp/fav.html",{"fav":fav})
#   else:
#     return redirect("/")
 
# def remove_fav(request,fid):
#   item=Favourite.objects.get(id=fid)
#   item.delete()
#   return redirect("/favviewpage")
 
 
 
 
# def cart_page(request):
#   if request.user.is_authenticated:
#     cart=Cart.objects.filter(user=request.user)
#     return render(request,"voiceapp/cart.html",{"cart":cart})
#   else:
#     return redirect("/")
 
# def remove_cart(request,cid):
#   cartitem=Cart.objects.get(id=cid)
#   cartitem.delete()
#   return redirect("/cart")
 
 
 
# def fav_page(request):
#    if request.headers.get('x-requested-with')=='XMLHttpRequest':
#     if request.user.is_authenticated:
#       data=json.load(request)
#       product_id=data['pid']
#       product_status=Product.objects.get(id=product_id)
#       if product_status:
#          if Favourite.objects.filter(user=request.user.id,product_id=product_id):
#           return JsonResponse({'status':'Product Already in Favourite'}, status=200)
#          else:
#           Favourite.objects.create(user=request.user,product_id=product_id)
#           return JsonResponse({'status':'Product Added to Favourite'}, status=200)
#     else:
#       return JsonResponse({'status':'Login to Add Favourite'}, status=200)
#    else:
#     return JsonResponse({'status':'Invalid Access'}, status=200)
 
 
# def add_to_cart(request):
#    if request.headers.get('x-requested-with')=='XMLHttpRequest':
#     if request.user.is_authenticated:
#       data=json.load(request)
#       product_qty=data['product_qty']
#       product_id=data['pid']
#       #print(request.user.id)
#       product_status=Product.objects.get(id=product_id)
#       if product_status:
#         if Cart.objects.filter(user=request.user.id,product_id=product_id):
#           return JsonResponse({'status':'Product Already in Cart'}, status=200)
#         else: 
#           if product_status.quantity>=product_qty:
#             Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
#             return JsonResponse({'status':'Product Added to Cart'}, status=200)
#           else:
#             return JsonResponse({'status':'Product Stock Not Available'}, status=200)
#     else:
#       return JsonResponse({'status':'Login to Add Cart'}, status=200)
#    else:
#     return JsonResponse({'status':'Invalid Access'}, status=200)
 
# def logout_page(request):
#   messages.success(request,"Logged out Successfully")
#   if request.user.is_authenticated:
#     logout(request)
#     messages.success(request,"Logged out Successfully")
#   return redirect("/")

# def logout_view(request):
#     logout(request)
#     return redirect('/')
 
# def login_page(request):
#   if request.user.is_authenticated:
#     return redirect("/")
#   else:
#     if request.method=='POST':
#       name=request.POST.get('username')
#       pwd=request.POST.get('password')
#       user=authenticate(request,username=name,password=pwd)
#       if user is not None:
#         login(request,user)
#         messages.success(request,"Logged in Successfully")
#         return redirect("/")
#       else:
#         messages.error(request,"Invalid User Name or Password")
#         return redirect("/login")
#     return render(request,"voiceapp/login.html")
 
# def register(request):
#   form=CustomUserForm()
#   if request.method=='POST':
#     form=CustomUserForm(request.POST)
#     if form.is_valid():
#       form.save()
#       messages.success(request,"Registration Success You can Login Now..!")
#       return redirect('/login')
#   return render(request,"voiceapp/register.html",{'form':form})
 
 
# def collections(request):
#   catagory=Catagory.objects.filter(status=0)
#   return render(request,"voiceapp/collections.html",{"catagory":catagory})
 
# def collectionsview(request,name):
#   if(Catagory.objects.filter(name=name,status=0)):
#       products=Product.objects.filter(category__name=name)
#       return render(request,"voiceapp/products/index.html",{"products":products,"category_name":name})
#   else:
#     messages.warning(request,"No Such Catagory Found")
#     return redirect('collections')
 
 
# def product_details(request,cname,pname):
#     if(Catagory.objects.filter(name=cname,status=0)):
#       if(Product.objects.filter(name=pname,status=0)):
#         products=Product.objects.filter(name=pname,status=0).first()
#         return render(request,"voiceapp/products/product_details.html",{"products":products})
#       else:
#         messages.error(request,"No Such Produtct Found")
#         return redirect('collections')
#     else:
#       messages.error(request,"No Such Catagory Found")
#       return redirect('collections')