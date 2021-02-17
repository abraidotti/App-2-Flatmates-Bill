from files.flat import Bill, Flatmate
from files.reports import PdfReport

amount = float(input("Please enter the bill amount: "))
period = input("Please enter the billing period, e.g. 'December 2021': ")
flatmate1_name = input("Please enter the first flatmate's name: ")
flatmate1_days = int(input(f"How many days will {flatmate1_name} be billed for? "))
flatmate2_name = input("Please enter the second flatmate's name: ")
flatmate2_days = int(input(f"How many days will {flatmate2_name} be billed for? "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
