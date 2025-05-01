import csv
FILENAME ="soilData.csv"
def create_file():
  with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Moisture", "Temperature"])
#input ad save data
def log_data():

    moisture=float(input("enter the moisture of the soil(%):"))
    temperature=float(input("enter the temperature of the soil(c):"))
    with open(FILENAME, mode='a',newline='')as file:
      writer=csv.writer(file)
      writer.writerow([moisture, temperature])
    print("😎 data saved")
#analyze and print summary
def read_and_analyze():
  moisture=[]
  temps=[]
  with open(FILENAME, mode='r')as file:
    reader=csv.DictReader(file)
    for row in reader:
      try:
        moisture.append(float(row["Moisture"]))
        temps.append(float(row["Temperature"]))
      except ValueError:
        print("🤦‍♀sorry no data found")
  if moisture and temps:
    print("🙂‍↔ summary:")
    print(f"minimum:{min(moisture)}%| maximum:{max(moisture)}%|average:{sum(moisture)/len(moisture):.2f}%")
    print(f"minimum:{min(temps)}c|maximum:{max(temps)}c,|average:{sum(temps)/len(temps):.2f}c")
  else:
      print("😵‍💫 oopssss, surrrrryyyy!!!")


  #menu to run the app
def menu():
    create_file()  # ✅ correct, no colon
    while True:
        print("\n -----Soil Data Logger----")
        print("choose your option from 1 to 3")
        print("1.log new data")
        print("2.summary")
        print("3.exit")
        choice = input("choose: ")

        if choice == '1':
            log_data()
        elif choice == '2':
            read_and_analyze()
        elif choice == '3':
            print("exiting...😒😒😒")
            break
        else:
            print("invalid input plichhhhh🤖🤖🤖")
menu()