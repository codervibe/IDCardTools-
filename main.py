from IDCardTools import IDCardTool
from QQNumberInfo import QQNumberInfo


from IDCardTools import IDCardTool
from QQNumberInfo import QQNumberInfo


def get_idcard_prefix(qq_number, birthday=None):
    """
    根据QQ号码和生日信息获取身份证前缀。

    参数:
    - qq_number: QQ号码，用于获取地区信息。
    - birthday: 生日信息，用于补充身份证号码。

    返回:
    - 如果提供了QQ号码，则返回身份证前缀（地区码+生日）；否则，提示用户输入身份证前14位。
    """
    if qq_number:
        # 根据QQ号码初始化QQNumberInfo对象，获取身份证地区码
        qq_info = QQNumberInfo("regions.json", qq_number)
        id_card_regions = qq_info.get_id_card_regions()
        print(f"id_card_regions:{id_card_regions}")
        # 如果 id_card_regions 为空 打印提示信息 并结束整个进程
        if id_card_regions == []:
            print("无法根据QQ号码 获取身份证地区")
            return input("请输入身份证前14位: ")

        # 检查地区码是否为列表，并与生日信息拼接
        return [region + str(birthday) for region in id_card_regions] if isinstance(id_card_regions, list) and birthday else []

    else:
        # 如果没有提供QQ号码，提示用户直接输入身份证前14位
        return input("请输入身份证前14位: ")


if __name__ == "__main__":
    # 主程序入口
    name = input("请输入姓名: ")
    gender = input("请输入性别 (男/女): ")
    qq_number = input("请输入QQ号码: ")

    # 根据QQ号码是否提供，获取生日信息
    if qq_number:
        birthday = input("请输入生日 (格式例如：19990101): ")
    else:
        birthday = None

    # 获取身份证号前缀
    idcard_prefix = get_idcard_prefix(qq_number, birthday)

    # 如果获取到了身份证前缀，则进行后续处理
    if idcard_prefix:
        # print(idcard_prefix)
        # 创建IDCardTool对象
        tool = IDCardTool()
        # 运行工具
        if isinstance(idcard_prefix, list):
            for prefix in idcard_prefix:
                tool.run(prefix, name, gender)
        else:
            tool.run(idcard_prefix, name, gender)



if __name__ == "__main__":
    # 主程序入口
    name = input("请输入姓名: ")
    gender = input("请输入性别 (男/女): ")
    qq_number = input("请输入QQ号码: ")

    # 根据QQ号码是否提供，获取生日信息
    if qq_number:
        birthday = input("请输入生日 (格式例如：19990101): ")
    else:
        birthday = None

    # 获取身份证号前缀
    idcard_prefix = get_idcard_prefix(qq_number, birthday)

    # 如果获取到了身份证前缀，则进行后续处理
    if idcard_prefix:
        print(f"name:{name}, idcard_prefix:{idcard_prefix} \t 验证需要时间 请耐心等待一会儿.....................")
        # 创建IDCardTool对象
        tool = IDCardTool()
        # 运行工具
        tool.run(idcard_prefix, name, gender)
