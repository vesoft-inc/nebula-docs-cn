# 使用Tag索引提高查询效率

如果需要根据Tag进行查询，Nebula Graph支持为Tag创建索引，提高查询效率。

## 原理

在Neo4j中，可以为点添加label，通过label可以快速筛选需要的点。

Nebula Graph支持通过Tag实现相同的操作，创建Tag并将Tag插入到已有的点上，就可以根据Tag名称快速查找点，也可以通过`DELETE TAG`删除某些点上不再需要的Tag。

!!! caution

    请确保点上已经有另一个Tag，否则删除点上最后一个Tag时，会导致点也被删除。

## 示例

例如在basketballplayer数据集中，部分篮球运动员同时也是球队股东，可以为股东Tag`shareholder`创建索引，方便快速查找。如果不再是股东，可以通过`DELETE TAG`语句删除相应运动员的股东Tag。

示例：

```ngql
//创建股东Tag和索引，插入测试数据
nebula> CREATE TAG shareholder ();
nebula> CREATE TAG INDEX shareholder_tag on shareholder();
nebula> INSERT VERTEX shareholder() VALUES "player100":();
nebula> INSERT VERTEX shareholder() VALUES "player101":();

//快速查询所有股东
nebula> MATCH (v:shareholder) RETURN v;
+---------------------------------------------------------------------+
| v                                                                   |
+---------------------------------------------------------------------+
| ("player100" :player{age: 42, name: "Tim Duncan"} :shareholder{})  |
+---------------------------------------------------------------------+
| ("player101" :player{age: 36, name: "Tony Parker"} :shareholder{}) |
+---------------------------------------------------------------------+
nebula> LOOKUP ON shareholder;
+-------------+
| VertexID    |
+-------------+
| "player100" |
+-------------+
| "player101" |
+-------------+

//如果player100不再是股东
nebula> DELETE TAG shareholder FROM "player100";
nebula> LOOKUP ON shareholder;
+-------------+
| VertexID    |
+-------------+
| "player101" |
+-------------+
```

!!! note

    如果插入测试数据后才创建索引，请用`REBUILD TAG INDEX <index_name_list>;`语句重建索引。