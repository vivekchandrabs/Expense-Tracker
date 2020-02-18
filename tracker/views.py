from django.shortcuts import render

from tracker.models import Expense, Income


def get_all_expense(request):
	all_expenses = Expense.objects.all()
	return render(request, "expense.html", {"all_expenses":all_expenses})

def get_all_income(request):
	all_incomes = Income.objects.all()
	return render(request, "income.html", {"all_incomes":all_incomes})