# дана квадратная картинка из 4 квадратных картинок
# функция должна создавать новую картинку из 4 одинаковых картинок
# на вход функции дается имя файла, левая верхняя координата картинки
# каждую маленькую картинку функция должна поворачивать на 90 последовательно
# 0 90 180 270
# функция сохраняет новую картинку с именем image.png
from PIL import Image


def make_new_image(image_name: str, info: tuple[int, int, int]):
    start_im = Image.open(image_name)
    left, upper, step = info

    crop_im = start_im.crop((left, upper, left + step, upper + step))
    width, height = crop_im.size

    new_im = Image.new('RGB', (width * 2, height * 2), color='#FFFFFF')

    # первая картинка
    new_im.paste(crop_im)
    new_im.paste(crop_im.rotate(-90), (width, 0))
    new_im.paste(crop_im.rotate(-180), (0, height))
    new_im.paste(crop_im.rotate(-270), (width, height))
    new_im.save('result.png')


make_new_image('collage.jpg', (100, 100, 200))