import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as a total amount and billing period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in a flat and shares a bill.
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a PDF that contains data about the flatmates such as their names, the amount due, and the billing period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_payment = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_payment = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add an icon
        pdf.image(name="house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert billing period, label, and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=200, h=40, txt="Billing Period", border=0)
        pdf.cell(w=160, h=40, txt=bill.period, border=0, ln=1)

        # Insert name, and amount due by flatmate1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=200, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=160, h=25, txt=flatmate1_payment, border=0, ln=1)

        # Insert name, and amount due by flatmate1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=200, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=160, h=25, txt=flatmate2_payment, border=0)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
