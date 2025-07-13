from flat import Bill, Flatmate
from reports import PdfReport, FileSharer
import re

# Entrada de dados do usuário
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = str(input("What is your name? "))
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

# Criação de objetos
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

# Impressão no terminal
print(f"{flatmate1.name} pays: ", round(flatmate1.pays(the_bill, flatmate2), 2))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(the_bill, flatmate1), 2))

# Sanitizar nome do arquivo
safe_period = re.sub(r'\W+', '_', the_bill.period)
pdf_report = PdfReport(filename=f"{safe_period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

