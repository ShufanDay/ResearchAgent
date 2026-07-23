from abc import ABC, abstractmethod

class BaseTool(ABC):
    """
    所有 Tool 的父类
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """ 工具名称 """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """工具描述"""
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """执行工具"""
        pass