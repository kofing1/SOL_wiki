import json

def convert_images_to_json(input_file, output_file):
    """
    将文本文件中的图片文件名转换为JSON数组格式
    
    Args:
        input_file: 输入文本文件路径
        output_file: 输出JSON文件路径
    """
    try:
        # 读取原始文件
        with open(input_file, 'r', encoding='utf-8') as f:
            # 读取所有行，去除空白字符和空行
            lines = [line.strip() for line in f if line.strip()]
        
        # 转换为JSON数组格式
        json_data = json.dumps(lines, indent=2, ensure_ascii=False)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_data)
        
        print(f"转换成功！已保存到: {output_file}")
        print(f"共处理了 {len(lines)} 个文件名")
        
        return lines
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")

# 使用示例
if __name__ == "__main__":
    # 指定输入输出文件
    input_filename = "images.txt"  # 你的原始文本文件
    output_filename = "images.json"  # 输出JSON文件
    
    # 执行转换
    convert_images_to_json(input_filename, output_filename)