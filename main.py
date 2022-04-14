# This is a sample Python script.
import json

from Model.JsonItemModel import JsonItemModel
from Services.SocketRdgJson import SocketRdgJson
from Services.CommandsRdgJson import CommandsRdgJson


class Main:

    def __init__(self):
        self.socket_rdg_json = SocketRdgJson()
        self.commands = CommandsRdgJson()

    def switch(self):
        option = int(input("----------------------"
                           "\nSelect your option (number): "
                           "\n  0 - Exit"
                           "\n  1 - Get tables"
                           "\n  2 - Get Clients table info"
                           "\n  3 - Insert record to Clients table"
                           "\n  4 - Update last record from Clients table"
                           "\n  5 - Get last record from Clients table"
                           "\n  6 - Delete last record from Clients table"
                           "\n"))

        if option == 0:
            self.socket_rdg_json.close()

        elif option == 1:
            print(json.dumps(self.commands.command_get_tables(self.socket_rdg_json)) + "\n")
            self.switch()

        elif option == 2:
            print(json.dumps(self.commands.command_get_table_info(self.socket_rdg_json, 'Clients')) + "\n")
            self.switch()

        elif option == 3:
            record_values = []
            data = self.commands.command_get_table_info(self.socket_rdg_json, 'Clients')

            for db_name in data['Items']:
                if db_name['Alterability'] == 0:
                    record_values.append(JsonItemModel(db_name['DbName'], str(input("Enter value for: "+db_name['DbName']+", Type: "+str(db_name['Type'])+" \n"))))

            print(json.dumps(self.commands.command_insert(self.socket_rdg_json, 'Clients', record_values)) + "\n")
            self.switch()

        elif option == 4:
            record_values = []
            data = self.commands.command_get_table_info(self.socket_rdg_json, 'Clients')

            for db_name in data['Items']:
                if db_name['Alterability'] == 0:
                    record_values.append(JsonItemModel(db_name['DbName'], str(input("Enter new value for: "+db_name['DbName']+", Type: "+str(db_name['Type'])+" \n"))))

            print(json.dumps(self.commands.command_update_by_index(self.socket_rdg_json, 'Clients', data['Count'] - 1, record_values)) + "\n")
            self.switch()

        elif option == 5:
            data = self.commands.command_get_table_info(self.socket_rdg_json, 'Clients')
            print(json.dumps(self.commands.command_read_by_index(self.socket_rdg_json, 'Clients', data['Count']-1)) + "\n")
            self.switch()

        elif option == 6:
            data = self.commands.command_get_table_info(self.socket_rdg_json, 'Clients')
            if data['Count'] > 0:
                print(json.dumps(self.commands.command_delete_by_index(self.socket_rdg_json, 'Clients', data['Count']-1)) + "\n")
            else:
                print('No records i table')
            self.switch()

        else:
            print("Incorrect option")
            self.switch()

    def main(self):
        self.socket_rdg_json.connect(str(input("Enter ip address: \n")))
        self.switch()


if __name__ == '__main__':
    Main().main()
