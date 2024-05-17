class Car:
  def __init__(self, brand, hp, automatic, color, date):
    self.brand = brand
    self.hp = hp
    self.automatic = automatic
    self.color = color
    self.date = date

  def __str__(self):
    transmission = "automatic" if self.automatic else "manual"
    print_date = self.date.split("-")[0]
    return f"{self.color} {print_date} {self.brand}, {transmission} {self.hp}HP"



car_brand = "seat" # @param {type:"string"}
hp = 210 # @param {type:"slider", min:50, max:1200, step:5}
automatic = True # @param {type:"boolean"}
color = "blue" # @param ["red", "blue", "green", "yellow", "black", "white"]
purchase_date = "2011-09-12" # @param {type:"date"}
my_car = Car(car_brand, hp, automatic, color, purchase_date)
print(my_car)
