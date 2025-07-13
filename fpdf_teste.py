from fpdf import FPDF

pdf = FPDF(
    orientation="portrait",
    unit="pt",
    format="A4"
)

pdf.add_page()

# Add some text
pdf.set_font(family="Times", size=24, style="B")
pdf.cell(w=100, h=80)

