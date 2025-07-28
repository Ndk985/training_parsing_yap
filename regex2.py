import re

from bs4 import BeautifulSoup

some_html = """
<article>
  Произвольный текст перемежается ссылками на разные картинки и документы.
  <a href="http://url.com/some_pic.jpg"><img src="..."></a>
  <a href="http://url.com/another_img.jpeg">Ссылка на картинку</a>
  <a href="http://url.com/not_an_image.docx">Документ Word</a>
  <a href="http://url.com/funny_pic.gif">Гифка</a>
  <a href="http://url.com/media1.png"><img src="..."></a>
  <a href="http://url.com/png_sheet.xlsx">Электронная таблица</a>
  <a href="http://url.com/it_s_a_trap.jpg.zip">Архив</a>
  <a href="http://url.com/pdf_with_gif.pdf">Документ PDF</a>
  <a href="http://url.com/something_strange.agif">Неизвестный объект</a>
</article>
"""

soup = BeautifulSoup(some_html, 'lxml')
pattern = re.compile(r'\.(jpg|jpeg|gif|png)$', re.IGNORECASE)

# Находим все <a> с нужным href
pictures = [
    a for a in soup.find_all('a')
    if a.has_attr('href') and pattern.search(a['href'])
]

print(pictures)