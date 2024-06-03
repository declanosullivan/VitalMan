import requests
from PIL import Image
from io import BytesIO

# URLs for images from Centurion Remedies
image_urls = {
    "Vidalista 80mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Tadalafil%20Vidalista%2080mg%20Tablets%201-1000x1000.jpg",
    "Vidalista 40mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Tadalafil%20Vidalista%2040mg%20Tablets%201-1000x1000.jpg",
    "Vidalista 20mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Tadalafil%20Vidalista%2020mg%20Tablets%201-1000x1000.jpg",
    "Vilitra 40mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Vardenafil%20Vilitra%2040mg%20Tablets%201-1000x1000.jpg",
    "Cenforce 100mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Tadalafil%20Cenforce%20100mg%20Tablets%201-1000x1000.jpg",
    "Cenforce 200mg": "https://www.centurionremedies.com/image/cache/catalog/Products/Tadalafil%20Cenforce%20200mg%20Tablets%201-1000x1000.jpg"
}

# Download and save images
for name, url in image_urls.items():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(f"/mnt/data/{name.replace(' ', '_').lower()}.jpg")

image_files = list(image_urls.keys())
image_files
