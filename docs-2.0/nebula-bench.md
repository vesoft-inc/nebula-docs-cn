# Nebula Bench

Nebula Bench是一款利用LDBC数据集对Nebula Graph进行性能测试的工具。

## 适用场景

- 生成测试数据并导入Nebula Graph。

- 对Nebula Graph集群进行性能测试。

## 测试流程

1. 使用ldbc_snb_datagen生成测试数据。

2. 使用importer导入数据到Nebula Graph。

3. 使用K6（含xk6-nebula插件）进行性能测试。

详细使用说明请参见[Nebula Bench](https://github.com/vesoft-inc/nebula-bench/blob/{{bench.branch}}/README_cn.md)。

