import requests
from bs4 import BeautifulSoup

def get_weather():
    url = 'https://www.msn.cn/zh-cn/weather/forecast/in-上海市，浦东新区'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取天气描述
    p_elements = soup.find_all('p', class_='summarydesccompact-e1_1')
    weather_desc = [p.get_text() for p in p_elements]

    # 获取温度
    element = soup.find('a', {'class': ('summarytemperaturecompact-e1_1', 'summarytemperaturehover-e1_1')})
    if element and 'title' in element.attrs:
        temperature = element['title']
    else:
        temperature = "没有找到温度信息"

    return weather_desc, temperature

if __name__ == '__main__':

    weather_desc, temperature = get_weather()
    print("天气描述:", weather_desc)
    print("温度:", temperature)


