"""
IPAD自动化测试   pytest 参数传递
肖子淅
日期：2023年01月31日
"""
import pytest


# @pytest.fixture()
# def myfixture():
#     print('this is mine')
#     a = [1,2,3,4]
#     yield a
#
#
# @pytest.mark.usefixtures("myfixture")
# class Test:
#
#     def test_1(self):
#         print()
#
#     def test_2(self):
#         print()

@pytest.fixture(scope='class')
def myfixture(self):
    a = [1, 2, 3, 4]
    #yield a

class Test:
    def test1(self,myfixture):
        print(myfixture)

    def test2(self,myfixture):
        print(myfixture)



if __name__ == '__main__':
    pytest.main()