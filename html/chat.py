input = open('input.txt', 'r')
output = open('chat.html', 'x')
temp = ""

output.write("<html>\n<head>\n<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js'></script></head>\n<body>")

for i in input.readlines():
    if i != "User" or i != "ChatGPT":
        temp += i
    elif i == "User":
        output.write("<div class='title'>"+i+"</div><div class='panel success' style='position:relative;margin-left:0px;>"+temp+"</div>")
        temp = ""
    elif i == "ChatGPT":
        output.write("<div class='title'>"+i+"</div><div class='panel default' style='position:relative;margin-right:0px;>"+temp+"</div>")
        temp = ""
    else:
        continue
        


output.write('</body>\n</html>')
output.close()