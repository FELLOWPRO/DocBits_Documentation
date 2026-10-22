# 用户组、用户和权限

## 创建用户组并测试文档访问权限

在用户组权限已启用的环境中，创建审核用户组并添加无管理员权限的测试用户。允许列出、查看和编辑分配给该用户的发票，保持删除、批量修改和审批权限关闭。保存并重新打开设置，然后以普通用户登录：已分配的发票可见，未分配的对照文档不可见。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/zh.mp4" %}

[观看带字幕的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/zh.html)

这些设置分别回答三个不同的问题：谁可以登录、他们在哪个子组织中工作，以及其所属用户组可以执行哪些操作。

| 如果你需要…… | 打开…… |
| --- | --- |
| 添加或编辑某人的账户 | **设置** → **用户**；然后阅读[用户](users/README.md)。 |
| 管理公司各单位的访问权限 | **设置** → **子组织**；然后阅读[子组织](sub-organizations/README.md)。 |
| 按用户组控制访问权限 | **设置** → **组和权限**；然后阅读[用户组和权限](groups-and-permissions/README.md)。 |

<figure><img src="../../../../.gitbook/assets/prior-t008-zh.png" alt="群组选择面板。"><figcaption><p>群组选择面板。</p></figcaption></figure>

如果用户看不到某份文档或某项操作，请先检查其账户和所属组织，然后检查相关用户组的权限。在更改正式组织的设置前，请使用非管理员测试账户确认普通用户实际拥有的访问权限。
