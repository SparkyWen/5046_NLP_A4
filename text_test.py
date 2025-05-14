import re

# 定义输入和输出文件路径
input_file = 'many_shot_results.txt'
output_file = 'text_analysis.txt'

# 读取文件内容
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式提取所需的信息
pattern = re.compile(
    r'Standard SQL:\n(.*?)\nRaw LLM Response:\n```sql\n(.*?)\n```\nExtracted Predicted SQL:\n(.*?)\n✅ Exact match: (.*?)\n✅ Semantic match: (.*?)\n',
    re.DOTALL | re.IGNORECASE
)

matches = pattern.findall(content)

# 将结果写入到新的文件中
with open(output_file, 'w', encoding='utf-8') as output:
    for idx, match in enumerate(matches, 1):
        standard_sql, raw_llm_response, extracted_sql, exact_match, semantic_match = match

        output.write(f"Example [{idx}]\n")
        output.write("Standard SQL:\n")
        output.write(standard_sql.strip() + "\n\n")

        output.write("Raw LLM Response:\n")
        output.write(raw_llm_response.strip() + "\n\n")

        output.write("Extracted Predicted SQL:\n")
        output.write(extracted_sql.strip() + "\n\n")

        output.write(f"Exact match: {exact_match.strip()}\n")
        output.write(f"Semantic match: {semantic_match.strip()}\n")

        output.write("-" * 80 + "\n")

print(f"Analysis results have been successfully written to {output_file}")
