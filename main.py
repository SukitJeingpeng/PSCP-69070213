#จงแสดงผลตัวแปร text ที่มีการเติม (padding) ข้อความ "z" ทางขวาของตัวแปรให้มีความยาวรวมกัน 20 อักษร โดยใช้เมธอดด้านบนที่กล่าวถึง
text = "pineapple"
x = text.ljust(20)
y = text.rjust(20)
print(x,text)
print(y,text)