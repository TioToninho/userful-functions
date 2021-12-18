import PyPDF2


def tirar_texto(archive):
    with open(archive, "rb") as pdf_file, open("sample.txt", "w") as text_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            page_content.encode("utf-8")
            text_file.write(page_content)
    txt = open("sample.txt")
    line = txt.read().replace("\n", " ")
    txt.close()
    return line


if __name__ == "__main__":
    tirar_texto(
        "eXtreme Programming Práticas para o dia a dia no desenvolvimento ágil de software.pdf"
    )
