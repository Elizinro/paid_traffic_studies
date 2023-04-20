def in_group(user: object, group_name: str):
    return user.groups.filter(name=group_name).exists()