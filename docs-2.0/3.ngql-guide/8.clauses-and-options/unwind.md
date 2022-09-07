# UNWIND

`UNWIND`语句可以将列表拆分为单独的行，列表中的每个元素为一行。

`UNWIND`可以作为单独语句或语句中的子句使用。

## UNWIND 语句

### 语法

```ngql 
UNWIND <list> AS <alias> <RETURN clause>;
```

### 示例

- 拆分列表。

  ```ngql
  nebula> UNWIND [1,2,3] AS n RETURN n;
  +---+
  | n |
  +---+
  | 1 |
  | 2 |
  | 3 |
  +---+
  ```

## UNWIND 子句

### 语法

- 原生 nGQL 语句中使用`UNWIND`子句。

  !!! note

        在原生 nGQL 语句中使用`UNWIND`子句时，需要用在管道符`|`之后，并使用`$-`引用管道符之前的变量。如果`UNWIND`后使用语句或子句，需要使用管道符`|`并且使用`$-`引用管道符之前的变量。

  ```ngql
  <statement> | UNWIND $-.<var> AS <alias> <|> <clause>;
  ```


- openCypher 语句中使用`UNWIND`子句。

  ```
  <statement> UNWIND <list> AS <alias> <RETURN clause>；
  ```


### 示例

- 在`UNWIND`子句中使用`WITH DISTINCT`可以将列表中的重复项忽略，返回去重后的结果。

  !!! note
      
      原生 nGQL 语句不支持`WITH DISTINCT`。  

  ```ngql
  // 拆分列表`[1,1,2,2,3,3]`，删除重复行，排序行，将行转换为列表。
  nebula> WITH [1,1,2,2,3,3] AS n \
          UNWIND n AS r \
          WITH DISTINCT r AS r \
          ORDER BY r \
          RETURN collect(r);
  +------------+
  | collect(r) |
  +------------+
  | [1, 2, 3]  |
  +------------+
  ```

- `MATCH`语句中使用`UNWIND`。

  ```ngql
  // 将匹配路径上的顶点输出到列表中，拆分列表，删除重复行，将行转换为列表。
  nebula> MATCH p=(v:player{name:"Tim Duncan"})--(v2) \
          WITH nodes(p) AS n \
          UNWIND n AS r \
          WITH DISTINCT r AS r \
          RETURN collect(r);
  +----------------------------------------------------------------------------------------------------------------------+
  | collect(r)                                                                                                           |
  +----------------------------------------------------------------------------------------------------------------------+
  | [("player100" :player{age: 42, name: "Tim Duncan"}), ("player101" :player{age: 36, name: "Tony Parker"}),            |
  |("team204" :team{name: "Spurs"}), ("player102" :player{age: 33, name: "LaMarcus Aldridge"}),                          |
  |("player125" :player{age: 41, name: "Manu Ginobili"}), ("player104" :player{age: 32, name: "Marco Belinelli"}),       |
  |("player144" :player{age: 47, name: "Shaquile O'Neal"}), ("player105" :player{age: 31, name: "Danny Green"}),         |
  |("player113" :player{age: 29, name: "Dejounte Murray"}), ("player107" :player{age: 32, name: "Aron Baynes"}),         |
  |("player109" :player{age: 34, name: "Tiago Splitter"}), ("player108" :player{age: 36, name: "Boris Diaw"})]           |  
  +----------------------------------------------------------------------------------------------------------------------+
  ```

- `GO`语句中使用`UNWIND`。

  ```ngql 
  // 在点列表中查询点关联的边。
  nebula> YIELD ['player101', 'player100'] AS a | UNWIND $-.a AS  b | GO FROM $-.b OVER follow YIELD edge AS e;
  +----------------------------------------------------+
  | e                                                  |
  +----------------------------------------------------+
  | [:follow "player101"->"player100" @0 {degree: 95}] |
  | [:follow "player101"->"player102" @0 {degree: 90}] |
  | [:follow "player101"->"player125" @0 {degree: 95}] |
  | [:follow "player100"->"player101" @0 {degree: 95}] |
  | [:follow "player100"->"player125" @0 {degree: 95}] |
  +----------------------------------------------------+
  ```

- `LOOKUP`语句中使用`UNWIND`。

  ```ngql
  // 查询年龄大于 46 岁球员的所有属性，去掉重复属性，并将结果转换为行。
  nebula> LOOKUP ON player \
          WHERE player.age > 46 \
          YIELD DISTINCT keys(vertex) as p | UNWIND $-.p as a | YIELD $-.a AS a;
  +--------+
  | a      |
  +--------+
  | "age"  |
  | "name" |
  +--------+
  ```

- `FETCH`语句中使用`UNWIND`。

  ```ngql
  // 查询 player101 点的所有 Tag，并将结果转换为行。
  nebula> CREATE TAG hero(like string, height int);
          INSERT VERTEX hero(like, height) VALUES "player101":("deep", 182);
          FETCH PROP ON * "player101" \
          YIELD tags(vertex) as t | UNWIND $-.t as a | YIELD $-.a AS a;
  +----------+
  | a        |
  +----------+
  | "hero"   |
  | "player" |
  +----------+
  ```
  
- `GET SUBGRAPH`语句中使用`UNWIND`。

  ```ngql
  // 查询从点 player100 开始、0~2 跳、serve 类型的出边和入边的子图，并将结果转换为行。
  nebula> GET SUBGRAPH 2 STEPS FROM "player100" BOTH serve \
          YIELD edges as e | UNWIND $-.e as a | YIELD $-.a AS a;
  +----------------------------------------------+
  | a                                            |
  +----------------------------------------------+
  | [:serve "player100"->"team204" @0 {}]        |
  | [:serve "player101"->"team204" @0 {}]        |
  | [:serve "player102"->"team204" @0 {}]        |
  | [:serve "player103"->"team204" @0 {}]        |
  | [:serve "player105"->"team204" @0 {}]        |
  | [:serve "player106"->"team204" @0 {}]        |
  | [:serve "player107"->"team204" @0 {}]        |
  | [:serve "player108"->"team204" @0 {}]        |
  | [:serve "player109"->"team204" @0 {}]        |
  | [:serve "player110"->"team204" @0 {}]        |
  | [:serve "player111"->"team204" @0 {}]        |
  | [:serve "player112"->"team204" @0 {}]        |
  | [:serve "player113"->"team204" @0 {}]        |
  | [:serve "player114"->"team204" @0 {}]        |
  | [:serve "player125"->"team204" @0 {}]        |
  | [:serve "player138"->"team204" @0 {}]        |
  | [:serve "player104"->"team204" @20132015 {}] |
  | [:serve "player104"->"team204" @20182019 {}] |
  +----------------------------------------------+
  ```

- `FIND PATH`语句中使用`UNWIND`。

  ```ngql
  // 找出 player101 到 team204 延 serve 类型边的最短路径上的所有点，并将结果转换为行。
  nebula> FIND SHORTEST PATH FROM "player101" TO "team204" OVER serve \
          YIELD path as p | YIELD nodes($-.p) AS nodes | UNWIND $-.nodes AS a | YIELD $-.a AS a;
  +---------------+
  | a             |
  +---------------+
  | ("player101") |
  | ("team204")   |
  +---------------+
  ```










