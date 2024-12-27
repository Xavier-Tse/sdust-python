def ReadDictionary(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      return {line.split()[0]: line.split()[1] for line in file if line.strip()}
  except FileNotFoundError:
    return {}

def SaveDictionary(file_path, dictionary):
  with open(file_path, 'w', encoding='utf-8') as file:
    for word, meaning in dictionary.items():
      file.write(f"{word} {meaning}\n")

def Add(dictionary, file_path):
  word = input("请输入英文单词:")
  meaning = input("请输入中文释义:")
  if word in dictionary:
    print("该单词已添加到字典库")
  else:
    dictionary[word] = meaning
    SaveDictionary(file_path, dictionary)
    print("单词添加成功")

def Query(dictionary):
  word = input("请输入要查询的英文单词:")
  if word in dictionary:
    print(f"{word} 的中文释义是:{dictionary[word]}")
  else:
    print("字典库中未找到这个单词")

def main():
  filePath = 'dictionary.txt'
  dictionary = ReadDictionary(filePath)
  while True:
    print("\n请选择功能:")
    print("1. 添加单词")
    print("2. 查询单词")
    print("3. 退出")
    options = input("请输入选项编号:")
    if options == '1':
      Add(dictionary, filePath)
    elif options == '2':
      Query(dictionary)
    elif options == '3':
      print("退出程序")
      break
    else:
      print("输入有误，请重新输入")

if __name__ == '__main__':
  main()
