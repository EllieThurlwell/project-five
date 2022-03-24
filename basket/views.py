from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    """ view to render contents of the basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ view to add specified quantity of an item to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
