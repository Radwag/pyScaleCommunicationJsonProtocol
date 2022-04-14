import json


class CommandsRdgJson:

    def command_get_tables(self, socket):
        query = json.dumps({'Command': 'DbGetTables'})
        socket.send(query)
        return socket.reciv()

    def command_get_table_info(self, socket, _table_name):
        query = json.dumps({'Command': 'TableInfo', 'Table': _table_name})
        socket.send(query)
        return socket.reciv()

    def command_insert(self, socket, _table_name, json_items):
        json_items_builder = ''
        query = json.dumps({'Command': 'DbInsert', 'Table': _table_name})
        data = json.loads(query)

        for json_item in json_items:
            json_items_builder = json_items_builder + ',' + json_item.get_object()
            data[json_item.name] = json_item.value

        socket.send(json.dumps(data))
        return socket.reciv()

    def command_update_by_index(self, socket, _table_name, _index, json_items):
        json_items_builder = ''
        query = json.dumps({'Command': 'DbUpdate', 'Index': _index, 'Table': _table_name})
        data = json.loads(query)

        for json_item in json_items:
            json_items_builder = json_items_builder + ',' + json_item.get_object()
            data[json_item.name] = json_item.value

        socket.send(json.dumps(data))
        return socket.reciv()

    def command_update_by_index(self, socket, _table_name, _id, json_items):
        json_items_builder = ''
        query = json.dumps({'Command': 'DbUpdate', 'Index': _id, 'Table': _table_name})
        data = json.loads(query)

        for json_item in json_items:
            json_items_builder = json_items_builder + ',' + json_item.get_object()
            data[json_item.name] = json_item.value

        socket.send(json.dumps(data))
        return socket.reciv()

    def command_read_by_index(self, socket, _table_name, _index):
        query = json.dumps({'Command': 'DbRead', 'Table': _table_name, 'Index': _index})
        socket.send(query)
        return socket.reciv()

    def command_read_by_id(self, socket, _table_name, _id):
        query = json.dumps({'Command': 'DbRead', 'Table': _table_name, 'Id': _id})
        socket.send(query)
        return socket.reciv()

    def command_delete_by_index(self, socket, _table_name, _index):
        query = json.dumps({'Command': 'DbDelete', 'Table': _table_name, 'Index': _index})
        socket.send(query)
        return socket.reciv()

    def command_delete_by_id(self, socket, _table_name, _id):
        query = json.dumps({'Command': 'DbDelete', 'Table': _table_name, 'Id': _id})
        socket.send(query)
        return socket.reciv()
