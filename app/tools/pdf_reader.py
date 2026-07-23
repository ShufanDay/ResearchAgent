from pypdf import PdfReader
from .base_tool import BaseTool

class PDFReaderTool(BaseTool):
    @property
    def name(self):
        return "pdf_reader"
    @property
    def description(self):
        return "读取PDF文件内容"
    def run(self, path):
        reader = PdfReader(path)

        text = []

        for page in reader.pages:
            content = page.extract_text()

            if content:
                text.append(content)
        return "\n".join(text)
            

    
if __name__ == '__main__':
    tool = PDFReaderTool()
    text = tool.run("./2026acl.pdf")

    print(text)