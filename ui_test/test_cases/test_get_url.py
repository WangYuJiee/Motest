# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-02-15
"""
import logging

from ui_test.test_cases.url_enable.mo_factory_test import Generator

"""
page object model
```
> pip
```
"""
import seldom


class MoTest(seldom.TestCase):
    """
    page object
    """

    def test_case01(self):
        """
        A simple test
        """
        logging.info("ENTER")
        print("ENTER")
        generator = Generator()
        generator.login_state()

        generator.run()
        print("EXIT")


if __name__ == '__main__':
    seldom.main(browser='chrome', debug=True)
