from lib.generator import Generator
from os import listdir
import json


def generate_from_template(template_path: str) -> str:
    # Generate PDF
    return Generator.generate_pdf(template_path)


def generate_templates(template: str):
    with open("data/data.json", "r") as file:
        data = json.load(file)

    i = 1
    j = 1
    for week in data["weeks"]:
        for prompt in week["prompts"]:
            page_number = (j - 1) * 7 + i
            Generator.generate_template(
                template,
                mantra=week["mantra"],
                theme=week["theme"],
                free=week["free"],
                prompt=prompt,
                num=page_number,
                output_path=f"parsed/week-{j}-day-{i}.html",
            )

            i += 1
        j += 1
        i = 0


if __name__ == "__main__":
    generate_templates("template/layout.templ")

    templates = [f for f in listdir("parsed")]

    for template in templates:
        template_path = f"parsed/{template}"
        pdf_path = generate_from_template(template_path)
