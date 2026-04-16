import os 
from pathlib import Path


def read_file():

    # 👉 方法1：基于当前工作目录（程序运行的位置）
    archivo1 = Path(os.getcwd()) / ".." / "resources" / "matrices" / "matriz.txt"
    
    # 👉 方法2：基于当前 .py 文件的位置（更稳定，推荐）
    archivo2 = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"

    # 👉 打印解析后的绝对路径（方便检查路径是否正确）
    print("getcwd()", archivo1.resolve()) 
    print("__file__", archivo2.resolve()) 
    
    try:
        # 👉 方式1：传统打开文件（需要手动关闭）
        readfile = open(archivo2.resolve(), "r")
        readfile.readlines()   # 读取所有行（这里只读取，没有输出）
    finally:
        readfile.close()       # 手动关闭文件（如果忘记会导致资源占用 ❌）

    # 👉 方式2：推荐写法（with 会自动关闭文件 ✔）
    with open(archivo2.resolve(), "r") as readfile:
        print(readfile.readlines())  # 读取并打印所有内容


# 👉 判断当前文件是否是“主程序”
# 如果是直接运行这个文件，就执行 read_file()
# 如果是被其他文件 import，则不会执行
if __name__ == "__main__":
    read_file()

