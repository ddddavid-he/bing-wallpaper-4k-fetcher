import os



def genItem(date, url, lazy=False):
    small_url = url.replace('UHD', '1280x720')
    full_date = f"20{date[:2]}-{date[2:4]}-{date[4:]}"
    if lazy:
        loading = "loading=\"lazy\""
    else:
        loading = ""
    code = ""
    code += "\t<div class=\"item-container\">\n"
    code += "\t\t<div class=\"img-container\">\n"
    code += f"\t\t<a href={url} target=\"_blank\">"
    code += f"\t\t\t<img src={small_url} alt=\"bing picture\" {loading}>\n"
    code += "\t\t</a>"
    code += "\t\t</div>\n"
    code += "\t\t<h5 class=\"img-title\">\n"
    # code += f"\t\t\t<a href=\"{url}\">{full_date}</a>\n"
    code += f"\t\t\t{full_date} &nbsp;\n"
    code += f"\t\t\t<a href={url} target=\"_blank\">View Full Size</a> &nbsp;\n"
    code += f"\t\t\t<a href=\"BW-{date}.jpg\" download=\"\">Download 4K</a>\n"
    code += "\t\t</h5>\n"
    code += "\t</div>\n"
    return code


def genToday(title, url):
    small_url = url.replace('UHD', '1920x1080')
    code = ""
    code += "\t<div class=\"today-item-container\">\n"
    code += "\t\t<div class=\"img-container\">\n"
    code += f"\t\t\t<img src={small_url} alt=\"\">\n"
    code += "\t\t</div>\n"
    code += "\t\t<h3 class=\"img-title\">\n"
    code += f"\t\t\t<b>Today: </b>{title}\n"
    code += "\t\t</h3>\n"
    code += "\t</div>\n"
    return code
    


def genRow(items):
    code = ""
    code += "<div class=\"row-container\">\n"
    for item in items:
        code += item
        code += "&nbsp;"
    code = code[:-6]
    code += "</div>"
    code += "\n"
    return code
    


with open('./html/head.html', 'r') as file:
    tmp = file.readlines()
head = ''
for line in tmp:
    head = head + line 
head += "\n"
# print(head)
with open('./html/tail.html', 'r') as file:
    tmp = file.readlines()
tail = ''
for line in tmp:
    tail = tail + line 
tail += "\n"
# print(tail)




dates_exists = os.listdir("./wallpaper")
with open('./cache/dates', 'r') as file:
    dates = file.readlines()
with open('./cache/urls', 'r') as file:
    urls = file.readlines()
with open('./cache/today', 'r') as file:
    today = file.readline()
    
dates = [i.replace("\n", "") for i in dates]
urls = [i.replace("\n", "") for i in urls]
today = today.replace("\n", "")
#print(dates)
#print(urls)

num = len(dates)
row_num = num // 3


with open('./html/bing.html', 'w') as file:
    file.write(head)
    
    file.write(genRow([genToday(today, urls[0])]))
    
    for i in range(row_num):
        items = []
        if i > 10:
            lazy = True
        else:
            lazy = False
        for j in range(3):
            date = dates[i*3+j]
            url = urls[i*3+j]
            items.append(genItem(date, url, lazy=lazy))
        file.write(genRow(items))
    if(num%3 != 0):
        items = []
        for j in range(num%3):
            date = dates[row_num*3+j]
            url = urls[row_num*3+j]
            items.append(genItem(date, url, lazy=True))
        file.write(genRow(items))
    file.write("\n\n")
    file.write(tail) 

print("html/bing.html generated.")
    


