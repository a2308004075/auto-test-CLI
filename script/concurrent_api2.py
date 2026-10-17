import asyncio
import aiohttp
import time

"""
多接口并发
"""
# === 配置 ===
HOST = "https://pdd-station-supercharge-test.catles.com"
PATH1 = "/api/scheduleTask/executeHandler1"  # 替换成你的接口路径1
PATH2 = "/api/scheduleTask/executeHandler2"  # 替换成你的接口路径2
URL1 = f"{HOST}{PATH1}"
URL2 = f"{HOST}{PATH2}"

METHOD = "POST"  # GET / POST
HEADERS = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0Iiwic3ViIjoie1wiaWRcIjo0LFwidW5pb25JZFwiOm51bGwsXCJwbGF0Zm9ybVR5cGVcIjoxLFwicmVhbE5hbWVcIjpcIueuoeeQhuWRmFwiLFwiYWNjb3VudFwiOlwiR0xZXCIsXCJjbGllbnRJZFwiOm51bGwsXCJzb3VyY2VVc2VySWRcIjpudWxsLFwiYXZhdGFyXCI6bnVsbCxcInRlbmFudElkXCI6bnVsbCxcInRlbmFudEx2XCI6bnVsbCxcImRlcHRJZFwiOm51bGwsXCJyb2xlQ29kZXNcIjpudWxsLFwicm9sZUlkc1wiOm51bGwsXCJwZXJtc1wiOm51bGwsXCJtZW51c1wiOm51bGx9IiwiaWF0IjoxNzg1OTk5NTUyLCJleHAiOjE3ODYwODU5NTJ9.T_GfdaFaZ0w_R05oi39oU_HJKnYt5XJGbHqHwpDQuIk',
    'Content-Type': 'application/json'
}
# POST 时填写, 如 {"key": "value"}
BODY = {
    "executorHandler": "autoChargeStrategy"
}
CONCURRENCY = 3  # 并发数
TOTAL = 2  # 总调用次数


async def call_api(i, url):
    start = time.time()
    try:
        async with aiohttp.ClientSession() as session:
            if METHOD.upper() == "GET":
                async with session.get(url, headers=HEADERS, timeout=10) as resp:
                    elapsed = time.time() - start
                    print(f"[{i}] {resp.status} | {elapsed:.3f}s")
                    return resp.status
            else:
                async with session.post(url, headers=HEADERS, json=BODY, timeout=10) as resp:
                    elapsed = time.time() - start
                    print(f"[{i}] {resp.status} | {elapsed:.3f}s")
                    return resp.status
    except Exception as e:
        elapsed = time.time() - start
        print(f"[{i}] ERROR: {e} | {elapsed:.3f}s")
        return None


async def main():
    # 创建任务列表
    tasks = []
    for i in range(TOTAL):
        if i % 2 == 0:
            tasks.append(call_api(i, URL1))
        else:
            tasks.append(call_api(i, URL2))

    results = await asyncio.gather(*tasks)
    ok = sum(1 for r in results if r and 200 <= r < 300)
    fail = TOTAL - ok
    print(f"\n完成: {ok} 成功, {fail} 失败, 总耗时 {time.time() - t0:.3f}s")


if __name__ == "__main__":
    t0 = time.time()
    asyncio.run(main())
