# print({x for x in range(100) if x % 3 == 0})
# number_list = [x for x in range(100) if x % 3 if x % 5]
# print(number_list)
# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, 2019)))
#
# first_array = [1, 2, 3, 4]
# second_array = first_array.pop
#
# print("Hello World"[::-1]
# )


import requests


def cache(url):
    id = url.split('/')[6]
    data = {}
    caches_id = []
    if id in caches_id:
        return data
    else:
        headers = {"Authorization": "Basic c2tfY2VydF9tcWtFdmp5aXVhNU5XR2hoRTU3V2ZLOg=="}
        req = requests.get(url, headers=headers)
        data = req.json()
        caches_id.append(id)
        return data


print(cache("https://cert-api.kashio.net/v1/payments/invoices/inv_cs0_fYiaJSCADHwYdAASgGMP3Y"))
