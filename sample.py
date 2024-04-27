def process_item(products: dict[int, str, str]):
    for id, product, company in products.item():
        print(f"{id}, {product}, {company}")