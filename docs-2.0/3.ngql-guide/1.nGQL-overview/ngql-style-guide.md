# nGQL风格指南

nGQL没有严格的构建格式要求，但根据恰当而统一的风格创建nGQL语句有利于提高可读性、避免歧义。在同一组织或项目中使用相同的nGQL风格有利于降低维护成本，规避因格式混乱或误解造成的问题。本文为写作nGQL语句提供了风格参考。

!!! compatibility

    nGQL 风格与[Cypher Style Guide](https://s3.amazonaws.com/artifacts.opencypher.org/M15/docs/style-guide.pdf)不同。

## 换行

1. 换行写子句。

  不推荐：

  ```ngql
  GO FROM "player100" OVER follow REVERSELY YIELD follow._dst AS id;
  ```

  推荐：

  ```ngql
  GO FROM "player100" \
  OVER follow REVERSELY \
  YIELD follow._dst AS id;
  ```

2. 换行写复合语句中的不同语句。

  不推荐：

  ```ngql
  GO FROM "player100" OVER follow REVERSELY YIELD follow._dst AS id | GO FROM $-.id \
  OVER serve WHERE $^.player.age > 20 YIELD $^.player.name AS FriendOf, $$.team.name AS Team;
  ```

  推荐：

  ```ngql
  GO FROM "player100" \
  OVER follow REVERSELY \
  YIELD follow._dst AS id | \
  GO FROM $-.id OVER serve \
  WHERE $^.player.age > 20 \
  YIELD $^.player.name AS FriendOf, $$.team.name AS Team;
  ```

3. 子句长度超过80个字符时，在合适的位置换行。

  不推荐：

  ```ngql
  MATCH (v:player{name:"Tim Duncan"})-[e]->(v2) \
  WHERE (v2.name STARTS WITH "Y" AND v2.age > 35 AND v2.age < v.age) OR (v2.name STARTS WITH "T" AND v2.age < 45 AND v2.age > v.age) \
  RETURN v2;
  ```

  推荐：

  ```ngql
  MATCH (v:player{name:"Tim Duncan"})-[e]->(v2) \
  WHERE (v2.name STARTS WITH "Y" AND v2.age > 35 AND v2.age < v.age) \
  OR (v2.name STARTS WITH "T" AND v2.age < 45 AND v2.age > v.age) \
  RETURN v2;
  ```

!!! note

    即使子句不超过80个字符，如需换行后有助于理解，也可将子句再次分行。

## 标识符命名

在nGQL语句中，关键字、标点符号、空格以外的字符内容都是标识符。推荐的标识符命名方式如下。

1. 使用单数名词命名Tag，用原型动词或动词短语构成Edge type。

  不推荐：

  ```ngql
  MATCH p=(v:players)-[e:are_following]-(v2) \
  RETURN nodes(p);
  ```

  推荐：

  ```ngql
  MATCH p=(v:player)-[e:follow]-(v2) \
  RETURN nodes(p);
  ```

2. 标识符用蛇形命名法，以下划线（_）连接单词，且所有字母小写。

  不推荐：

  ```ngql
  MATCH (v:basketballTeam) \
  RETURN v;
  ```

  推荐：

  ```ngql
  MATCH (v:basketball_team) \
  RETURN v;
  ```

## Pattern

1. 分行写Pattern时，在表示边的箭头右侧换行，而不是左侧。

  不推荐：

  ```ngql
  MATCH (v:player{name: "Tim Duncan", age: 42}) \
  -[e:follow]->()-[e:serve]->()<--(v3) \
  RETURN v, e, v2;
  ```

  推荐：

  ```ngql
  MATCH (v:player{name: "Tim Duncan", age: 42})-[e:follow]-> \
  ()-[e:serve]->()<--(v3) \
  RETURN v, e, v2;
  ```

2. 将无需查询的点和边匿名化。

  不推荐：

  ```ngql
  MATCH (v:player)-(e:follow)->(v2) \
  RETURN v;
  ```

  推荐：

  ```ngql
  MATCH (v:player)-(:follow)->() \
  RETURN v;
  ```

3. 将非匿名点放在匿名点的前面。

  不推荐：

  ```ngql
  MATCH ()-(:follow)->(v) \
  RETURN v;
  ```

  推荐：

  ```ngql
  MATCH (v)<-(:follow)-() \
  RETURN v;
  ```

## 字符串

字符串用双引号包围。

  不推荐：

  ```ngql
  RETURN 'Hello Nebula!';
  ```

  推荐：

  ```ngql
  RETURN "Hello Nebula!\"123\"";
  ```

!!! note

    字符串中需要嵌套单引号或双引号时，用反斜线（\）转义。例如:

    ```ngql
    RETURN "\"Nebula Graph is amazing,\" the user says.";
    ```

<!--## 空格 TODO-->

## 结束语句

1. 用英文分号（;）结束nGQL语句。

  不推荐：

  ```ngql
  FETCH PROP ON player "player100"
  ```

  推荐：

  ```ngql
  FETCH PROP ON player "player100";
  ```

2. 使用管道符（|）分隔的复合语句，仅在最后一行末用英文分号结尾。在管道符前使用英文分号会导致语句执行失败。

  不支持：

  ```ngql
  GO FROM "player100" \
  OVER follow \
  YIELD follow._dst AS id; | \
  GO FROM $-.id \
  OVER serve \
  YIELD $$.team.name AS Team, $^.player.name AS Player;
  ```

  支持：

  ```ngql
  GO FROM "player100" \
  OVER follow \
  YIELD follow._dst AS id | \
  GO FROM $-.id \
  OVER serve \
  YIELD $$.team.name AS Team, $^.player.name AS Player;
  ```

3. 在包含自定义变量的复合语句中，用英文分号结束定义变量的语句。不按规则加分号或使用管道符结束该语句会导致执行失败。

  不支持：

  ```ngql
  $var = GO FROM "player100" \
  OVER follow \
  YIELD follow._dst AS id \
  GO FROM $var.id \
  OVER serve \
  YIELD $$.team.name AS Team, $^.player.name AS Player;
  ```

  也不支持：

  ```ngql
  $var = GO FROM "player100" \
  OVER follow \
  YIELD follow._dst AS id | \
  GO FROM $var.id \
  OVER serve \
  YIELD $$.team.name AS Team, $^.player.name AS Player;
  ```

  支持：

  ```ngql
  $var = GO FROM "player100" \
  OVER follow \
  YIELD follow._dst AS id; \
  GO FROM $var.id \
  OVER serve \
  YIELD $$.team.name AS Team, $^.player.name AS Player;
  ```
