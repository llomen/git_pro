"""
IPAD自动化测试
肖子淅
日期：2023年01月31日
"""
import pytest

@pytest.fixture()
def myfixture(self):
    a = [1, 2, 3, 4]
    yield a
