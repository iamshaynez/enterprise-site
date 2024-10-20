import os
import re
import yaml

def generate_slug(title):
    # 转换为小写
    slug = title.lower()
    # 移除特殊字符，只保留字母、数字和空格
    slug = re.sub(r'[^a-z0-9\s]', '', slug)
    # 将空格替换为连字符
    slug = re.sub(r'\s+', '-', slug)
    return slug

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取 YAML 前置元数据
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        metadata = yaml.safe_load(yaml_content)

        # 检查 slug 是否为空
        if 'slug' in metadata and metadata['slug'] == '':
            # 从 title 生成新的 slug
            new_slug = generate_slug(metadata['title'])
            metadata['slug'] = new_slug

            # 更新 YAML 内容
            new_yaml = yaml.dump(metadata, allow_unicode=True, sort_keys=False)
            new_content = f'---\n{new_yaml}---\n' + content[match.end():]

            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"No changes needed for {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path)

if __name__ == "__main__":
    directory = "./content"
    process_directory(directory)