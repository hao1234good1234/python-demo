# 新增：命令行入口
import logging
import click
import os
from dotenv import load_dotenv
from contact_app3.core.contacts import add_contact, find_contact, delete_contact
from contact_app3.core.storage import load_contacts, save_contacts
from contact_app3.models import Contact

load_dotenv()  # 加载 .env配置文件
# 这个库dotenv能自动加载 `.env` 文件中的变量到 `os.environ`
# 从环境变量中读取配置
LOG_FILE = os.getenv("LOG_FILE", "contact_app3.log") #从配置读取，如果没有设置，就使用默认值"contact_app3.log"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# 🔧 配置日志：同时输出到控制台和文件
logging.basicConfig(
    # level=logging.INFO,
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO), # 将字符串转换为日志级别，如果无法转换，使用默认级别INFO
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # 写入文件
        logging.StreamHandler(),  # 输出到终端
    ],
)
# 获取当前模块的日志器
logger = logging.getLogger(__name__)
# 这样所有日志会同时出现在终端和 `contact_app.log` 文件中。


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    """通讯录管理工具"""
    pass

@click.group()
@click.option('--debug', is_flag=True, help="启用调试日志")
def cli(debug):
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("调试模式已开启")


@cli.command()
@click.argument("name")
@click.argument("phone")
def add(name, phone):
    """添加联系人"""
    # 记录用户的操作
    logger.info(f"收到添加请求：name = {name}, phone ={phone}")

    try:
        contacts = load_contacts() # 从"data/contacts.json"文件中加载通讯录对象列表
        contacts = add_contact(contacts, name, phone)
        save_contacts(contacts) # 保存通讯录对象列表到"data/contacts.json"文件中
        logger.info(f"添加联系人成功：name = {name}, phone = {phone}") #成功记录
        click.echo(click.style("✅ 添加成功: name = {name}, phone = {phone}", fg="green"))
    except Exception as e:
        # 记录错误 + 完整堆栈
        logger.error(f"添加联系人失败：{e}", exc_info=True)  #记录错误堆栈
        click.echo(click.style("❌ 添加失败", fg="red", bold=True), err=True)
        raise click.Abort()

@cli.command()
def list():
    """列出所有联系人"""
    logger.info("收到列出联系人请求")
    contacts = load_contacts()  # 从"data/contacts.json"文件中获取通讯录对象列表
    if not contacts:
        logger.warning("通讯录为空")
        click.echo("通讯录为空")
        return
    # 输出通讯录信息
    # 遍历通讯录对象列表，输出每个通讯录对象的信息
    for i, contact in enumerate(contacts, start=1):
        click.echo(f"{i}. {contact.name} - {contact.phone} - {contact.email}")


@cli.command()
@click.argument("name")
def find(name):
    """查找联系人"""
    logger.info(f"收到查找请求：name = {name}")
    contacts = load_contacts()  # 从"data/contacts.json"文件中获取通讯录对象列表
    found_contact = find_contact(contacts, name)
    if found_contact:
        logger.info(f"找到联系人：name = {found_contact.name}, phone = {found_contact.phone}")
        click.echo(f"找到: {found_contact.name} - {found_contact.phone}")
    else:
        logger.warning(f"未找到：name = {name}")
        click.echo(f"未找到: {name}")

@cli.command()
@click.argument("name")
def delete(name):
    """删除联系人"""
    logger.info(f"收到删除请求：name = {name}")
    contacts = load_contacts()
    if name not in (contact.name for contact in contacts):
        logger.info(f"未找到联系人：name = {name}")
        click.echo(click.style("❌ 未找到联系人", fg="red"))
        return
    new_contacts = delete_contact(contacts, name)
    save_contacts(new_contacts)
    logger.info(f"删除联系人成功：name = {name}")
    click.echo(click.style("✅ 删除成功", fg="green"))

if __name__ == "__main__":
    cli()
