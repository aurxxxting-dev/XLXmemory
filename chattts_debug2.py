import os
import sys
import traceback

os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.chdir(r'C:\Users\Laptop\.openclaw\workspace')
sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    print("Step 1: 导入 ChatTTS...")
    import ChatTTS
    print("✓ ChatTTS 导入成功")
    
    print("\nStep 2: 创建 Chat 实例...")
    chat = ChatTTS.Chat()
    print("✓ Chat 实例创建成功")
    
    print("\nStep 3: 加载本地模型...")
    print(f"模型路径: C:\\Users\\Laptop\\.openclaw\\workspace\\ChatTTS")
    
    # 检查文件是否存在
    import pathlib
    p = pathlib.Path(r'C:\Users\Laptop\.openclaw\workspace\ChatTTS')
    print(f"\n目录内容:")
    for f in p.rglob('*'):
        if f.is_file():
            print(f"  {f.relative_to(p)}")
    
    success = chat.load(
        source='custom',
        custom_path=r'C:\Users\Laptop\.openclaw\workspace\ChatTTS',
        compile=False
    )
    
    if success:
        print("\n✓ 模型加载成功！")
    else:
        print("\n✗ 模型加载返回 False")
        
except Exception as e:
    print(f"\n✗ 错误: {e}")
    traceback.print_exc()
