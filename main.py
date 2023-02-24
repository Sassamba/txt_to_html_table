html = ''
with open("adv.txt", "r", encoding='utf-8') as f:
    i = 0
    for l in f:
        if(i % 5 == 0):
            html += "<tr>"
        html += f"<td>{l}</td>";
        if(i % 5 == 4):
            html += "</tr>"
        i += 1
# Write the HTML table to a file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
