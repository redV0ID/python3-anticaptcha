from python3_anticaptcha import ImageToTextTask

ANTICAPTCHA_KEY = ""
# Пример который показывает работу антикапчи при решении капчи-изображением и сохранением её в качестве обычного файла в
# папку
result = ImageToTextTask.ImageToTextTask(anticaptcha_key = ANTICAPTCHA_KEY, save_format = 'const')\
									.captcha_handler('http://85.255.8.26/static/image/common_image_example/800070.png')
print(result)

"""
Данная библиотека реализует два различных метода для сохранения изображений(для последующей их передачи сервису):
1. В качестве временного файла, параметр задаётся по умолчанию, но для того что бы его объявить явно нужно передать
save_format = 'temp' .
2. В качестве обычного файла, для этого нужно передать:
save_format = 'const' .
"""
# Пример который показывает работу антикапчи при решении капчи-изображением и сохранением её в качестве ВРЕМЕННОГО файла
result = ImageToTextTask.ImageToTextTask(anticaptcha_key = ANTICAPTCHA_KEY)\
									.captcha_handler('http://85.255.8.26/static/image/common_image_example/800070.png')
print(result)