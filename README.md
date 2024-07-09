### auto_remove_bg
`Discord bot that can quickly remove background from photos`

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1259774252396056651/1260287979797348516/bot_icon.png?ex=668ec625&is=668d74a5&hm=6850b468e574a5fe7628afdc8c2de27d21f1a4c37d1121b0cf327f245975e82b&" alt="Bot Icon" width="400"/>
  <img src="https://cdn.discordapp.com/attachments/1259774252396056651/1260287696346288370/bot_pic.png?ex=668ec5e1&is=668d7461&hm=0b27a51ef195d515272733d14aefb8ba9a3f4ad844247879da4f907fd38e99fa&" alt="Bot Picture" width="600"/>
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

<img src="https://media.discordapp.net/attachments/1259774252396056651/1260294992543350814/1226.png?ex=668eccad&is=668d7b2d&hm=67282aa97ab7365be954d1c0ab8eefce4d3630cffdbc40e5cd72e06d18d15b7d&=&format=webp&quality=lossless" height="100" width="700"/>

`Response`

<img src="https://media.discordapp.net/attachments/1259774252396056651/1260294992925294642/1227.png?ex=668eccad&is=668d7b2d&hm=ecbc058e77852d56921ba8b914f09dadfb6d5f78aff2fd2f4262c19751f3f553&=&format=webp&quality=lossless" height="100" width="700"/>

#### It works exactly the same with other languages...

`Request`

<img src="https://media.discordapp.net/attachments/1259774252396056651/1260294992027713767/1224.png?ex=668eccad&is=668d7b2d&hm=df147ebc111bf5b6253355e73df0c34da72d17ae735031882c656d98c8a9b7f9&=&format=webp&quality=lossless" height="100" width="700"/>

`Response`

<img src="https://media.discordapp.net/attachments/1259774252396056651/1260294992270852116/1225.png?ex=668eccad&is=668d7b2d&hm=a5f5a1ec99405d718df2021dcf522882b622ae5de411c9e3f9c4d368a4e7742b&=&format=webp&quality=lossless" height="100" width="700"/>

---

### Stack
- python 3.9
- discord.py 2.4.0
- requests 2.26.0
- aiohttp 3.9.5
- asyncio

---

Author: [linkoffee](https://github.com/linkoffee)
