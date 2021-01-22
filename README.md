让我们尽情的享受田园生活吧


#### 目的
* 做一个运维平台的样例


#### 说在前面
> 如果觉得有用，请点个Star(这就是俺的动力, 一个Star我能开心一天)  

> 项目中所有资产都是使用阿里云，但是如果要接入其它平台，只要平台提供了接口很容易接入.  

> 阅读时，请根据指定的tag号，切换到对应代码版本查看.  
> 可以使用git diff 0.0.3 0.0.4来查看不同版本之间的改动.  
> 当前也可以先看看哪些文件改动了不看具体更改内容: git diff 0.0.1 0.0.5 --stat  
> 也可以使用git diff 0.0.1 0.0.5 (文件名)来具体某一文件的改动内容.  
> 使用python版本: 3.8.5  
> 这绝不是零基础教程  

[一些有关使用Django的教程](https://github.com/bxxfighting/big-talk-django)  

[后端代码库](https://github.com/bxxfighting/rurality)  
[前端代码库](https://github.com/bxxfighting/enjoy)  

#### 体验及提示

* 请不要将自己实际账号等重要信息填写到体验系统中，如果因此造成损失开发者不承担责任  
* 体验地址主要是体验整个控制界面及流程，如果要实际操作，可以本地部署测试  

> [体验地址](http://39.105.71.60)  
> 体验系统管理账号: admin/123456 (超级管理员)  
> 体验业务操作账号: buxingxing/123456 (管理员)  

> 友情提示: 最好使用右击新标签页打开以下链接  

#### 安装文档
[安装文档](https://github.com/bxxfighting/rurality/blob/master/INSTALL.md)  

<details>
<summary>第一章 美好生活的开启</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/1.md">第一节 开启美好生活</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/2.md">第二节 增加常用的工具方法</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/3.md">第三节 增加基础错误及基础类型校验</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/4.md">第四节 根据自己的需求删减django中间件及apps</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/5.md">第五节 定制自己的基础model</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/6.md">第六节 定制自己的基础api</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/7.md">第七节 增加依赖管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/8.md">第八节 定义用户model</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/9.md">第九节 角色与部门</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/10.md">第十节 模块与权限</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/11.md">第十一节 基础操作model对象方法</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/12.md">第十二节 配置数据库</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/13.md">第十三节 跨域配置</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/14.md">第十四节 创建超级管理员账号</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/15.md">第十五节 运行服务(gunicorn)</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/1/16.md">第十六节 第一个接口：登录</a>
</code></pre>
</details>

<details>
<summary>第二章 努力的积淀</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/enjoy/blob/master/how/to/do/1.md">第一节 开辟新战场</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/1.md">第二节 模块基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/2.md">第三节 权限基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/3.md">第四节 部门基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/4.md">第五节 角色基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/5.md">第六节 用户基础接口</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/6.md">第七节 接口并发请求锁</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/7.md">第八节 完善所有接口的并发处理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/2/8.md">第九节 用户\角色\模块\部门\权限关联关系接口</a>
</code></pre>
</details>
<details>
<summary>第三章 画画的北北</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/1.md">第一节 前后开工</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/2.md">第二节 写一个mod模块玩玩</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/3.md">第三节 是时候展示复制粘贴的魅力了</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/4.md">第四节 继续感受复制粘贴的强大</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/5.md">第五节 无规矩不成方圆</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/3/6.md">第六节 整点实际的</a>
</code></pre>
</details>
<details>
<summary>第四章 完善基础支撑功能</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/1.md">第一节 啥系统都得有任务</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/2.md">第二节 总得有日志吧?</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/4/3.md">第三节 防背锅手册</a>
</code></pre>
</details>
<details>
<summary>第五章 拥抱阿里云</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/1.md">第一节 开启阿里云的钥匙</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/2.md">第二节 阿里云资产模块管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/3.md">第三节 阿里云地域、可用区管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/4.md">第四节 环境管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/5.md">第五节 先玩玩阿里云ECS</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/6.md">第六节 服务配置需要用到的资产模块</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/7.md">第七节 服务与ECS有个约会</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/8.md">第八节 干SLB</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/9.md">第九节 服务关联SLB服务器组</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/10.md">第十节 干RDS</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/11.md">第十一节 服务关联数据库</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/12.md">第十二节 干Redis</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/13.md">第十三节 干Mongo</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/14.md">第十四节 域名也得管理上</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/15.md">第十五节 MQ中选一个写写(RocketMQ)</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/5/16.md">第十六节 便捷万岁</a>
</code></pre>
</details>
<details>
<summary>第六章 来点正经的</summary>
<pre><code>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/1.md">第一节 统一任务管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/2.md">第二节 引用代码库管理</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/3.md">第三节 服务增加编程语言、框架、代码库属性</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/4.md">第四节 服务基础部署配置</a>
<a target="_blank" href="https://github.com/bxxfighting/rurality/blob/master/how/to/do/6/5.md">第五节 Jenkins管理</a>
</code></pre>
</details>

哈哈，支付宝收款码在此，一分不嫌少，一元不嫌多，就是图一个乐子  
<img src="https://github.com/bxxfighting/rurality/blob/master/data/sponsor/images/支付宝收款码.jpeg" width="300" hegiht="300" />
[赞助名单](https://github.com/bxxfighting/rurality/blob/master/data/sponsor/README.md)

<details>
<summary>Todo List</summary>
<pre><code>
<ol>
<li>接入阿里云Redis/RDS/Mongo/Kafka/Rocketmq管理</li>
<li>服务关联jenkins进行部署，采用pipeline加ansible的方式</li>
<li>实现阿里云资源的购买释放以及与服务相关功能进行联动</li>
<li>购买等行为增加审批</li>
<li>统一的任务管理</li>
<li>操作审批</li>
</ol>
</code></pre>
</details>

#### 免责声明
* 本项目属于教学及体验设计，如果在生产环境使用，请进行充分测试与评估，出现任何问题作者不承担任何责任
