"""
This module contains localized messages for the bot in different languages.

So far only 5 languages ​​are available:
    - English
    - Russian
    - Spanish
    - Chinese
    - Arabic
"""
MESSAGES: dict[str, dict[str, str]] = {
    'en': {
        'START_MSG': 'Hi there! I know how to remove background from images. Post a photo here in png, jpg or bmp format and see for yourself :D',
        'PRE_REMOVE_MSG': 'Accepted! I`m starting to process the image',
        'WAITING_MSG': 'Wait, magic is happening...',
        'RESULT_MSG': 'Hooray! Your image is ready',
        'AGAIN?_MSG': 'Like it? you can send another image',
        'INFO_MSG': 'My name is Auto Remove Bg Bot, so far I can communicate in 5 languages ​​(English, Russian, Spanish, Chinese, Arabic)',
    },
    'ru': {
        'START_MSG': 'Привет! Я умею удалять фон с изображений. Кидай сюда фото в формате png, jpg или bmp и сам в этом убедишься :D',
        'PRE_REMOVE_MSG': 'Принято! Начинаю обрабатывать изображение',
        'WAITING_MSG': 'Подождите, происходит магия...',
        'RESULT_MSG': 'Ура! Ваше изображение готово',
        'AGAIN?_MSG': 'Понравилось? можешь отправить еще одно изображение',
        'INFO_MSG': 'Я - Auto Remove Bg Bot, пока что я умею общаться на 5 языках (английский, русский, испанский, китайский, арабский)',

    },
    'es': {
        'START_MSG': '¡Hola! Sé cómo eliminar el fondo de las imágenes. Publica una foto aquí en formato png, jpg o bmp y compruébalo tú mismo :D',
        'PRE_REMOVE_MSG': '¡Aceptado! Estoy empezando a procesar la imagen',
        'WAITING_MSG': 'Espera, la magia está sucediendo...',
        'RESULT_MSG': '¡Hurra! Tu imagen está lista',
        'AGAIN?_MSG': '¿Como te gusta esto? envía la siguiente imagen',
        'INFO_MSG': 'Mi nombre es Auto Remove Bg Bot, hasta ahora puedo comunicarme en 5 idiomas (inglés, ruso, español, chino, árabe)',
    },
    'zh': {
        'START_MSG': '你好！我知道如何从图像中删除背景。在此发布 png、jpg 或 bmp 格式的照片并亲自查看 :D',
        'PRE_REMOVE_MSG': '公认！我开始处理图像。',
        'WAITING_MSG': '等等，魔法发生了……',
        'RESULT_MSG': '哇，你的图片已经准备好了！',
        'AGAIN?_MSG': '喜欢吗？你可以发送另一张图片吗',
        'INFO_MSG': '我的名字是 Auto Remove Bg Bot，到目前为止我可以用 5 种语言进行交流（英语、俄语、西班牙语、中文、阿拉伯语）',
    },
    'ar': {
        'START_MSG': 'مرحبًا! أنا أعرف كيفية إزالة الخلفية من الصور. انشر صورة هنا بتنسيق png أو jpg أو bmp وشاهد بنفسك :D',
        'PRE_REMOVE_MSG': 'قبلت! لقد بدأت في معالجة الصورة.',
        'WAITING_MSG': 'انتظر، السحر يحدث...',
        'RESULT_MSG': 'مرحا! صورتك جاهزة',
        'AGAIN?_MSG': 'ليس سيئا، أليس كذلك؟ يمكنك إرسال صورة أخرى',
        'INFO_MSG': 'اسمي Auto Remove Bg Bot، حتى الآن يمكنني التواصل بخمس لغات (الإنجليزية، الروسية، الإسبانية، الصينية، العربية)',
    }
}
