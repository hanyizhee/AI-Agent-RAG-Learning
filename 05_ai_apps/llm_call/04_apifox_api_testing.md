# Json格式

JSON(JavaScript Object Notation)是前端的一种对象表示方法。表示形式类似于Python中的字典,都是
key:value这种形式,不过所有的key都必须使用双引号引起来,值可以是任何类型:

> - 对象:用{}表示,{}之间是键值对形式,键是字符串,值可以是任意其它类型

> - 数字:整数和小数都是数字,例如:12、3.14

> - 字符串:用""引起来,例如:"jack"

> - 布尔:有两种值:true或false

> - 列表: 用[]表示,[]中是列表的元素,多个元素以,分割。

```json
{
  "model": "deepseek-chat",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "Hello!" }
  ],
  "stream": false
}
```
