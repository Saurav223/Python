Question = ['What is the largest mount in the world','In which place Lord Buddha was born','Which is the largest lake of Nepal',
'Fastest land animal','Longest river of Nepal']

Option = ["1.Mt Everst  2.Mt K2  3.Mt Annapurna  4.Mt Kanchanjaga","1.Kathmandu  2.Pokhara  3.Chitwan  4.Lumbini",
          "1.Rara   2.Shy Phosundo  3.Tilicho  4.Fewa","1.Leopard  2.Deer  3.Cheetah  4.Lion","1.Gandaki  2.Karnali  3.Narayani  4.Khosi"]

answer= [1,4,1,3,2]
price = 0

print("Welcom to KO Bancha Hajarpati")
name = input("Enter your name to begin the game: ")
for i in range(0,5):
    print(Question[i])
    print(Option[i])
    
    a= int(input("Enter the number of option: "))
    if(a!=answer[i]):
        print("Wrong Answer")
        break
    else:
        print("Correct Answer")
        price = price+1000

if(price==0):
    print("Losser",name,"you won't won anything")

else:
    print("Congratulate",name,"you won ",price)
