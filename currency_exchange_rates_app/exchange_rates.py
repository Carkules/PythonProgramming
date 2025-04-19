"""
This script makes a GUI app showing currency exchange rates from a given url source.
"""
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

def get_rates_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table')

        exchange_rates = [("PLN", "1", "1", "1")]

        rows = table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) >= 4:
                currencies = cells[1].text.strip().split("\n")
                currency_name = currencies[0]
                buy_price = cells[2].text.strip().replace(",", ".")
                sell_price = cells[3].text.strip().replace(",", ".")
                modifier = cells[5].text.strip()
                exchange_rates.append((currency_name, buy_price, sell_price, modifier))

        with open('exchange_rates.txt', 'w') as file:
            for rate in exchange_rates:
                file.write(f"{rate[0]} {rate[1]} {rate[2]} {rate[3]}\n")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

def currency_to_PLN(currency_name, amount, file_with_rates):
    with open(file_with_rates, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if currency_name in line:
                content = line.split()
                buying_price = float(content[1])
                modifier = float(content[3])
                result = amount*buying_price/modifier
                return result

def PLN_to_currency(currency_name, amount, file_with_rates):
    with open(file_with_rates, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            if currency_name in line:
                content = line.split()
                selling_price = float(content[2])
                modifier = float(content[3])
                result = amount*modifier/selling_price
                return result
            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.input_currency_box = QtWidgets.QComboBox(self.centralwidget)
        self.input_currency_box.setGeometry(QtCore.QRect(170, 130, 131, 31))
        self.input_currency_box.setObjectName("input_currency_box")
        self.output_currency_box = QtWidgets.QComboBox(self.centralwidget)
        self.output_currency_box.setGeometry(QtCore.QRect(640, 130, 131, 31))
        self.output_currency_box.setObjectName("output_currency_box")

        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(20, 130, 131, 31))
        self.input_amount.setObjectName("input_amount")

        self.result_amount = QtWidgets.QLabel(self.centralwidget)
        self.result_amount.setGeometry(QtCore.QRect(510, 130, 131, 31))
        self.result_amount.setText("")
        self.result_amount.setObjectName("result_amount")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 10, 291, 51))
        self.title.setText("Exchange rate calculator")
        self.title.setObjectName("title")

        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(350, 130, 131, 31))
        self.calculate_button.setObjectName("calculate_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_currencies('exchange_rates.txt')
        self.calculate_button.clicked.connect(self.clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))

    def load_currencies(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            for line in lines:
                content = line.split()
                currency_name = content[0]
                self.input_currency_box.addItem(currency_name)
                self.output_currency_box.addItem(currency_name)
    
    def clicked(self):
        amount_str = self.input_amount.text()
        try:
            amount = float(amount_str)
            input_currency = self.input_currency_box.currentText()
            output_currency = self.output_currency_box.currentText()
            file_name = 'exchange_rates.txt'

            if input_currency == output_currency:
                self.result_amount.setText(amount_str)
            elif input_currency == "PLN":
                result = PLN_to_currency(output_currency, amount, file_name)
                self.result_amount.setText(str(result))
            elif output_currency == "PLN":
                result = currency_to_PLN(input_currency, amount, file_name)
                self.result_amount.setText(str(result))
            else:
                pln = currency_to_PLN(input_currency, amount, file_name)
                result = PLN_to_currency(output_currency, pln, file_name)
                self.result_amount.setText(str(result))
        except ValueError:
            self.result_amount.setText("Error")



def run_ui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



url = "https://www.pekao.com.pl/kursy-walut/lista-walut.html"
try:
    get_rates_from_url(url)
except:
    print("Loading data from internet failed. I will use local data instead.")

run_ui()