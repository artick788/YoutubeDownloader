# YoutubeDownloader
YoutubeDownloader is a simple program that allows you to download videos from YouTube while also specifying some metadata. 
A lot of other sites do exist, but they mostly have a lot of ads and are not very user friendly. This program is made to 
be as simple as possible. It is also really useful to specify the metadata, as this will be added to the musicfile tags.

Most youtube video titles also contain a lot of extra information in the title (things like Originam Mix, Official Video, etc.).
This program will automatically remove this information from the title, so you can easily add it to the metadata.
The resulting file will be stored in the root of the project and will have the following format:
```
{artist} - {title}.mp3
```

The program is written in Python and uses GLFW and ImGui (OpenGL) to draw the GUI. The program is also cross-platform.

## Installation
To install the program, you need to have Python 3.6 or higher installed. You can download it from [here](https://www.python.org/downloads/).
After that, you need to install the dependencies. You can do this by running the following command in the terminal:
```
pip3 install -r requirements.txt
```
After that, you can run the program by running the following command in the terminal:
```
python3 main.py
```

## Note
As I wrote this program within 2 hours, it will probably not be the most elegant code.
Also don't expect things like unit tests or documentation. I will probably add them later, but for now, this is it.
