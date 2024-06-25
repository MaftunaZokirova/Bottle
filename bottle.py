class Bottles:
    #def __init__(self) -> None:
       # print("Default constructor")

    def __init__(self, bot_percase: int, profit_perBottle: float) -> None:
        self.bot_percase = bot_percase
        self.profit_perBottle = profit_perBottle
        self.days_peryear = 365
        self.cases_perday = 0
        self.daily_profit = 0
        self.yearly_profit = 0
        print("Bottles per Case \t", self.bot_percase)
        print("Days per Year \t\t", self.days_peryear)
        print("Profit Per Bottle \t", self.profit_perBottle)

    def Run(self) -> None:
       self.ObtainCasesPerDay()
       self.CalculateDailyProfit()
       self.CalculateYearlyProfit()
       self.DisplayDailyProfit()
       

    def ObtainCasesPerDay(self) -> None:
        self.cases_perday = input(" Please input cases per day: ")

    def CalculateDailyProfit(self) -> None:
        self.daily_profit = float(self.cases_perday) * float(self.bot_percase) * self.profit_perBottle

    def CalculateYearlyProfit(self) -> None:
        self.yearly_profit = float(self.daily_profit) * float(self.days_peryear)

    def DisplayDailyProfit(self) -> None:
        print("The store has made: $ ", self.daily_profit)
        print("From above we can say that yearly profit is : $", self.yearly_profit )
    



if __name__ == '__main__':
    bottles_produc = Bottles(12, 0.2)
    bottles_produc.Run()