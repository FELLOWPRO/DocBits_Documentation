# DocBits Infor 本地部署客户

向 Infor 本地部署客户发送数据有两种方式：使用 IPsec 建立站点到站点连接，或使用 [WatchDog](../../administration-and-setup/setup/watchdog/README.md)。

向 Infor 本地部署客户发送数据

向 Infor 本地部署客户发送数据有两种方式：使用 IPsec 建立站点到站点 VPN。

## IPsec（互联网协议安全）站点到站点 VPN 配置

### 1. 配置信息：

| **IPSEC VPN 设置**            |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **端点 B**                                                  |
| **客户**                   | _**FELLOWPRO AG**_                                              |
| **联系人姓名**            | _**Daniel Lopez**_                                              |
| **邮箱**                       | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **端点硬件/软件** | _**StrongWAN**_                                                 |
| **防火墙位置**       | _**法兰克福**_                                                 |
| **端点 IP**                | _**46.101.133.158**_                                            |
| **网络/主机 1**             | _**10.135.0.0/16**_                                             |

### 2. 对于 IPsec 站点到站点 VPN，您需要配置并开放以下端口：

1\. UDP 端口 500：用于互联网密钥交换（IKE）第 1 阶段和第 2 阶段。

2\. UDP 端口 4500：用于 NAT 穿越（NAT-T），允许 VPN 流量通过 NAT（网络地址转换）设备。

## 访问 Infor OS

• 身份验证 URL：https://inforos.CustomerXYZad.net/

• 数据 URL：https://inforos.CustomerXYZad.net:7443/

## 摘要：

设置 IPsec 站点到站点 VPN 时，请确保已配置并开放上述端口和协议。

使用提供的 URL 访问 Infor OS，以进行身份验证和数据访问。
