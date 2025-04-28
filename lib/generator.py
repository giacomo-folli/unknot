from lib.parser import Parser
import pdfkit


class Generator:
    def generate_template(
        template: str,
        mantra: str,
        theme: str,
        free: str,
        prompt: str,
        output_path: str,
    ):
        parser = Parser(
            template,
            mantra,
            theme,
            free,
            prompt,
        )
        parsed_content = parser.parse()

        with open(output_path, "+w") as f:
            f.write(parsed_content)

    def generate_pdf(template_path: str) -> str:
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

        # dir/file_name.html -> file_name
        template_name = template_path.split("/")[1].split(".")[0]
        output_path = f"{pdf_dir}/{template_name}.pdf"

        # Generate PDF
        try:
            pdfkit.from_file(template_path, output_path, options=options)
            print(f"PDF successfully created: {output_path}")
            return output_path
        except Exception as e:
            print(f"Error generating PDF: {e}")
