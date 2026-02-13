import sys
print("Python:", sys.executable)
try:
    from duckduckgo_search import DDGS
    print("DDGS import OK")
    with DDGS() as ddgs:
        results = list(ddgs.text('GLM-5 开源 智谱', max_results=3))
        print(f"Found {len(results)} results")
        for r in results:
            print(f"- {r['title'][:50]}...")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
