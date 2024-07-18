### auto_remove_bg
`Discord bot that can quickly remove background from photos`

<p align="center">
  <img src="https://habrastorage.org/webt/tx/em/e0/txeme0-wb9_zphwweswgrpaojmq.png" alt="Bot Icon" width="270"/>
  <img src="https://habrastorage.org/webt/fg/_0/me/fg_0mexote7jzeukfp3mszsqmws.png" alt="Bot Picture" width="400"/>
</p>

> [!NOTE]
> This is the demo version of this bot -> `0.1`

### Аt the moment the bot can
- Receive photos from the user in formats...

  - PNG
  > The PNG (Portable Network Graphics) format is a graphic image storage format that supports transparency. it provides lossless compression, supports multiple color spaces, and can save images at high quality. png is widely used in web design, as well as in graphic editors for saving images with a transparent background.
  - JPEG
  > JPEG (Joint Photographic Experts Group) is one of the most common image compression formats. It supports millions of colors and provides good image quality at a relatively small file size. jpeg is often used for photographs, web graphics, and other images to reduce file size and speed up data transfer.
  - JPG
  > The JPG format is one of the most popular image compression formats used for storing photographs and other raster images. it allows you to save high quality images in relatively small file sizes. jpg files are easy to open and process on most devices and image editing programs.
  - BMP
  > The BMP (Bitmap Picture) format is an uncompressed image storage format that allows you to save images with high quality and color accuracy. bmp files take up more disk space due to lack of compression, but provide higher image detail. bmp is supported by many image processing programs, but due to its large file sizes it is rarely used for distributing images on the web.

...and return the image in `PNG` format with the background removed.

### In the future it is planned to add
- Parallel processing of multiple images
- The ability to immediately substitute a background image

---

> [!WARNING]
> Images should not occupy more than 15 MB in memory, otherwise they will not be processed

> [!IMPORTANT]
> Images must have an object that is clearly in the foreground, such as a person, animal, product or car. if the image is too large (for example, larger than 4096 x 4096 pixels), the image will be resized to that maximum supported resolution

---

### Localization
`At the moment the bot can communicate in 5 languages`
- English
- Russian
- Spanish
- Chinese
- Arabic

#### To change the language, you need to enter the command `/set_language` + language key from the following list:
- `ru` [Russian]
- `en` [English]
- `es` [Spanish]
- `zh` [Chinese]
- `ar` [Arabic]

#### Example:

`Request`

<img src="https://habrastorage.org/webt/1i/1_/1c/1i1_1crl0qwxwvhz6zebuc5jn1o.png" height="100" width="700"/>

`Response`

<img src="https://habrastorage.org/webt/rq/iw/rt/rqiwrttix-4rzqixffpc6ufvo9g.png" height="100" width="700"/>

#### It works exactly the same with other languages...

`Request`

<img src="https://habrastorage.org/webt/bg/yi/iv/bgyiivkvyi-qzwcut19botcathy.png" height="100" width="700"/>

`Response`

<img src="https://habrastorage.org/webt/sa/jn/ij/sajnijucs8uf9xtrd7qdvfoduhg.png" height="100" width="700"/>

---

### How the bot works

<img src="https://habrastorage.org/webt/n-/vl/7u/n-vl7u2ugsrz-atb5bwlxv-7agi.png" width="700"/>

> [!IMPORTANT]
> Unfortunately, the bot can only process up to 2 images from one account on the [ba-la.ru](https://ba-la.ru/).

---

### How to install
1. Clone the remote repository and go to it:
```
git clone https://github.com/linkoffee/auto_remove_bg.git
```
```
cd auto_remove_bg
```
2. Create and activate a virtual environment:
```
python3 -m venv env
```
```
source env/bin/activate
```
3. Install all required dependencies:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
4. Create your application on the [website](https://discord.com/developers/applications), register the bot.
5. Configure the bot in point `OAuth2`, give it the following privileges: `bot`, `Send Messages`, `Attach Files`.
6. In `OAuth2`, immediately get the url, paste it into the address bar and add it to your discord server.
7. At the `Bot` point, be sure to generate and receive your personal token.
8. Go to the [site](https://ba-la.ru/) to remove the background, register, go to the `API` tab, get your personal token.
9. In the root dir of the project create a file `.env`, add your tokens there, in this format, without quotes and spaces:
```.env
BOT_TOKEN=IHDWd0-whd0widjhWDWA-D0JA-0jdwa.IFHeiwd2.2193u  # Example of bot token.
BALA_TOKEN=iwdhIDHAUWD923od1j9JDJW  # Example of bala token.
```
10. Run the tests, they are in the `tests/` folder:
```
pytest
```
12. Run the bot:
```
python main.py
```

---

### Stack
- python 3.9
- discord.py 2.4.0
- requests 2.26.0
- aiohttp 3.9.5
- asyncio

---

Author: [linkoffee](https://github.com/linkoffee)
