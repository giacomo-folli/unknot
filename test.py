from lib.generator import Generator
from os import listdir
import json

if __name__ == "__main__":
    Generator.generate_template(
        template="template/layout.templ",
        prompt="In cosa oggi sono stato 'abbastanza'?",
        mantra="La mia bellezza sta nelle mie imperfezioni.",
        theme="Settimana 1: Accogliere l'Imperfezione",
        free="Come mi sono sentito accogliendo l'imperfezione?",
        output_path=f"parsed_test/test.html",
    )

    templates = [f for f in listdir("parsed_test")]

    for template in templates:
        template_path = f"parsed_test/{template}"
        pdf_path = Generator.generate_pdf(template_path)
