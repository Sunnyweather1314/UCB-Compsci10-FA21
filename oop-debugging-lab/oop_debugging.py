# Account

class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> sophia_account = Account('Sophia')
    >>> sophia_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> sophia_account.transactions
    [('deposit', 1000000)]
    >>> sophia_account.withdraw(100)      # buying dinner
    999900
    >>> sophia_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02
    balance = 1000
    """Did not understand what these two lines are for."""

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.transactions.append(('withdraw', amount))
            self.balance = self.balance - amount
            
        return self.balance


# Quidditch

class QuidditchPlayer:
    def __init__(self, name, base_energy):
        """
        QuidditchPlayers have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy

class Beater(QuidditchPlayer):
    role = "bludgers"

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. 
        After playing for time minutes, Beaters lose their base energy level 
        divided by the number of minutes. If time is 0, return "You can't divide by zero!" instead.
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.energy(40)
        624.0
        >>> fred.energy(0)
        You can't divide by zero!
        """
        "*** YOUR CODE HERE ***"
        if time == 0:
            return "You cannot divide by zero!"
        else:
            return self.base_energy-self.base_energy/time
             
        

class Chaser(QuidditchPlayer):
    role = "score"
    energy_expended = 20
    
    def __init__(self, name, base_energy, goals):
        """
        Chasers have a name, score goals, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy
        self.goals = goals
        

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. For every goal 
        they score, they use energy_expended units of energy. In addition, they also use 
        10% of energy_expended if the number of minutes they have played is a multiple of 9.
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.energy(20)
        190
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.energy(45)
        338.0
        """
        "*** YOUR CODE HERE ***"
        if time == 0:
            return "You cannot divide by zero"
        elif time % 9 == 0:
            self.base_energy = self.base_energy-self.energy_expended*self.goals*1.1
        else:
            return self.base_energy-self.energy_expended*self.goals
        
                   
            
class Seeker(QuidditchPlayer):
    role = "snitch"
    energy_expended = 5

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. Seekers expend energy_expended 
        units of their energy for every minute they have been playing.
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.energy(30)
        550
        """
        "*** YOUR CODE HERE ***"
        return self.base_energy - time*Seeker.energy_expended
         



class Keeper(QuidditchPlayer):
    role = "guard"
    energy_expended = 50

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. If less than 30 minutes have 
        passed, then Keepers do not lose any energy. If 30 minutes or more have passed, 
        then Keepers expend 80% of their energy_expended units for every full 15 
        minutes that pass.
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.energy(45)
        260.0
        """
        "*** YOUR CODE HERE ***"
        if time < 30:
            return self.base_energy
        else:
            energy = self.base_energy-30*Keeper.energy_expended
            new_t = time-30
            new_e = Keeper.energy_expended * 1.8
            while new_t >= 0:
                if new_t >= 15:
                    energy = energy - new_e * 15
                    new_t = new_t - 15
                    new_e = new_e * 1.8
                else:
                    energy = energy - new_e * new_t
            return energy
                

