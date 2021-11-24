# 导入命令参数

完成配置文件修改后，可以运行以下命令将指定来源的数据导入 Nebula Graph 数据库。

- 首次导入

  ```bash
  <spark_install_path>/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-2.x.y.jar_path> -c <application.conf_path> 
  ```

- 导入 reload 文件
  
  如果首次导入时有一些数据导入失败，会将导入失败的数据存入 reload 文件，可以用参数`-r`尝试导入 reload 文件。
  
  ```bash
  <spark_install_path>/bin/spark-submit --master "local" --class com.vesoft.nebula.exchange.Exchange <nebula-exchange-2.x.y.jar_path> -c <application.conf_path> -r "<reload_file_path>" 
  ```

!!! note
    JAR 文件版本号以实际编译得到的 JAR 文件名称为准。

!!! note

    如果使用 [yarn-cluster 模式](https://spark-reference-doc-cn.readthedocs.io/zh_CN/latest/deploy-guide/running-on-yarn.html) 提交任务，请参考如下示例：

    ```bash
    $SPARK_HOME/bin/spark-submit     --master yarn-cluster \
    --class com.vesoft.nebula.exchange.Exchange \
    --files application.conf \
    --conf spark.driver.extraClassPath=./ \
    --conf spark.executor.extraClassPath=./ \
    nebula-exchange-{{exchange.release}}.jar \
    -c application.conf
    ```

下表列出了命令的相关参数。

| 参数 | 是否必需 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `--class`  | 是 | 无 | 指定驱动的主类。 |
| `--master`  | 是 | 无 | 指定 Spark 集群中 master 进程的 URL。详情请参见 [master-urls](https://spark.apache.org/docs/latest/submitting-applications.html#master-urls "点击前往 Apache Spark 文档")。 |
| `-c`  / `--config`  | 是 | 无 | 指定配置文件的路径。 |
| `-h`  / `--hive`  | 否 | `false` | 添加这个参数表示支持从 Hive 中导入数据。 |
| `-D`  / `--dry`  | 否 | `false` | 添加这个参数表示检查配置文件的格式是否符合要求，但不会校验`tags`和`edges`的配置项是否正确。正式导入数据时不能添加这个参数。 |
|-r / --reload | 否  |  无  |   指定需要重新加载的 reload 文件路径。 |

更多 Spark 的参数配置说明请参见 [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html#runtime-environment)。
