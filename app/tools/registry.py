from json import tool
from .pdf_reader import PDFReaderTool

# 工具注册中心
class ToolRegistry:
    def __init__(self):
        self.tools = {} # 空的工具箱，用来存放工具

    def register(self, tool): # 存放工具
        self.tools[tool.name] = tool

    def get(self, name): # 获取工具
        return self.tools.get(name)
    
    def execute(self, name, *args): # 执行工具
        tool = self.get(name)
        if tool is None:
            raise ValueError(f"{name}不存在")
        
        return tool.run(*args)


tool_registry = ToolRegistry()
tool_registry.register(PDFReaderTool())

