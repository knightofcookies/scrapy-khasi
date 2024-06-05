## Selenium 4 Workaround
This project uses the `scrapy-selenium` package that is no longer maintained.

To implement a workaround (a modified version of the workaround [here](https://www.zenrows.com/blog/scrapy-selenium#implement-selenium4-workaround)), get to the `scrapy-selenium` installation folder: 

```
pip3 show scrapy-selenium 
```

In the folder specified by the `Location` field, open the `scrapy-selenium` directory.

Replace the `middlewares.py` file with the `updated_scrapy_seleniun_middleware_X.py` corresponding to the host operating system in the `scripts` directory of this project.

## Running the spiders
In the outer `khasi_news` directory, run `scrapy crawl <spider_name>`.

Available spiders:
- `rupang`