from UrlManager import UrlManager

objs = {
        "https://www.gutenberg.org/files/1342/1342-0.txt":"Pride And Prejudice.txt",
        "https://www.gutenberg.org/files/11/11-0.txt":"Alice's Adventures in Wonderland.txt",
        "http://www.gutenberg.org/cache/epub/16328/pg16328.txt":"Beowulf.txt",
        "https://www.gutenberg.org/files/1661/1661-0.txt":"The Adventures of Sherlock Holmes.txt",
        "https://www.gutenberg.org/files/1952/1952-0.txt":"The Yellow Wallpaper.txt",
        "https://www.gutenberg.org/files/98/98-0.txt":"A Tale of Two Cities.txt",
        "https://www.gutenberg.org/files/2701/2701-0.txt":"Moby Dick.txt",
        "https://www.gutenberg.org/files/84/84-0.txt":"Frankenstein; Or, The Modern Prometheus.txt",
        "http://www.gutenberg.org/cache/epub/5200/pg5200.txt":"Metamorphosis.txt",
        "http://www.gutenberg.org/cache/epub/1497/pg1497.txt":"The Republic.txt"
    }

manager = UrlManager(objs)
manager.multi_download()

for s in manager.iter():
    print(s)