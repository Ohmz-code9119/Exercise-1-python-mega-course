import glob
from fpdf import FPDF
from pathlib import Path

# first we input the data that needs to be converted into the pdf
filepaths = glob.glob("text_files/*.txt")

# create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # create first page for th pdf file
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=50, h=8, txt=name, ln=1)

pdf.output("output.pdf")









