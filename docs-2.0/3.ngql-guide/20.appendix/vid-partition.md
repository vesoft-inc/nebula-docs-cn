# 点ID和分片ID

## 点ID（`VID`）

在Nebula Graph中，插入点时必须用点ID（`VID`）标识这个点。`VID`有如下特点：

- `VID`数据类型可以为定长字符串或64位整数。

- `VID`在图空间中必须唯一。

- 一个`VID`可以有多个标签（`TAG`）。例如一个人（`VID`）可以有两个角色（`TAG`）。

- 不同图空间中的`VID`是完全独立的。

插入点请参见[INSERT VERTEX](../12.vertex-statements/1.insert-vertex.md)。

## 分片ID

点和边分布在不同的分片，分片分布在不同的机器。如果您需要将某些点放置在相同的分片（例如在一台机器上），可以参考[公式或代码](https://github.com/vesoft-inc/nebula-common/blob/master/src/common/clients/meta/MetaClient.cpp)。

下文用简单代码说明VID和分片的关系。

```
    // 如果ID长度为8，为了兼容1.0，将数据类型视为int64。
    uint64_t vid = 0;
    if (id.size() == 8) {
        memcpy(static_cast<void*>(&vid), id.data(), 8);
    } else {
        MurmurHash2 hash;
        vid = hash(id.data());
    }
    PartitionID pId = vid % numParts + 1;
```

简单来说，上述代码是将一个固定的字符串进行哈希计算，转换成数据类型为int64的数字（int64数字的哈希计算结果是数字本身），将数字取模，然后加1，即：

```C++
pId = vid % numParts + 1;
```

示例的部分参数说明如下。

|参数|说明|
|:---|:---|
|`%`|取模运算。|
|`numParts`|`VID`所在图空间的分片数，即[CREATE SPACE](../9.space-statements/1.create-space.md)语句中的`partition_num`值。|
|`pId`|`VID`所在分片的ID。|

例如有100个分片，`VID`为1、101和1001的三个点将会存储在相同的分片。分片ID和机器地址之间的映射是随机的，所以您不能假定任何两个分片位于同一台机器上。