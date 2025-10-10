# ✅ 第二步：改造 `main.py` —— 加 CLI 菜单
import logging  # 👈 只在这里 import logging 用于配置

# 🔧【唯一配置点】设置日志格式、级别、输出位置
logging.basicConfig(
    level=logging.INFO,  # 显示 INFO 及以上级别
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True  # Python 3.8+：强制覆盖可能存在的旧配置
)
# 然后导入你的业务代码（注意：导入必须在 basicConfig 之后！）
import sys
from core.services import LibraryService
from infrastructure.json_repos import JsonBookRepo, JsonUserRepo # 用json版本
from core.models import User

def ensure_default_user():
    """
    确保有一个默认用户
    """
    user_repo = JsonUserRepo()
    if not user_repo.get_by_id("u1"):
        user_repo.save(User("u1", "Alice"))
        print("默认用户已创建")
def display_menu():
    print("\n 图书管理系统")
    print("1. 添加图书")
    print("2. 借阅图书")
    print("3. 还书")
    print("4. 查询所有图书")
    print("5. 查询用户借阅的图书")
    print("6. 退出")
def main():
    ensure_default_user()
    book_repo = JsonBookRepo()
    user_repo = JsonUserRepo()
    library = LibraryService(book_repo, user_repo)
    while True:
        display_menu()
        choice = input("\n 请选择操作(1-6)：").strip()
        try:
            if choice == '1':
                isbn = input("请输入 ISBN：").strip()
                title = input("请输入书名：").strip()
                author = input("请输入作者：").strip()
                if not all([isbn, title, author]):
                    print("图书信息不能为空！")
                    continue
                book = library.add_book(isbn,title,author)
                print(f"图书 {book.title} 添加成功！")
            elif choice =='2':
                isbn = input("请输入 ISBN：").strip()
                user_id = input("请输入用户 ID：").strip() or "u1"
                if library.borrow_book(isbn, user_id):
                    book = book_repo.get_by_isbn(isbn)
                    user = user_repo.get_by_id(user_id)
                    print(f"用户 {user.name} 借阅了图书 {book.title}")
                else:
                    print(f"图书 {isbn} 借阅失败！（书不存在/已被借/用户无效）")
            elif choice =='3':
                isbn = input("请输入 ISBN：").strip()
                if library.return_book(isbn):
                    book = book_repo.get_by_isbn(isbn)
                    print(f"图书 {book.title} 还书成功")
                else:
                    print(f"图书 {isbn} 归还失败！（书不存在或未被借出）")
            elif choice =='4':
                books = book_repo.list_all()
                if not books:
                    print("图书库为空！")
                else:
                    print("\n 当前的图书库:")
                    for b in books:
                        status = "已借出" if b.is_borrowed else "可借阅"
                        borrower = f"-> {b.borrowed_by}" if b.borrowed_by else ""
                        print(f"{b.isbn}\t{b.title}\t{b.author}\t{status}{borrower}")
            elif choice == '5':
                user_id = input("请输入用户 ID：").strip() or "u1"
                books = library.get_user_books(user_id)
                user = user_repo.get_by_id(user_id)
                if not books:
                    print(f"用户 {user.name} 没有借阅任何图书！")
                else:
                    print(f"\n 用户 {user.name} 借阅的图书:")
                    for b in books:
                        print(f"{b.isbn}\t{b.title}\t{b.author}")

            elif choice == '6':
                print("再见！")
                break
            else:
                print("无效的操作！请输入 1-6 之间的数字！")

        except KeyboardInterrupt as e:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"发生异常：{e}")
            logging.exception("Unexpected error")

if __name__ == "__main__":
    main() 