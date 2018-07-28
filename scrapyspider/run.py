from scrapy import cmdline

name = 'douban_movie_top250'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
