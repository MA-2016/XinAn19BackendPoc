## Security Event

Reference: http://luncert.cn:9080/StaticFileService/static-file/XinAn.modelDesign

通讯协议：TCP

* timestamp: 日期
* deviceIP: 设备ip, eg. ```192.168.18.8 [eth0]```
* eventTypeID: 事件类型ID
* eventID: 唯一事件ID, eg. ```1005502```
* type: 事件类型, eg. ```Alert```
* subType: 子类型, eg. ```HostIDS Alert```
* docSrcName: 资料来源名称, 我理解就是发出该事件的主机的主机名, eg. ```AlienVault HIDS-syslog```
* docSrcID: 资料来源ID, eg. ```7001```
* productType: 产品类型, eg. ```Operating System```
* additionalInfo: 附加信息

引出一个问题：数据采集设备管理