# 9anime-scrapper
scrape download links of your favourite animes

## How it works
For all the download links check ***dwnld_links.txt*** on your system and use ***IDM***(windows) ,***uGet***(ubuntu) to download this batch.
Or use [jdownloader] for any platform.

## Deployment
```
Usage: 9anime.py [options] url
    url: the url of the anime (ex:http://9anime.to/watch/masamune-kun-no-revenge.pyr9)

    Additional:

    The episode paramter allows to specify a range delimited by '-'

    -e 7-  #=> downloads all episodes from episode 4 and onward
    -e -7  #=> downloads episodes 1-4
    -e 3-5 #=> downloads episodes 3-5 ( shortcut for -s 3 -f 5 )
    -e 7 #=> downloads episode 7 ( shortcut for -s 7 -f 7 )

Options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output=OUTPUT
                        write report to FILE [default: dwnld_links.txt]
  -s START, --start=START
                        episode to begin with [default: 1]
  -f FINISH, --finish=FINISH
                        episode to finish with [default: none]
  -e EPISODE, --episode=EPISODE
                        episode to download. Can also use a range: (ex: 4- all
                        episodes from for on) [default: none]
  -r RESOLUTION, --resolution=RESOLUTION
                        resolution of download: 360p, 480p, 720p, 1080p
                        [default: 720p]
```


To download using uget copy the all the content of the txt and just select "New Clipboard batch...".
useing [jdownloader] just paste all the links into it.

[jdownloader]: http://www.jdownloader.org/download/index

## Prerequisites
* Python
* Modules(download and install modules given below)
### Installation of modules
Example:
```
sudo pip install bs4
```
```
sudo pip install requests
```
```
sudo pip install lxml
```

## Authors

* **yozo06**
* **danielb2**

## Acknowledgments
* **jQwotos** for his work that I referred.
