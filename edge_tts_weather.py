import asyncio
import edge_tts

async def main():
    text = """你好aur，这里是小爪为您带来的成都天气预报。

今天是2026年2月11日，星期三。成都今天是个大晴天，当前气温5摄氏度，体感舒适。西南风微风，风速大约4公里每小时，能见度7公里，没有降雨。

今天的详细预报如下：

早上，阳光明媚，气温7摄氏度，北风轻拂1到2公里每小时，非常适合晨跑或晨练。

中午时分，气温上升到13摄氏度，阳光明媚，西北风6到7公里每小时，适合出门吃个午饭。

下午到傍晚，气温达到全天最高14摄氏度，依然是晴天，西风8到11公里每小时，是户外活动的好时机。

夜间，气温回落到11摄氏度，天气晴朗，西风6到12公里每小时，适合早点休息。

未来两天预报：

明天周四，白天晴天为主，气温10到14摄氏度。傍晚可能会有些多云，夜间晴朗，气温12摄氏度左右。

后天周五，多云为主，气温11到17摄氏度，稍微暖和一点。

总的来说，这几天成都天气都不错，适合各种活动。记得根据早晚温差适当增减衣物哦。

以上就是今天的成都天气预报，我是小爪，祝你今天愉快！"""
    
    # 使用晓晓语音 (中文女声，非常自然)
    voice = "zh-CN-XiaoxiaoNeural"
    output_file = r"C:\Users\Laptop\.openclaw\workspace\weather-edge-tts.mp3"
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"Generated: {output_file}")

asyncio.run(main())
