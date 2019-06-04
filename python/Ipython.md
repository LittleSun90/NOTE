# IPython（Interactive Python）
  
  
### 帮助命令
  
command | description
--- | ---
?  | IPython帮助文档
%quickref | 快速参考
help() | Python内建函数help
object? | 有关object对象的详细信息(文档字符串,<br>函数定义和类的构造函数等信息)
object?? | 比object?更多的信息
  
### Tab代码提示和自动补全
  
  
### 魔法方法概述
  
command | description
--- | --- 
%magic | Line magics 只对当前行代码有效<br>当前命名空间未定义对应标识符，可不添加<br>%前缀调用magics，可使用%automagic切换
%%magic | Cell magics 置于单元开始，<br>magic针对整个单元有效，不能嵌套
%lsmagic | 列出所有的magic函数
  
### 常用魔法方法
  
magic_name | description | Usage
--- | --- | --- 
%alias | 别名 | %alias alias_name cmd <br> 使用%s定义带参数的别名
%rehashx | 自动为环境变量PATH的内容创建别名 |
%reload_ext | 通过其模块名称重新加载IPython扩展 |
%edit | 调用编辑器并执行生成的代码 | 默认调用环境变量EDITOR <br> 选项-x退出后不立即执行编辑后的代码
%run | 在ipython运行python文件 | 选项-t执行结束后打印计时信息
%load | 加载文件 | 选项-r指定加载的行或范围
%history | 历史记录 | %hist是别名<br>接收位置参数行号范围<br>选项-n/o/p/t/f/g/u,详细%history?
%save | 将命令保存到文件 | %save [options] filename n1-n2 n3-n4<br>选项-a追加模式
%logstart | 开启日志记录 | %logstart [options] [log_name [log_mode]]<br>配合使用logstop，logoff和logon
%sotre | 存储别名、宏等 | 重启ipyhon后需要%store -r
  
  
### 配置
  
  
#### 配置文件
  
创建空白配置文件  
ipython profile create  
默认配置文件路径  
~/.ipython/profile_default/ipython_config.py
  
#### 数据目录（文件配置、命令历史和扩展等）
  
查询命令  
ipython locate  
环境变量  
IPYTHONDIR  
  
#### 常用配置
  
  
``` Python
# 自动重载 autoreload
## lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = ['%autoreload 2', '']
  
## A list of dotted module names of IPython extensions to load.
c.InteractiveShellApp.extensions = ['autoreload']
  
# 启动后自动恢复存储的宏、变量、别名等 %store -r
## If True, any %store-d variables will be automatically restored when IPython starts.
c.StoreMagics.autorestore = True
```
  
### 其他
  
Crtl-o 强制在光标处插入新行  
!cmd  执行外部shell命令
  
