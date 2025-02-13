import os
import requests
from urllib.parse import urlparse

# 详情参考：http://translationproject.org/domain/gcc.html


# 定义下载参数（对于CN版本）
# URL = "http://translationproject.org/PO-files/zh_CN/gcc-14.2.0.zh_CN.po"
URL = "https://translationproject.org/POT-files/gcc-14.2.0.pot"
FILENAME = os.path.basename(urlparse(URL).path)

# 执行下载
print("正在下载翻译文件...")

try:
    response = requests.get(URL, stream=True)
    response.raise_for_status()  # 如果状态码不是200，引发HTTPError异常

    total_size = int(response.headers.get('content-length', 0))
    downloaded_size = 0

    with open(FILENAME, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):  # 使用8KB的块
            if chunk:  # 过滤掉keep-alive新块
                f.write(chunk)
                downloaded_size += len(chunk)
                if total_size > 0:  # 只有当content-length存在时才显示进度
                    progress = (downloaded_size / total_size) * 100
                    print(f"\r下载进度: {progress:.2f}%", end="", flush=True)
    print() # Newline after progress bar

    # 结果检查 (简化 - requests库已经处理了大多数错误)
    if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
        print(f"✅ 下载完成，保存为：{FILENAME}")
    else:
         print(f"❌ 下载失败，文件 {FILENAME} 不存在或为空。")
         print("请检查：")
         print("1. 网络连接是否正常")
         print(f"2. 目标地址是否有效：{URL}")
         exit(1)


except requests.exceptions.RequestException as e:
    print(f"❌ 下载失败，发生网络错误：{e}")
    print("请检查：")
    print("1. 网络连接是否正常")
    print(f"2. 目标地址是否有效：{URL}")
    exit(1)
except Exception as e:
    print(f"❌ 下载失败，发生未知错误：{e}")
    exit(1)

