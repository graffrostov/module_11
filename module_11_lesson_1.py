# import PIL
from PIL import Image

# ------------------------------------------------------------------------------------------

def rotate(image_path, img_name:str, extension:str, angl:int, qual:int=100):
    """
    Поворачивает изображение на заданный угол.
    Сохраняет результат по месту расположения изображения
    под новым именем с добавлением _rotate к имени файла
    :param image_path: Путь до файла с изображением
    :param img_name: Имя файла изображения
    :param extension: Расширение файла изображения
    :param angl: Угол, на который надо повернуть изображение
    :param qual: Качество для сохраняемого изображения
    :return: Ничего не возвращает
    """

    image = Image.open(image_path + img_name + '.' + extension)
    im_rotate = image.rotate(angl, expand=True)
    im_rotate.save(f'{image_path}{img_name}_rotate.{extension}', quality=qual)
    image.close()
    im_rotate.close()

# ------------------------------------------------------------------------------------------

def flip_image(image_path, img_name:str, extension:str):
    """
    Переворачивает изображение слева направо.
    Сохраняет результат по месту расположения изображения
    под новым именем с добавлением _flip к имени файла
    :param image_path: Путь до файла с изображением
    :param img_name: Имя файла изображения
    :param extension: Расширение файла изображения
    :return: Ничего не возвращает
    """
    image = Image.open(image_path + img_name + '.' + extension)
    im_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
    im_flip.save(f'{image_path}{img_name}_flip.{extension}')
    image.close()
    im_flip.close()

# ------------------------------------------------------------------------------------------

def bw(image_path, img_name:str, extension:str):
    """
       Создаёт чёрно-белое изображение.
       Сохраняет результат по месту расположения изображения
       под новым именем с добавлением _bw к имени файла
       :param image_path: Путь до файла с изображением
       :param img_name: Имя файла изображения
       :param extension: Расширение файла изображения
       :return: Ничего не возвращает
       """
    image = Image.open(image_path + img_name + '.' + extension)
    im_bw = image.convert('L')
    im_bw.save(f'{image_path}{img_name}_bw.{extension}')
    image.close()
    im_bw.close()

# ------------------------------------------------------------------------------------------

def redu(image_path, img_name:str, extension:str, value:int=1):
    """
          Масштабирует изображение.
          Сохраняет результат по месту расположения изображения
          под новым именем с добавлением _bw к имени файла
          :param image_path: Путь до файла с изображением
          :param img_name: Имя файла изображения
          :param extension: Расширение файла изображения
          :param value: Коэффициент масштабирования
          :return: Ничего не возвращает
          """
    image = Image.open(image_path + img_name + '.' + extension)
    im_reduce = image.reduce(value)
    im_reduce.save(f'{image_path}{img_name}_reduce.{extension}')
    image.close()
    im_reduce.close()

# ------------------------------------------------------------------------------------------

# Поворачиваем изображение на 90 градусов
rotate('./img_11/', '1', 'jpg', 90)

# Отражение изображения слева направо
flip_image('./img_11/', '2', 'jpg')

# Чёрно-белое изображение из исходного
bw('./img_11/', '3', 'jpg')

# Масштабирование изображения. В данном случае уменьшение в 2 раза.
redu('./img_11/', '4', 'jpg',2)
