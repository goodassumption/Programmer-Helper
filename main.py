import requests
import os

from src.request import make_request
from src.choose_module import choose_module

def main():
    print('Это - помощник программиста для автоматизации различных рутинных задач при помощи нейросетей')
    choose_module()

if __name__ == '__main__':
    main()