class User:
    '''User of the store'''

    def __init__(self, name, password):
       self._name = name
       self._password = password
       self._logged_in = False


    def login(self, password):
        if password == self._password:
            self._logged_in = True
        else:
            print('Incorrect password')

    def show_status(self):
        if self._logged_in:
            print(f'{self._name} is logged in')
        else:
            print(f'{self._name} is NOT logged in')

customer = User(
    name='Bruce',
    password='SuperSecretPassword'
)

customer.login('IncorrectPassword')
customer.show_status()
customer.login('SuperSecretPassword')
customer.show_status()

class Admin(User):
    '''Administrator of the store'''

    def __init__(self, name, password, staff_id):
        """Initialise data for a store user"""
        super().__init__(name, password)
        self._staff_id = staff_id

    def add_product(self, name):
        '''Add new product to inventory'''
        if self._logged_in:
            print(f'{self._name} ({self._staff_id}) added product: {name}')
        else:
            print('Login to add product')

staff = Admin(
    name = 'Gagik',
    password = 'SuperGagik1123',
    staff_id = 123,
)
staff.add_product('Coffee')
staff.login('SuperGagik1123')
staff.show_status()
staff.add_product('Coffee')