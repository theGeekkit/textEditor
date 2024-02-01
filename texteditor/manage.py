#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import tkinter as tk


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'texteditor.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    window = tk.Tk()
    window.title("Text Editor")

    text_edit = tk.Text(window, font="Helvetica 18 bold")
    text_edit.grid(row=0, column=1)    

    window.mainloop()

main()


if __name__ == '__main__':
    main()
