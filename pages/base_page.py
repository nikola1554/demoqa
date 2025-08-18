class BasePage:
    page_url = None

    def __init__(self, page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(self.page_url)
