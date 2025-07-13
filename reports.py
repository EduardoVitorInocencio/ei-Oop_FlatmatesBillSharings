import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Gera um relatório em PDF com as informações dos moradores e valores.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="portrait", unit="pt", format="A4")
        pdf.add_page()

        # Caminho da imagem e do arquivo final
        image_path = "files/house.png"
        output_path = f"files/{self.filename}"

        # Título
        pdf.image(image_path, w=30, h=30)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Período
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Moradores
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Salva e abre
        pdf.output(output_path)
        webbrowser.open(output_path)


class FileSharer:
    """
    Compartilha o arquivo PDF gerado usando a API do Filestack.
    """
    def __init__(self, filepath, api_key):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
