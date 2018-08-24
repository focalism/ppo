from selenium import webdriver
from .context import Context


class ContextFactory:
    def __init__(self):
        pass

    @staticmethod
    def create():
        return Context(webdriver)
