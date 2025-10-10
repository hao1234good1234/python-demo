# 🖥️ 第五步：命令行入口（`main.py`）
import logging  # 👈 只在这里 import logging 用于配置

# 🔧【唯一配置点】设置日志格式、级别、输出位置
logging.basicConfig(
    level=logging.INFO,  # 显示 INFO 及以上级别
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True  # Python 3.8+：强制覆盖可能存在的旧配置
)
# 然后导入你的业务代码（注意：导入必须在 basicConfig 之后！）
from core.services import LibraryService
from infrastructure.in_memory_repos import InMemoryBookRepo, InMemoryUserRepo
from core.models import User

def main():
    # 初始化依赖
    book_repo = InMemoryBookRepo()
    user_repo = InMemoryUserRepo()

    # 初始化业务逻辑
    library = LibraryService(book_repo, user_repo)

    # 添加测试用户
    user_repo.save(User("u1", "Alice"))

    # 添加测试图书
    library.add_book("978-0134685991", "西游记", "吴承恩")
    library.add_book("978-1492051299", "水浒传", "施耐庵")

    print("\n 当前的图书库:")
    for book in book_repo.list_all():
        print(book)
    # 查询图书是否可借阅
    print("可借阅" if library.is_available("978-1492051299") else "不可借阅")

    # 用户借阅图书
    success = library.borrow_book("978-1492051299", "u1")
    print(f"借阅结果: {success}")  # True


    # 查询用户借阅的图书
    print("Alice's books:", [b.title for b in library.get_user_books("u1")])

    # 用户还书
    library.return_book("978-1492051299")

    # 查询用户借阅的图书
    print("Alice's books:", [b.title for b in library.get_user_books("u1")])


if __name__ == "__main__":
    main()

# ✅ **关键**：`basicConfig` 必须在 **任何业务模块被导入之前** 调用！