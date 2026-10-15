def calculator():
    print("===== 简易计算器 =====")
    print("支持运算：+、-、*、/")
    print("输入 q 退出计算器")

    while True:
        num1 = input("\n请输入第一个数字：")

        if num1.lower() == "q":
            print("感谢使用计算器！")
            break

        try:
            num1 = float(num1)
            operator = input("请输入运算符 (+ - * /)：")
            num2 = float(input("请输入第二个数字："))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("错误：除数不能为 0！")
                    continue
                result = num1 / num2
            else:
                print("错误：不支持的运算符！")
                continue

            print(f"计算结果：{num1} {operator} {num2} = {result}")

        except ValueError:
            print("输入错误：请输入有效的数字！")


if __name__ == "__main__":
    calculator()
