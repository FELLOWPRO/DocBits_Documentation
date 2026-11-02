---
description: 使用本地扫描仪和 Doc Scan 在 DocBits 中创建文档。
---

# Doc Scan

## 下载并安装扫描软件

在 DocBits 仪表板上点击 Scan Document。

<figure><img src="../../../../.gitbook/assets/doc_scan_dashboard_button.png" alt="DocBits 仪表板上的 Scan Document 按钮"><figcaption></figcaption></figure>

如果尚未安装本地扫描软件，DocBits 会显示下载提示。请选择适合您操作系统的下载项。

<figure><img src="../../../../.gitbook/assets/doc_scan_download_prompt.png" alt="下载本地扫描软件的提示"><figcaption></figcaption></figure>

打开下载的安装文件。图中的安装程序适用于 macOS；请遵循您所用操作系统的安装说明。

<figure><img src="../../../../.gitbook/assets/doc_scan_installer_start.png" alt="扫描软件安装程序启动画面"><figcaption></figcaption></figure>

在图示安装程序中，点击 Continue，使用 Agree 接受软件许可，然后继续。检查安装位置和所需空间，再点击 Install。图中显示的 33.6 MB 仅适用于该安装程序版本；所需空间可能随版本变化。

安装完成后，关闭安装程序。

<figure><img src="../../../../.gitbook/assets/doc_scan_installation_complete.png" alt="扫描软件安装完成画面"><figcaption></figcaption></figure>

在浏览器中打开 https://local.polydocs.io:12500/ ，测试本地服务。如果浏览器无法访问该服务，并且您使用 FRITZ!Box，请检查下文所述的 DNS 重绑定保护设置。

<figure><img src="../../../../.gitbook/assets/doc_scan_browser_test_error.png" alt="测试本地扫描服务时的浏览器错误"><figcaption></figcaption></figure>

本地服务页面出现后，点击 DocBits 以打开 DocBits。

<figure><img src="../../../../.gitbook/assets/doc_scan_browser_test_success.png" alt="连接成功后的本地扫描服务页面"><figcaption></figcaption></figure>

在 DocBits 登录页面输入凭据，进入仪表板。

<figure><img src="../../../../.gitbook/assets/doc_scan_login_redirect.png" alt="从本地服务打开的 DocBits 登录页面"><figcaption></figcaption></figure>

在设置的模块部分启用 Doc Scan。

<figure><img src="../../../../.gitbook/assets/site-extra-modules-document-integration-zh.png" alt="中文文档集成模块：脚本、扫描、条码及自定义主数据等选项；Select 仍为英文。未改动任何开关。"><figcaption><p>中文文档集成模块：脚本、扫描、条码及自定义主数据等选项；Select 仍为英文。未改动任何开关。</p></figcaption></figure>

## FRITZ!Box 网络设置

如果 FRITZ!Box 阻止了指向私有地址的 DNS 响应，导致 https://local.polydocs.io:12500/ 无法访问，浏览器可能报告 DNS 超时。FRITZ!Box 使用此机制防止 DNS 重绑定。请为该本地服务添加主机名例外：

1. 在 FRITZ!Box 的德语界面中，打开 Heimnetz（家庭网络），然后打开 Netzwerk（网络）。
2. 打开 Netzwerkeinstellungen（网络设置）选项卡。
3. 在 DNS-Rebind-Schutz（DNS 重绑定保护）下，将 local.polydocs.io 添加到主机名例外中。
4. 点击 Übernehmen（应用），然后重新测试本地服务。

## 卸载 Doc2Scan Service Manager

要在 macOS 上卸载 Doc2Scan Manager，请运行：

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## 扫描仪兼容性

sane-airscan 是一个 SANE 后端，支持 Apple AirScan/eSCL 和 Microsoft WSD（WS-Scan，Web Services for Devices）。这些都是网络扫描协议。

请查看[持续维护的 sane-airscan 兼容性信息](https://github.com/alexpevzner/sane-airscan)，了解已报告的设备和协议支持情况。协议可用或 sane-airscan 的兼容性报告并不保证设备的所有功能都能在 Doc Scan 中使用。请使用所需的 Doc Scan 工作流程测试您的扫描仪。
