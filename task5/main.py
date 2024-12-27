import requests
from bs4 import BeautifulSoup
import os

def Hack(url):
  try:
    outputFolder = 'output_files'
    if not os.path.exists(outputFolder):
      os.makedirs(outputFolder)

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    olTags = soup.find_all('ol')

    for _, ol in enumerate(olTags):
      liTags = ol.find_all('li')
      for li in liTags:
        aTag = li.find('a')
        if aTag:
          href = aTag.get('href')
          text = aTag.text
          print(f"链接显示内容: {text}")
          print(f"跳转URL: {href}")

          subResponse = requests.get(href)
          subResponse.raise_for_status() # 检测http状态码
          subSoup = BeautifulSoup(subResponse.text, 'html.parser')
          # print({subResponse.text})

          pTags = subSoup.find_all('p')
          pContent = '\n'.join([p.text for p in pTags])

          fileName = f"{text}.txt"
          filePath = os.path.join(outputFolder, fileName)
          with open(filePath, 'w', encoding='utf-8') as file:
            file.write(pContent)

          print(f"跳转页面内容已写入文件: {filePath}\n")
        else:
          print(f"没有找到 <a> 标签，<li> 标签内容: {li.text}")

      print("\n")

  except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")

url = 'https://www.136book.com/hongloumeng'
Hack(url)
