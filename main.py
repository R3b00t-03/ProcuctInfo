from Product_Info.ProductInfo import AmazonInfo

if __name__ == '__main__':
    info = AmazonInfo("https://www.amazon.de/CHEETOS-knusprigen-gew%C3%BCrzte-Snacks-240-9/dp/B003H3U2XC/?_encoding=UTF8&pd_rd_w=xbxkn&pf_rd_p=5d071b01-5bf0-4ff1-842b-a79a8b10aee8&pf_rd_r=7SJ5NH8K9DEQ8F9MNA74&pd_rd_r=e6b05c6c-44af-4d20-9c1c-f307ab313b6d&pd_rd_wg=D7pUV&ref_=pd_gw_trq_ed_4j6q99uo")
    print(f"Title: {info.getTitle()}")
    print(f"Price: {info.getPrice()}")
    info.quit()


