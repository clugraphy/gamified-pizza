from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from cart.forms import CartAddProductForm
from .models import Category, Product
from orders_management.models import Leaderboard, Order, OrderItem


# @login_required
# def leaderboard(request):
#     leaderboard = Leaderboard.objects.all()
#     order = Order.objects.all()
#     orderItem = OrderItem.objects.all()
#     filter = Order.objects.all()
#     filter2 = OrderItem.objects.filter(pizzereum="50")
#     filter1 = Order.objects.order_by("last_name", "email")


#     context = {
#         "leaderboard": leaderboard,
#         "order": order,
#         "orderItem": orderItem,
#         "filter": filter,
#         "filter1": filter1,
#         "filter2": filter2,
#     }

#     return render(request, "leaderboard/leaderboard.html", context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {"category": category, "categories": categories, "products": products}

    return render(request, "product/list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        "product": product,
        "cart_product_form": cart_product_form,
    }

    return render(request, "product/detail.html", context)


def signup_view(request):
    if request.method == "POST":
        email = request.POST["password"]
        password = request.POST["password"]

        # Create user and save to the database
        user = User.objects.create_user(email, password)
        user.save()

    return render(
        request, "registration/signup.html", {"message": "Create new account"}
    )


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("product_list"))
    else:
        return render(
            request, "registration/login.html", {"message": "Invalid credentials."}
        )


def logout_view(request):
    logout(request)
    return render(request, "registration/login.html", {"message": "Logged out."})
