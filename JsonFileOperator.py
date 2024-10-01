import json


class JsonFileOperator:
    """
    一个用于操作JSON文件的类，包括加载、保存、查询、添加和删除键值对的功能。
    """

    def __init__(self, filename):
        """
        初始化JsonFileOperator实例。

        参数:
        - filename: JSON文件的名称。
        """
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        """
        加载JSON文件中的数据。
        如果文件不存在或格式错误，将打印错误信息并不进行操作或尝试重新创建文件。
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"文件 {self.filename} 不存在，将创建一个新的空文件。")
        except json.JSONDecodeError:
            print(f"文件 {self.filename} 格式错误，将尝试修复或重新创建。")

    def save(self):
        """
        保存数据到JSON文件中。
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def query(self, key):
        """
        查询给定键的值。

        参数:
        - key: 要查询的键。

        返回:
        - 如果键存在，则返回对应的值；否则返回"未找到"。
        """
        return self.data.get(key, "未找到")

    def add(self, key, value):
        """
        添加一个新的键值对到数据中。

        参数:
        - key: 新的键。
        - value: 新的值。

        返回:
        - 如果键不存在则添加成功，返回True；否则返回False。
        """
        if key not in self.data:
            self.data[key] = value
            return True
        else:
            print(f"键 {key} 已存在，无法添加。")
            return False

    def delete(self, key):
        """
        删除给定键的值。

        参数:
        - key: 要删除的键。

        返回:
        - 如果键存在则删除成功，返回True；否则返回False。
        """
        if key in self.data:
            del self.data[key]
            return True
        else:
            print(f"键 {key} 不存在，无法删除。")
            return False

    def display(self):
        """
        显示数据中的所有键值对。
        """
        for key, value in self.data.items():
            print(f"键: {key}, 值: {value}")


# 以下为使用示例代码的注释，实际使用时应取消注释并执行
# if __name__ == "__main__":
#     # 创建一个操作类实例
#     json_operator = JsonFileOperator("regions.json")
#
#     # 查询特定键的值
#     print("查询结果:")
#     print(json_operator.query("142701"))
#
#     # 添加新的键值对
#     print("\n添加新的键值对:")
#     json_operator.add("152627", "内蒙古自治区乌兰察布盟兴和县")
#
#     # 删除特定键的值
#     print("\n删除特定键的值:")
#     json_operator.delete("152627")
#
#     # 显示所有内容
#     print("\n显示所有内容:")
#     json_operator.display()
#
#     # 保存到文件
#     json_operator.save()
