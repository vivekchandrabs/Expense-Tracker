from django.shortcuts import render, redirect

from tracker.models import Expense, Income

from datetime import datetime


def get_all_expense(request):
	all_expenses = Expense.objects.all()
	return render(request, "expense.html", {"all_expenses":all_expenses})

def get_all_income(request):
	all_incomes = Income.objects.all()
	return render(request, "income.html", {"all_incomes":all_incomes})

def create_expense(request):
	if request.method == "POST":
		expense_amount = request.POST["expense_amount"]
		expense_title = request.POST["expense_title"]
		expense_description = request.POST["expense_description"]

		expense_instance = Expense.objects.create(
				title=expense_title,
				amount=expense_amount,
				description=expense_description,
				timestamp = datetime.now()
			)

		return redirect("/expense/")
		
	return redirect("/expense/")

def delete_expense(request, expense_id):
	expense_instance = Expense.objects.get(pk=expense_id)
	expense_instance.delete()

	return redirect("/expense/")

def get_expense(request, expense_id):
	expense_instance = Expense.objects.get(pk=expense_id)

	return render(request,
				 "edit_expense.html", {"expense":expense_instance})


def expense_edit(request, expense_id):
	if request.method == "POST":
		expense_title = request.POST["expense_title"]
		expense_amount = request.POST["expense_amount"]
		expense_description = request.POST["expense_description"]

		expense_instance = Expense.objects.get(pk=expense_id)

		expense_instance.title = expense_title
		expense_instance.amount = expense_amount
		expense_instance.description = expense_description

		expense_instance.save()

		return redirect("/expense/")

	return redirect("/expense/")


