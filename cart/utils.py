def get_cart(request):
    return request.session.get('cart', [])

def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True