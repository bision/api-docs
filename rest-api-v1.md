## 接入说明

### REST API

``
https://api.bision.com
``

鉴于延迟高和稳定性差等原因，不建议通过代理的方式访问Bision API。

请求头信息请设置为：`Content-Type=application/x-www-form-urlencoded`

<br/>

### 限频规则

获取资产每秒3次，其他方法单个用户每秒10次，单个IP每分钟1000次，超出锁定账户10分钟。

<br/>

### 签名说明


使用API请求在通过 internet 传输的过程中极有可能被篡改，为了确保请求未被更改，除公共接口（基础信息，行情数据）外的私有接口均必须使用您的 API Key 做签名认证，以校验参数或参数值在传输途中是否发生了更改。每一个API Key需要有适当的权限才能访问相应的接口。每个新创建的API Key都需要分配权限。权限类型分为：读取，交易，提币。在使用接口前，请查看每个接口的权限类型，并确认你的API Key有相应的权限。


一个合法的请求由以下几部分组成：

方法请求地址：即访问服务器地址 `api.bision.com`，比如 `api.bision.com/trade/api/v1/order`。

API 访问密钥（accesskey）：您申请的 API Key 中的 Access Key。

时间戳（nonce）：您应用程序发出请求的时间戳，13位毫秒数，Bision将根据这个时间戳检验您API请求的有效性。

签名(signature)：签名计算得出的值，用于确保签名有效和未被篡改，Bision使用 HmacSHA256。

<br/>

### 签名步骤

规范要计算签名的请求 因为使用 HMAC 进行签名计算时，使用不同内容计算得到的结果会完全不同。所以在进行签名计算前，请先对请求进行规范化处理。下面以查询某订单详情请求为例进行说明：


`https://api.bision.com/trade/api/v1/getOrder?accesskey={AccessKey}&market={Market}&none={Timestamp}&id={OrderId}&signature={Signature}`

按照ASCII码的顺序对参数名进行排序,将各参数使用字符 “&” 连接，例如下面就是排序之后结果：

`accesskey=myAccessKey&id=123&market=btc_usdt&nonce=1562919832183`

需要注意的是none的值为13位毫秒数时间戳

使用网站申请得到的SecretKey对上面生成的参数串进行 HmacSHA256 签名。例如上述参数进行签名的结果：

`97b7b71741ca0aec6e0404a5b1c7cb2a78e7bd6c2a8088dbd84a20129dee4fe7`

最后把签名赋值到参数名signature并提交到服务器。

<br/>

### 返回格式

所有的接口返回都是JSON格式。交易 API 返回信息均包含Code与Message两个信息。


<br/>


### 行情数量

**K线数据**

``
    GET /data/api/v1/getKLine
``

>请求参数

参数 | 数据类型 | 是否必须 | 默认值 | 描述 | 取值范围  
-|-|-|-|-|-
market | string | true | N/A | 交易市场 | btc_usdt, eth_usdt...
type | string | true | N/A | K线类型 | 1min,5min,15min,30min,1hour,6hour,1day,7day,30day,365day
since | integer | true | 0 | 时间条件，控制增量 | 第一次为0,之后为响应的since的值即可

>响应数据
```js
// [时间戳，开盘价，最高价，最低价，收盘价，成交量，成交额]
{
  "datas": [
    [
      1562923200,
      11634.64,  
      11637.22,
      11627.58,
      11631.43,
      1.144578,
      13314.16264138
    ]
  ],
  "since": 1562923200
}
```

<br/>

**聚合行情（Ticker）**

``
    GET /data/api/v1/getTicker
``

>请求参数

参数 | 数据类型 | 是否必须 | 默认值 | 描述 | 取值范围  
-|-|-|-|-|-
market | string | true | N/A | 交易市场 | btc_usdt, eth_usdt...

>响应数据
```js
{
  "high": 11776.93,
  "moneyVol": 33765013.61761934,    //成交额
  "rate": 1.3900,                   //24涨跌幅
  "low": 11012.17,
  "price": 11609.92,
  "ask": 11618.25,
  "bid": 11604.08,
  "coinVol": 2944.208780            //成交量
}
```

<br/>

**所有交易对的最新 Tickers**

``
    GET /data/api/v1/getTickers
``

>请求参数

>None

>响应数据
```js
{
  "ltc_usdt": {
    "high": 106.99,
    "moneyVol": 1589953.528784,
    "rate": 4.3400,
    "low": 97.51,
    "price": 105.52,
    "ask": 105.61,
    "bid": 105.46,
    "coinVol": 15507.7052
  },
  "btc_usdt": {
    "high": 11776.93,
    "moneyVol": 33765013.61761934,
    "rate": 1.3900,                 
    "low": 11012.17,
    "price": 11609.92,
    "ask": 11618.25,
    "bid": 11604.08,
    "coinVol": 2944.208780
  }
}
```

<br/>

**市场深度数据**

``
    GET /data/api/v1/getDepth
``

>请求参数

参数 | 数据类型 | 是否必须 | 默认值 | 描述 | 取值范围  
-|-|-|-|-|-
market | string | true | N/A | 交易市场 | btc_usdt, eth_usdt...

>响应数据
```js
{
  "last": 11591.26,     //最新成交价
  "asks": [
    [
      11594.80,
      0.049472
    ],
    [
      11594.86,
      0.048462
    ]
  ],
  "bids": [
       [
         11590.06,
         0.188749
       ],
       [
         11588.42,
         0.030403
       ]
   ]
}
```

<br/>

**最近市场成交记录**

``
    GET /data/api/v1/getTrades
``

>请求参数

参数 | 数据类型 | 是否必须 | 默认值 | 描述 | 取值范围  
-|-|-|-|-|-
market | string | true | N/A | 交易市场 | btc_usdt, eth_usdt...

>响应数据
```js
// [时间戳，成交价，成交数量，交易类型，记录ID]
[
  [
    1562924059762,
    11613.18,
    0.044448,
    "bid",
    156292405956105
  ],
  [
    1562924059006,
    11613.22,
    0.000086,
    "bid",
    156292405956104
  ]
]
```
