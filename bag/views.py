from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# View Bag
def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')

# Add to bag
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)
    

# Adjust bag
def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

# Remove items from bag

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

