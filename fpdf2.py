# https://docs-python.ru/packages/modul-fpdf2-python/

from fpdf import FPDF, HTMLMixin, __version__ as ver
print('Версия FPDF2:', ver)

# наследуемся от классов FPDF и HTMLMixin
# - класс FPDF для создания PDF-документа
# - класс HTMLMixin содержит парсер HTML


class HTML_PDF(FPDF, HTMLMixin):
    pass

# создаем экземпляр
pdf = HTML_PDF()
# директория где лежат системные шрифты Mac OS
font_dir = '/Library/Fonts'
# добавляем TTF-шрифты, поддерживающие кириллицу.
# шрифт FreeSerif
pdf.add_font("Serif", style="", fname=f"{font_dir}/FreeSerif/FreeSerif.ttf", uni=True)
pdf.add_font("Serif", style="B", fname=f"{font_dir}/FreeSerif/FreeSerifBold.ttf", uni=True)
pdf.add_font("Serif", style="I", fname=f"{font_dir}/FreeSerif/FreeSerifItalic.ttf", uni=True)
pdf.add_font("Serif", style="BI", fname=f"{font_dir}/FreeSerif/FreeSerifBoldItalic.ttf", uni=True)
# шрифт FreeSans
pdf.add_font("Sans", style="", fname=f"{font_dir}/FreeSans/FreeSans.ttf", uni=True)
pdf.add_font("Sans", style="B", fname=f"{font_dir}/FreeSans/FreeSansBold.ttf", uni=True)
pdf.add_font("Sans", style="I", fname=f"{font_dir}/FreeSans/FreeSansOblique.ttf", uni=True)
pdf.add_font("Sans", style="BI", fname=f"{font_dir}/FreeSans/FreeSansBoldOblique.ttf", uni=True)
# устанавливаем шрифт по умолчанию
pdf.set_font("Serif", size=13)
# добавляем страницу
pdf.add_page()
# печатаем HTML
pdf.write_html("""
  <h1>ввв</h1>
   
    """)

pdf.output("html.pdf")