# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# # NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

def handle_under100(i):
    lsum = 0
    if i <= 20:
        lsum += len(number[i])
    if i > 20 and i <= 99:
        if i % 10 == 0:
            lsum += len(number[i])
        else :
            remain = i % 10
            withoutSingle = i - remain
            temp = len(number[withoutSingle]) + len(number[remain])
            lsum += temp
    return lsum 

def count_letter_sum(n):
    lsum = 0
    for i in range(1, n+1):
        # 处理 1～20
        lsum += handle_under100(i)
        if i >= 100 and i <= 999:
            if i % 100 == 0:
                k = i // 100
                print("i=",i ,"k=",k)
                lsum += len(number[k]) + len(number[100])
            else:
                k = i // 100
                remain = i % 100
                # print(k,remain)
                lsum += len(number[k]) + len(number[100]) + 3 + handle_under100(remain)
        if i == 1000:
            lsum += len(number[1000]) + 3
    print(lsum)

if __name__ == "__main__":
    count_letter_sum(1000)