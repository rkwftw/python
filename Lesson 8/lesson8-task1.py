class Data:
    def __init__(self,d_m_y):
        self.d_m_y = str(d_m_y)


    @classmethod
    def cm(cls, d_m_y):
        date = []

        for i in d_m_y.split("."):
            if i != ".": date.append(i)

        return int(date[0]), int(date[1]), int(date[2])


    @staticmethod
    def sm(d, m, y):

        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2222 >= y >=0:
                    return ("valid")
                else:
                    return ("invalid year")
            else:
                return ("invalid month")
        else:
            return ("invalid day")

    def __str__(self):
        return f'Date is: {Data.cm(self.d_m_y)}'


test = Data("1.2.1989")
print(test)
print(test.sm(1, 13, 2001))
print(Data.sm(1, 1, 2021))
print(Data.sm(55, 55, 2000))

