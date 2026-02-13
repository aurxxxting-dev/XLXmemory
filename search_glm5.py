from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text('GLM-5 开源 智谱 AI 发布', max_results=5)
    for i, r in enumerate(results):
        print(f"{i+1}. {r['title']}")
        print(f"   {r['href']}")
        print(f"   {r['body'][:120]}...")
        print()
