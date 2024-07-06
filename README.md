### auto_remove_bg
`Discord bot that can quickly remove background from photos`

> [!NOTE]
> This is the demo version of this bot -> 0.1

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

### Stack
- python 3.9
- discord.py 2.4.0
- requests 2.26.0

---

Author: [linkoffee](https://github.com/linkoffee)
