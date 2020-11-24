from datetime import datetime
import pygame
from google.cloud import bigquery

class MousePosition:
    def __init__(self, credentials, table_id):
        self.data = []
        self.credentials = credentials
        self.table_id = table_id
        self.counter = 0

    def save_mouse_position(self, func):
        def save(*args, **kwargs):
            """
            save the time, x and y position of the mouse in data attribute
            """
            self.counter += 1
            if self.counter % 5 == 0: # 1 sample per 5 frames
                mouse_position = pygame.mouse.get_pos()
                time = datetime.utcnow()
                self.data.append((time, mouse_position))
            func(*args, **kwargs)
        return save

    def send_data(self, func):
        def convert_data_to_json(data, user_name, game_id):
            return [{'user': user_name, 'game_id': str(game_id), 'time': time.strftime('%Y-%m-%dT%H:%M:%S.%f'), 'x': x, 'y': y} for time, (x, y) in data]

        def send(game):
            """
            send data to BigQuery, each element is a row in the table
            """
            func(game)
            rows_to_insert = convert_data_to_json(self.data, game.user_name, game.game_id)
            client = bigquery.Client.from_service_account_json(self.credentials)
            errors = client.insert_rows_json(self.table_id, rows_to_insert)  # Make an API request.
            if errors == []:
                print('New rows have been added.')
            else:
                print(f'Encountered errors while inserting rows: {errors}')
        return send
        

    def __str__(self):
        return str(self.data)
    