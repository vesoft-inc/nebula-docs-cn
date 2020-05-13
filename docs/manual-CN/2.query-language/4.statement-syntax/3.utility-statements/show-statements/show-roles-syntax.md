# SHOW ROLES 语法

```ngql
SHOW ROLES IN <space_name>
```

`SHOW ROLES` 语句显示分配给用户账户的角色。`SHOW ROLES` 输出以下列：用户账户和角色类型。

如果是 `GOD` 或 `ADMIN` 类型的用户, **Nebula Graph** 返回其权限内的所有用户角色。
如果是 `DBA`、 `USER` 或 `GUEST` 类型的用户, **Nebula Graph** 仅返回其自身角色。

例如：

```ngql
nebula> SHOW ROLES in NBA;
=======================
| Account | Role Type |
=======================
| userA   | ADMIN     |
-----------------------
```

参考 [Create User](../../../../3.build-develop-and-administration/4.account-management-statements/create-user-syntax.md) 创建用户，参考 [Grant Role](../../../../3.build-develop-and-administration/4.account-management-statements/grant-role-syntax.md) 为用户授予角色。
