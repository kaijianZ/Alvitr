# Alvitr
a simple pixiv crawler

## How to use:
```sh
   cd ~
   git clone https://github.com/kaijianZ/Alvitr.git
   cd ./Alvitr
   
   python ./alvitr.py
   python ./alvitr.py date 2017-01-01
   python ./alvitr.py tag 南ことり
```
Request package is required.

the images will be downloaded to WorkingDirectory/images/20xx-xx-xx/ if specific
date is given or today's list will be downloaded when no argument

WorkingDirectory/images/your_tag/ if specific tag is given


## Idea
This is a software that can automatically download the illustrations from pixiv.net. My program uses multi-thread to
improve the performance so it can download the top 50(except Manga) from the daily list in seconds.

## References
1. http://docs.python-requests.org/en/master/
2. http://stackoverflow.com/questions/39706134/return-400-when-login-to-a-website-using-python-requests
3. https://docs.python.org/3/library/threading.html
