from ddgs import DDGS

try:
    with DDGS() as ddgs:
        results = list(ddgs.text('GLM-5 open source Zhipu AI', max_results=5))
        print(f"Found {len(results)} results:\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']}")
            print(f"   {r['href']}")
            print(f"   {r['body'][:100]}...")
            print()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
