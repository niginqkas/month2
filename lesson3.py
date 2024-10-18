class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        total_power = self.cpu * self.memory
        average = (self.cpu + self.memory) / 2
        print(f"Total power: {total_power}")
        print(f"Average: {average}")

    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim = self.__sim_cards_list[sim_card_number - 1]
            print(f"Call to {call_to_number} from SIM-{sim_card_number} {sim['carrier']}")
        else:
            print("Invalid SIM card number.")

    def __str__(self):
        return f"Phone(sim_cards={self.__sim_cards_list})"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Building route to {location}")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards={self.sim_cards_list})"


computer1 = Computer(cpu=3.5, memory=16)
phone1 = Phone(sim_cards_list=[{'carrier': 'Beeline', 'number': '+996 777 99 88 11'}])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=[{'carrier': 'Megacom', 'number': '+996 700 11 22 33'}])


print(computer1)
print(phone1)
print(smartphone1)
smartphone1.make_computations()
smartphone1.call(1, "+996 555 66 77 88")
smartphone1.use_gps("Central Park")





