import requests

def access_baidu_via_proxy():
    """
    通过代理服务器访问 baidu.com
    """
    print("=== 代理访问百度测试 ===\n")
    
    # 1. 获取用户输入的代理信息
    proxy_host = input("请输入代理服务器地址 (例如: 10.10.1.10): ").strip()
    proxy_port = input("请输入代理端口号 (例如: 8080): ").strip()
    
    # 构建代理配置字典[citation:3][citation:10]
    proxy_url = f"http://{proxy_host}:{proxy_port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    
    print(f"\n使用代理: {proxy_url}")
    print("正在尝试访问 baidu.com...\n")
    
    # 2. 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    # 3. 通过代理发送请求[citation:7]
    try:
        response = requests.get(
            "https://www.baidu.com",
            proxies=proxies,
            headers=headers,
            timeout=10  # 设置超时时间[citation:3]
        )
        
        # 检查请求是否成功
        response.raise_for_status()
        
        # 从HTML中提取页面标题
        title_start = response.text.find('<title>')
        title_end = response.text.find('</title>')
        
        if title_start != -1 and title_end != -1:
            page_title = response.text[title_start+7:title_end]
            print(f"✅ 访问成功！")
            print(f"页面标题: {page_title}")
            print(f"状态码: {response.status_code}")
            print(f"响应大小: {len(response.text)} 字节")
        else:
            print("✅ 连接成功，但未能解析到页面标题。")
            print(f"状态码: {response.status_code}")
            
    except requests.exceptions.ProxyError as e:
        print(f"❌ 代理连接失败: {e}")
        print("请检查代理地址和端口是否正确，以及代理服务器是否可用。")
    except requests.exceptions.ConnectTimeout:
        print("❌ 连接超时：代理服务器响应时间过长。")
    except requests.exceptions.ConnectionError:
        print("❌ 网络连接错误：无法连接到代理服务器或目标网站。")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

if __name__ == "__main__":
    access_baidu_via_proxy()