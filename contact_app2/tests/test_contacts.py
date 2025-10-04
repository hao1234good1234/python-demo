from core.contacts import add_contact, find_contact
def test_add_contact():
    """
    测试添加联系人
    """
    contacts = []
    new_contacts = add_contact(contacts, "zhangsan", "13989879023")

    assert len(new_contacts) == 1
    assert new_contacts[0]["name"] == "zhangsan"
    assert new_contacts[0]["phone"] == "13989879023"

def test_find_contact():
    """
    测试查找联系人
    """
    contacts = [
        {"name": "Alice", "phone": "13590899833"},
        {"name": "Bob", "phone": "15638299090"}
    ]

    found = find_contact(contacts, "Alice")
    assert found is not None
    assert found["phone"] == "13590899833"

    not_found = find_contact(contacts, "Charlie")
    assert not_found is None

