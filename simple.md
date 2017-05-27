MAT: 1A
HOST: http://cs-api.vmceshi.com

### 公用存储接口api

本接口用于简单数据存储，支持key-value简单数据存储和修改

# Group 相关说明
::: note
# 参数说明
文档中所有接口参数，除必填参数外，其他参数可自定义，参数命名需遵循以下规则：
  
- 字符限制 字母 ，数字 , ：
- 关键字限制（保留字符，不能在参数中使用）：system,sys,admin,mgvmobel,yizhi,yanshi,js
- 长度限制为4～30个

其他说明：
- 字符编码为utf-8；
- 文档中Request下body中的内容仅作参考，均为非必填参数;
:::


# Group 接口 

# 接口列表 [/commonapi/storage/{catalog}/{?key,param}] 
## 保存数据 [POST]

根据key和value保存数据内容

+ Request (application/json)
      参数说明：
      + 参数中catalog和key为必填;
      + 除必填参数外，必须至少有一个自定义参数;
  
    + Headers

    + Body 

            {
                "catalog": "kmelearning:introduction",
                "key":"hong"，
                "introduction":"一句话介绍自己"，
                “score”:300,
                "rank":"1"，
                "join-time":"2017-03-20"
            }

+ Response 200 (application/json)
   
    + Headers

    + Body
                
            {
              "resp":""
            }


## 查询数据  [GET]

+ Parameters

    + catalog: kmelearning:introduction (required) - 保存信息分类，和key一起用于标示信息存放位置，可用于联合信息检索。
    + key: hong   (required) 
    + param: introduction (optional)） 支持多个参数可选
      

+ Response 200 (application/json)

    + Headers

    + Body

            {
                "resp":{
                        "record":"记录条数",
                        "list":
                       [{
                            “catalog”:"",
                            "key":"",
                            "introduction":"一句话"
                            “score”:300,
                            "rank":"1"
                            "join-time":"2016-03-20"        
                        },{
                            “catalog”:"",
                            "key":"",
                            "introduction":"一句话"
                            “score”:300,
                            "rank":"1"
                            "join-time":"2016-03-20"        
                        }]
                }
            }


## 更新数据 [PUT]
修改内容，该接口修改的内容不限参数个数。
+ Parameters
    + catalog: kmelearning:introduction (required) - 保存信息分类，和key一起用于标示信息存放位置，可用于联合使用用于信息检索。
    + key: hong   (required) 
   

+ Request (application/json)
    参数说明：
    + 需一个以上自定义参数；

    + Body

            {
                "introduction":"一句话介绍自己"
                “score”:300,
                "rank":"1"
                "join-time":"2017-03-20"
            }



+ Response 200 (application/json)

    + Body         

            {
                "resp":
                {"num": "成功保存记录条数"}
            }

