# 简单关键词记忆搜索
# 用于替代需要 API key 的语义搜索

import os
import re
from pathlib import Path
from datetime import datetime

class SimpleMemorySearch:
    def __init__(self):
        self.workspace = Path(os.path.expanduser("~/.openclaw/workspace"))
        
    def search(self, query, max_results=10):
        """简单关键词搜索"""
        results = []
        query_lower = query.lower()
        
        # 获取所有记忆文件
        memory_files = []
        
        # 主要记忆文件
        memory_md = self.workspace / "MEMORY.md"
        if memory_md.exists():
            memory_files.append(memory_md)
        
        # 每日记忆文件
        memory_dir = self.workspace / "memory"
        if memory_dir.exists():
            memory_files.extend(sorted(memory_dir.glob("*.md"), reverse=True))
        
        # 搜索每个文件
        for file_path in memory_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                # 分段搜索（按段落或标题）
                current_section = []
                section_start = 0
                
                for i, line in enumerate(lines):
                    # 如果是标题或空行，结束当前段
                    if line.startswith('#') or (line.strip() == '' and current_section):
                        if current_section:
                            # 搜索当前段
                            section_text = '\n'.join(current_section)
                            if query_lower in section_text.lower():
                                # 计算相关性分数
                                score = self._calculate_score(section_text, query_lower)
                                results.append({
                                    "path": str(file_path.relative_to(self.workspace)),
                                    "line": section_start + 1,
                                    "content": section_text[:500] + "..." if len(section_text) > 500 else section_text,
                                    "score": score
                                })
                            current_section = []
                            section_start = i + 1
                    
                    current_section.append(line)
                
                # 处理最后一段
                if current_section:
                    section_text = '\n'.join(current_section)
                    if query_lower in section_text.lower():
                        score = self._calculate_score(section_text, query_lower)
                        results.append({
                            "path": str(file_path.relative_to(self.workspace)),
                            "line": section_start + 1,
                            "content": section_text[:500] + "..." if len(section_text) > 500 else section_text,
                            "score": score
                        })
                        
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        # 按分数排序
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:max_results]
    
    def _calculate_score(self, text, query):
        """计算相关性分数"""
        text_lower = text.lower()
        
        # 基础分数
        score = 0
        
        # 完全匹配次数
        score += text_lower.count(query) * 10
        
        # 如果是标题匹配，额外加分
        if query in text.split('\n')[0].lower():
            score += 50
        
        # 如果包含关键词的同义词或相关词
        related_terms = {
            "remix": ["re:mix", "混合", "重组"],
            "github": ["git", "仓库", "推送"],
            "token": ["api", "key", "认证"],
            "memory": ["记忆", "存储", "回忆"],
            "skill": ["技能", "工具", "能力"]
        }
        
        for key, terms in related_terms.items():
            if query == key or query in terms:
                for term in terms:
                    if term in text_lower:
                        score += 5
        
        # 日期越近越重要
        if "2026-02" in text:
            score += 10
        
        return score

# 全局实例
_memory_search = None

def search_memory(query: str, max_results: int = 5):
    """
    搜索记忆文件
    
    用法:
        results = search_memory("Re:Mix", max_results=3)
        for r in results:
            print(f"{r['path']}:{r['line']} - {r['content'][:100]}")
    """
    global _memory_search
    if _memory_search is None:
        _memory_search = SimpleMemorySearch()
    
    return _memory_search.search(query, max_results)

# 如果直接运行此脚本
if __name__ == "__main__":
    import sys
    
    # 设置编码
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input("搜索关键词: ")
    
    print(f"\n搜索: '{query}'\n")
    print("=" * 60)
    
    results = search_memory(query, max_results=10)
    
    if not results:
        print("未找到相关记忆")
    else:
        for i, r in enumerate(results, 1):
            print(f"\n[{i}] {r['path']}:{r['line']} (score: {r['score']})")
            print("-" * 40)
            print(r['content'])
            print()
    
    print("=" * 60)
    print(f"共找到 {len(results)} 条记忆")
