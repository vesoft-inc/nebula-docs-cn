# Built-in Roles

**Nebula Graph** 角色可分为以下几类：

- God
  - 初始 Root 用户（类似于 Linux 系统中的 Root，和 Windows 系统中的 Administrator）。
  - 拥有所有操作权限。
  - 一个集群只能有一个 God。God 可管理集群内所有 space。
  - Meta 服务在初始化时会默认创建一个 GOD 角色的 Account，名为 root。
  - God 角色由 meta 自动初始化，且不支持用户自行授权成为 God。
- Admin
  - 管理员用户。
  - 对权限内的 space 拥有 schema 和 data 的读/写权限。
  - 可对权限内的 space 进行用户授权。
- DBA
  - 对权限内的 space 拥有 schema 和 data 的读/写权限。
  - 没有对用户受权的权限。
- User
  - 对权限内的 space 拥有 data 的读/写权限。
  - 对权限内的 space 拥有 schema 只读权限。
- Guest
  - 对权限内的 space 拥有 schema 和 data 的只读权限。

如果开启用户权限开关，则默认用户名为 root，默认密码为 nebula，且用户名不可更改。将 `/usr/local/nebula/etc/nebula-graphd.conf` 文件中的 `enable_authorize` 设置为 `true` 即可打开权限开关。

未被分配角色的用户将无权访问该 space。一个用户在同一个 space 中只能分配一个角色。一个用户在不同 space 可拥有不同权限。

各角色的 Executor 权限见下表。

按操作权限划分。

| OPERATION | STATEMENTS |
| --- | --- |
| Read space | Use, DescribeSpace |
| Write space | CreateSpace, DropSpace, CreateSnapshot, DropSnapshot, Balance, Admin, Config, Ingest, Download |
| Read schema |  DescribeTag, DescribeEdge,  DescribeTagIndex, DescribeEdgeIndex |
| Write schema | CreateTag, AlterTag, CreateEdge,  AlterEdge, DropTag, DropEdge, CreateTagIndex, CreateEdgeIndex, DropTagIndex, DropEdgeIndex |
| Write user | CreateUser, DropUser, AlterUser |
| Write role | Grant, Revoke |
| Read data | Go, Set, Pipe, Match, Assignment, Lookup, Yield, OrderBy, FetchVertices, Find, FetchEdges, FindPath, Limit, GroupBy, Return |
| Write data | BuildTagIndex, BuildEdgeIndex, InsertVertex, UpdateVertex, InsertEdge, UpdateEdge, DeleteVertex, DeleteEdges |
| Special operation | Show, ChangePassword |

按操作划分。

| OPERATION | GOD | ADMIN | DBA | USER | GUEST |
| --- | --- | --- | --- | --- | --- |
| Read space | Y | Y | Y | Y | Y |
| Write space | Y |  |  |  |  |
| Read schema | Y | Y | Y | Y | Y |
| Write schema | Y | Y | Y |  |  |
| Write user | Y |  |  |  |  |
| Write role | Y | Y |  |  |  |
| Read data | Y | Y | Y | Y | Y |
| Write data | Y | Y | Y | Y |  |
| Special operation | Y | Y | Y | Y | Y |
| Show Jobs | Y | Y | Y | Y | Y |

注意： Special Operation 为特殊操作，例如 `SHOW SPACE`，每个角色都可以执行，但其执行结果只显示 Account 权限内的结果。只有 `GOD` 用户有权限执行 `SHOW USERS` 和 `SHOW SNAPSHOTS` 语句。
