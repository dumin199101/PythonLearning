import psutil
print(psutil.cpu_count()) # CPU逻辑数量
print( psutil.cpu_count(logical=False)) # CPU物理核心
print(psutil.virtual_memory()) #内存信息
print(psutil.disk_partitions()) # 磁盘分区信息
print(psutil.disk_usage('/') )# 磁盘使用情况