from markdown_pdf import Section, MarkdownPdf

# python -m venv .\.venv
# venv aktivieren mit: .venv\Scripts\activate
# pip install markdown-pdf

changes_2025 = "Aenderungen_zu_2025"
topics_2025 = "IHK-AP1"
filename = topics_2025
path = "ressource\\markdowns\\"

path_filename = path + filename + ".md"

with open(path_filename, "r", encoding="utf-8") as file:
    markdown_content = file.read()

pdf = MarkdownPdf()

pdf.add_section(Section(markdown_content))

pdf.save(filename + ".pdf")

print("PDF has been created!")
