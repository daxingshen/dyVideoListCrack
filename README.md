# dolphin
方法一：
  版本：python3
  单个测试文件，注意替换html文件的路径和相应版本的chrome driver
  
  > python app.py
  ![image](https://github.com/daxingshen/imgines/raw/master/444.png)

  
方法二：使用thriftpy服务话
linux平台,需安装chrome

运行 

- 服务端
> cd dyVideoListCrack/dolphin/service/douyin  

> PYTHONPATH=$PYTHONPATH:./../../../ python kolserver.py  


## 这是我的地址：47.89.246.154:6000
调用方法：参考测试程序，
传入参数：用户uid
返回值：该用户的所有作品
## 备注： 本样例提供的是rpc接口，不是http

- 测试客户端
> cd dyVideoListCrack/test  

> PYTHONPATH=$PYTHONPATH:../ python main.py  

![image](https://github.com/daxingshen/imgines/raw/master/WX20180912-223024.png)
