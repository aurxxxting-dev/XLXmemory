from ddgs import DDGS

try:
    with DDGS() as ddgs:
        print('=== TF卡/存储价格趋势 2025-2026 ===\n')
        
        # 搜索1: NAND闪存价格趋势
        results = list(ddgs.text('NAND flash memory price trend 2025 2026', max_results=3))
        print('1. NAND闪存市场趋势:')
        for r in results:
            title = r['title']
            print(f'   - {title}')
        
        # 搜索2: 存储卡价格
        results = list(ddgs.text('microSD TF card price forecast 2026', max_results=3))
        print('\n2. 存储卡价格预测:')
        for r in results:
            title = r['title']
            print(f'   - {title}')
            
        # 搜索3: 国产存储影响
        results = list(ddgs.text('YMTC China NAND flash price impact 2025', max_results=3))
        print('\n3. 国产存储影响:')
        for r in results:
            title = r['title']
            print(f'   - {title}')
            
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
