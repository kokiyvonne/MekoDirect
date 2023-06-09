from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['order.get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete = False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
    
	if request.user.is_authenicated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
		cartItems = order['order.get_cart_items']
 
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.data)
	productId =data['productId']
	action = data['action']
	
	print('Action:', action)
	print('productId:', action)
 
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete = False)

	orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	
	orderItem.save()
	
	if orderItem.quantity <= 0:
		orderItem.delete()
  
	return JsonResponse('Added Successfully!', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		)

	return JsonResponse('Paid!', safe=False)









