from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=30)
pdf.cell(w=0, text= "CS50 Shirtificate", align= "C")
pdf.image("shirtificate.png", x=10, y=50, w=190)
pdf.set_text_color(255, 255, 255)
pdf.set_y(130)  # position vertically on the shirt
pdf.cell(w=0, text=f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")