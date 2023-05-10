from django.shortcuts import render, redirect
from .models import Expense, Category
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    categories = Category.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)
    return render(request, 'home.html', {'expenses': expenses, 'categories': categories, 'total_expenses': total_expenses})

@login_required(login_url='/accounts/login/')
def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        Expense.objects.create(title=title, amount=amount, category=Category.objects.get(name=category), user=request.user)
        return redirect('home')
    else:
        categories = Category.objects.all()
        return render(request, 'add_expense.html', {'categories': categories})



from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/accounts/profile/' # ログインに成功した後にリダイレクトするURL

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
