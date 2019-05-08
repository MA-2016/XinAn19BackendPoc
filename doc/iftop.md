
# iftop

网络流量监控工具

## 安装

http://www.vpser.net/manage/iftop.html

## 集成方案

* 是iftop以非交互方式运行: ```iftop -t -i wlp3s0```
* flume使用Exec数据源, reference: http://flume.apache.org/releases/content/1.9.0/FlumeUserGuide.html. ```Warning The problem with ExecSource and other asynchronous sources is that the source can not guarantee that if there is a failure to put the event into the Channel the client knows about it. In such cases, the data will be lost. As a for instance, one of the most commonly requested features is the tail -F [file]-like use case where an application writes to a log file on disk and Flume tails the file, sending each line as an event. While this is possible, there’s an obvious problem; what happens if the channel fills up and Flume can’t send an event? Flume has no way of indicating to the application writing the log file that it needs to retain the log or that the event hasn’t been sent, for some reason. If this doesn’t make sense, you need only know this: Your application can never guarantee data has been received when using a unidirectional asynchronous interface such as ExecSource! As an extension of this warning - and to be completely clear - there is absolutely zero guarantee of event delivery when using this source. For stronger reliability guarantees, consider the Spooling Directory Source, Taildir Source or direct integration with Flume via the SDK.```