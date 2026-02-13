from ddgs import DDGS

try:
    with DDGS() as ddgs:
        print('=== Insta360 Ace Pro 2 存储规格 ===\n')
        results = list(ddgs.text('Insta360 Ace Pro 2 storage microSD card slot internal', max_results=5))
        for r in results:
            title = r['title']
            print(f'- {title}')
except Exception as e:
    print(f'Error: {e}')
