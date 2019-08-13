#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# python manage.py shell
# 与项目进行交互的命令行工具集的入口，项目管理器
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
