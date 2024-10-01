import requests

from JsonFileOperator import JsonFileOperator


class QQNumberInfo:
    """
    用于查询QQ号码绑定的手机信息的类。

    该类通过API查询QQ号码绑定的手机信息，并根据查询到的地区信息，
    从给定的身份证地区文件中匹配可能的身份证地区。
    """

    def __init__(self, regions_file_path, qq_number):
        """
        初始化方法。

        :param regions_file_path: 字符串，身份证地区文件的路径。
        :param qq_number: 字符串，要查询的QQ号码。
        """
        # 初始化JsonFileOperator实例，用于操作地区文件
        self.json_operator = JsonFileOperator(regions_file_path)
        # 存储要查询的QQ号码
        self.qq_number = qq_number
        # 存储手机号码的地理位置信息
        self.location_of_cell_phone_number = ''

    def qqNumberQueryBindingMobilePhone(self, qq_number):
        """
        通过API查询QQ号码绑定的手机信息。

        :param qq_number: 字符串，要查询的QQ号码。
        :return: 字典，包含手机信息的数据，如果请求失败则返回None。
        """
        # 构建API请求的URL
        url = f"https://api.**********.cc/qqapi?qq={qq_number}"
        # 发送GET请求
        response = requests.get(url)
        if response.status_code == 200:
            # 如果请求成功，提取并返回手机所在地区信息
            # print(response.json())
            data = response.json().get('phonediqu')
            # print(data)
            if data:
                print(data)
                return data
            return None
        else:
            # 如果请求失败，打印错误信息并返回None
            print(f"请求失败，状态码: {response.json()}")
            return None

    def extract_location_from_result(self, result):
        """
        从查询结果中提取手机号码的地理位置信息。

        :param result: 字符串，查询到的手机信息。
        :return: 字符串，提取的地理位置信息，如果无法提取则返回None。
        """
        # 尝试从结果中提取地理位置信息
        if "移动" in result:
            return result.split("移动")[0]
        elif "联通" in result:
            return result.split("联通")[0]
        elif "电信" in result:
            return result.split("电信")[0]
        else:
            return None

    def get_id_card_region(self, location):
        """
        根据地理位置信息获取可能的身份证地区。

        :param location: 字符串，地理位置信息。
        :return: 列表，可能的身份证地区列表。
        """
        # 通过匹配地理位置信息，返回可能的身份证地区列表
        return [key for key, value in self.json_operator.data.items() if location in value]

    def get_id_card_regions(self):
        """
        获取QQ号码绑定的手机信息对应的可能的身份证地区。

        :return: 列表，可能的身份证地区列表。如果无法获取信息，则返回空列表。
        """
        # 首先查询QQ号码绑定的手机信息
        result = self.qqNumberQueryBindingMobilePhone(self.qq_number)
        if result:
            # 提取地理位置信息
            self.location_of_cell_phone_number = self.extract_location_from_result(result)
            if self.location_of_cell_phone_number:
                # 根据地理位置信息获取可能的身份证地区
                return self.get_id_card_region(self.location_of_cell_phone_number)
        # 如果无法获取信息，则返回空列表
        return []


if __name__ == '__main__':
    # 使用示例
    qq_info = QQNumberInfo("regions.json", 3507557934)
    id_card_regions = qq_info.get_id_card_regions()
    print(id_card_regions)
