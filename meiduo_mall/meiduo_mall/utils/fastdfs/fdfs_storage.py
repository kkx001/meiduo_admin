# *_*coding:utf-8 *_*
from django.core.files.storage import Storage
from django.conf import settings

class FastDFSStorage(Storage):
    """自定义文件存储系统"""

    def __init__(self, fdfs_base_url=None):
        """
        构造方法。可以不带参数，也可以带参数
        :param fdfs_base_url: Storage的IP
        """
        self.fdfs_base_url = fdfs_base_url or settings.FDFS_BASE_URL

    def _open(self, name, mode='rb'):
        """
        用于打开文件
        :param name: 要打开文件的名字
        :param mode: 打开文件的方式
        :return: None
        """

        # 打开文件时使用的，此时不需要，而文档告诉说明必须实现，所以pass
        pass

    def _save(self, name, content):
        """
        用于保存
        :param name: 要保存文件的名字
        :param content: 要保存文件的内容
        :return: None
        """
        # 保存文件时使用的，此时不需要，而文档告诉说明必须实现，所以pass
        pass

    def url(self, name):
        """
        返回name所指文件的绝对URL
        :param name:要读取文件的引用:group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg
        :return:http://192.168.100.136:8888/group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg
        """

        return self.fdfs_base_url + name

