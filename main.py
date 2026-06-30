"""主程序入口"""

def greet(name: str) -> str:
    return f"你好，{name}！欢迎来到 Git 项目。"


if __name__ == "__main__":
    user = input("请输入你的名字：")
    print(greet(user))
