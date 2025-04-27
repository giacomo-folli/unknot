import pdfkit, json
from lib.parser import Parser
from os import listdir


def generate_from_template(template_path: str) -> str:
    # PDF configuration options for A4 paper
    options = {
        "page-size": "A4",
        "margin-top": "0mm",
        "margin-right": "0mm",
        "margin-bottom": "0mm",
        "margin-left": "0mm",
        "encoding": "UTF-8",
        "no-outline": None,
    }

    # PDF path to save
    pdf_dir = "output"
    output_path = f"{pdf_dir}/{template_path.split("/")[1]}.pdf"

    # Generate PDF
    try:
        pdfkit.from_file(template_path, output_path, options=options)
        print(f"PDF successfully created: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating PDF: {e}")


def generate_templates(template: str):
    with open("data/data.json", "r") as file:
        data = json.load(file)

    i = 0
    for week in data["weeks"]:
        for prompt in week["prompts"]:
            parser = Parser(
                template,
                mantra=week["mantra"],
                theme=week["theme"],
                prompt=prompt,
            )
            parsed_content = parser.parse()

            with open(f"parsed/parsed-temp-{i}.html", "+w") as f:
                f.write(parsed_content)

            i += 1
        i = 0


if __name__ == "__main__":
    generate_templates("template/layout.templ")

    templates = [f for f in listdir("parsed")]

    for template in templates:
        template_path = f"parsed/{template}"
        pdf_path = generate_from_template(template_path)
