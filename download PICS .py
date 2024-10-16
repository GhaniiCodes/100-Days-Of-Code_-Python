import requests

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("Image downloaded:", save_path)


urls = [
    "https://images.app.goo.gl/ZCvU4WgNoSNKMkXH6",
    "https://images.app.goo.gl/H9JLPnhZyqcXbhp79",
    "https://images.app.goo.gl/P1sELwdWStagUiws9",
    "https://images.app.goo.gl/5Dxz17zMketPrf6c9",
    "https://images.app.goo.gl/zRRNe6W6YYVyzFxL7"
]


for i, Url in enumerate(urls , start = 1) :
    save_path = f"D:\PYTHON\downloaded\image {i}.PNG"
    download_image(Url, save_path)
    