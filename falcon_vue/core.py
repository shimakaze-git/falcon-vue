import os
import falcon
import mimetypes
import re

from bs4 import BeautifulSoup


class FalconVueAdapter:
    """This class is a callable taking the form for falcon sink.

    Keyword Arguments:
        src_path (str): vue.js dist directory path
            vue.js dist directory path
        api_url (str): falcon uri_template
            falcon uri_template
    """

    src_path = None
    api_url = None

    def __init__(self, src_path, api_url):
        """
        Parameters
        ----------
        src_path : str
            vue.js dist directory path
        api_url : str
            falcon uri_template
        """
        FalconVueAdapter.src_path = src_path
        FalconVueAdapter.api_url = api_url

    def __call__(self, req, resp):
        req_path = req.path
        file_path = req_path.replace(self.api_url, "", 1)

        filepath = self.src_path + file_path
        if self.api_url == "/":
            filepath = self.src_path + "/" + file_path

        if os.path.isfile(filepath):

            content_type = mimetypes.guess_type(filepath)[0]
            resp.status = falcon.HTTP_200

            file_type = ""
            if content_type:
                content_type_list = content_type.split('/')
                file_type = content_type_list[0]
                resp.content_type = content_type

            if file_type == 'image':
                resp.stream = open(filepath, 'rb')
                resp.stream_len = os.path.getsize(filepath)
            elif file_type == 'text':
                with open(filepath, 'r') as text_file:
                    text_html = text_file.read()
                    text_html = self.replace_static_tag(text_html)
                    resp.body = text_html
            else:
                with open(filepath, 'r') as text_file:
                    text_html = text_file.read()
                    resp.body = text_html
        else:
            resp.status = falcon.HTTP_404

    def replace_static_tag(self, html_text, test=2):
        soup = BeautifulSoup(html_text, "html.parser")
        self.replace_script_tag(soup)
        self.replace_css_tag(soup)
        self.replace_img_tag(soup)

        return soup.prettify(formatter="html")

    def replace_script_tag(self, soup):
        for script in soup.find_all('script', {"src": True}):
            script_src = script['src']

            if self.api_url != '/':
                script['src'] = self.api_url + script_src

    def replace_css_tag(self, soup):
        for css in soup.find_all(href=re.compile("css")):
            css_src = css['href']

            if self.api_url != '/':
                css['href'] = self.api_url + css_src

    def replace_img_tag(self, soup):
        for img in soup.find_all('img', {"src": True}):
            img_src = img['src']

            if self.api_url != '/':
                img['src'] = self.api_url + img_src
