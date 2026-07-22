from os import read
from pypdf import PdfReader

def read_pdf(path:str) -> str:
    """
    读取PDF文本
    """
    try:
        reader = PdfReader(path)
        text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)
    except Exception:

        return ""
    
if __name__ == '__main__':
    text = read_pdf("./2026acl.pdf")

    print(text)