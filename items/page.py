from toapi import Item, XPath


class Page(Item):
    next_page = XPath('//a[@class="morelink"]/@href')

    def clean_next_page(self, next_page):
        return "/https://news.ycombinator.com/" + next_page

    class Meta:
        source = None
        route = '/news\?p=\d+'
