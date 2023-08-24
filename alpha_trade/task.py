from .models import User

def increase_profit_balance():
    instances = User.objects.exclude(trade_status= "Inactive")
    
    for instance in instances:
        if instance.trading_plan == "Starter":
            profit_increase = 50
            print("1")
            instance.profit_balance += profit_increase
            instance.save()
            


        if instance.trading_plan == "Bronze":
            profit_increase = 100
            instance.profit_balance += profit_increase
            instance.save()
            

        if instance.trading_plan == "Silver":
            profit_increase = 200
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "Gold":
            profit_increase = 300
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "Diamond":       
            profit_increase = 500
            instance.profit_balance += profit_increase
            instance.save()

        if instance.trading_plan == "Platinum":
            profit_increase = 1000
            instance.profit_balance += profit_increase
            instance.save()