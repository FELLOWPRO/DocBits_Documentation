# Prefect 本地设置要求

#### 要求

确保主机系统已安装以下组件：

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### 主机操作系统兼容性

* **Linux**：推荐使用，并且得到全面支持。
* **Windows**：可通过 Docker Desktop（WSL2）运行。卷挂载可能会导致问题。
* **macOS**：通过 Docker Desktop 支持，行为与 Windows 类似。

#### 系统要求

* **内存**：每个容器需要 1–2 GB。运行多个流时需要 2–4 GB。
* **CPU**：每个容器需要 1–2 个核心。并发运行流时需要 2–4 个核心。
* **磁盘**：镜像和日志需要 2–3 GB&#x20。
