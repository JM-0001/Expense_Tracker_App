from abc import ABC, abstractmethod
import datetime, csv
from typing import List

class Expense:

    def __init__(self, id:int, date: datetime.date, amount:float, category:str, description:str):
        self._id = id
        self._date = date
        self._amount = amount
        self._category = category
        self._description = description

    def get_amount(self):
        return self._amount

    def set_amount(self, amount:float):
        self._amount = amount

    def category(self):
        return self._category
    
    def set_category(self, category:str):
        self._category = category
    
    def description(self):
        return self._description
    
    def set_description(self, description:str):
        self._description = description

    def calculate_total(self) -> float:
        return self._amount 

class ExpenseTracker:

    def __init__ (self):
        self._expenses: List[Expense] = []

    def add_expense(self, expense:Expense):
        self._expenses.append(expense)
    
    def remove_expense(self, expense_id:int) -> bool:
        for i, expense in enumerate(self._expenses):
            if expense._id == expense_id:
                self._expenses.pop(i)
                return True 
        return False
    
    def generate_report(self) -> str:
        report_list = []
        for expense in self._expenses:
            line = f"${expense._amount:.2f} - {expense._category}"
            report_list.append(line)
        return "\n".join(report_list) 

    def handle_invalid_expense(self):
        raise ValueError("Invalid expense.")

class CategoryManager:
    def __init__(self):
        self.categories: List[str] = []

    def add_category(self, cat: str):
        if cat not in self.categories:
            self.categories.append(cat) 
        else: 
            print("Category already exist")
    
    def remove_category(self, cat:str):
        if cat in self.categories:
            self.categories.remove(cat)
            return True # removed succesfully
        return False # failed to remove, possibly na remove na 
    
    def list_category(self): 
        print(self.categories)

    def validate_category(self, category:str) -> bool :
        return category in self.categories
''' 
class ExportFileManager:
    def __init__(self, filename:str, expenses:List[Expense]):
        self.filename = filename
        self.expenses = expenses

    def save_to_file(self) -> None:
        with open(self.filename, "w") as file:
            writer = csv.writer(file)

    def load_to_file(self, filename:str) -> List[Expense]:
        pass
'''
class Controller:
    def __init__(self):
        self._expense_tracker = None
        self._category_manager = None
        self._file_manager = None

    def handle_event(self, event: str, data: dict) -> None:
        pass

    def load_expenses(self) -> None:
        pass

    def save_expenses(self) -> None:
        pass

# nag base lang ako sa uml diagram - kaizen