import os
import sys
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 设置环境变量
os.environ['CHATTTS_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS'
os.environ['HF_HOME'] = r'C:\Users\Laptop\.openclaw\workspace\ChatTTS\hf_cache'

sys.path.insert(0, r'C:\Users\Laptop\.openclaw\workspace')

try:
    logging.info("正在导入 ChatTTS...")
    import ChatTTS
    logging.info("✓ ChatTTS 导入成功")
    
    logging.info("创建 Chat 实例...")
    chat = ChatTTS.Chat()
    logging.info("✓ Chat 实例创建成功")
    
    logging.info("\n开始下载模型（从 Hugging Face）...")
    logging.info("这可能需要几分钟，请耐心等待...\n")
    
    # 使用内置下载功能
    success = chat.load(
        source='huggingface',
        force_redownload=False,
        compile=False
    )
    
    if success:
        logging.info("\n✓ 模型下载并加载成功！")
    else:
        logging.error("\n✗ 模型加载失败")
        sys.exit(1)
        
except Exception as e:
    logging.error(f"\n✗ 错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
