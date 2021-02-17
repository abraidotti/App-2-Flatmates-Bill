import webbrowser

from fpdf import FPDF

import os


class PdfReport:
    """
    Creates a PDF that contains data about the flatmates such as their names, the amount due, and the billing period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_payment = flatmate1.pays(bill, flatmate2)
        flatmate2_payment = flatmate2.pays(bill, flatmate1)

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add an icon
        pdf.image(name="files/house.png", w=30, h=30)

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
        pdf.cell(w=160, h=25, txt=f"${flatmate1_payment}", border=0, ln=1)

        # Insert name, and amount due by flatmate1
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=200, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=160, h=25, txt=f"${flatmate2_payment}", border=0)

        # Change directory to "files", generate, and open the pdf
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
