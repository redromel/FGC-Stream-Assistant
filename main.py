# TODO:  Loser Identifier for Grands
# TODO:  Better Error Handling when querying
# TODO:  NiceGUI Implementation for fun

from dotenv import load_dotenv
import requests
from event_listner import *
from queries import *
from query_parser import *
from writer import *
from nicegui import ui
from constants import *


# *Testing variables
# phase_id = 1749308
# # phase_id = 1276356
# player_id = 16105
# slug = 'tournament/genesis-9-1/event/melee-singles'
# t_slug = 'tournament/py-testing-tourney-2'
# t_id = 704088

# keep iterating through pages until pageInfo = 0 and nodes = []

# P1 = 17646355
# P2 = 17646351

mutation_vars = {'setId':  79168390,
                 'winnerId': 17646351,
                 'gameData': [
                     {
                         'winnerId': 17646355,
                         'gameNum': 1
                     },
                     {
                         'winnerId': 17646355,
                         'gameNum': 2
                     },
                     {
                         'winnerId': 17646355,
                         'gameNum': 3
                     },
                     {
                         'winnerId': 17646351,
                         'gameNum': 3
                     },
                     {
                         'winnerId': 17646351,
                         'gameNum': 4
                     },
                     {
                         'winnerId': 17646351,
                         'gameNum': 5
                     }
                 ]}
set_payload = {'query':  SCOREBOARD_MUTATION, 'variables': mutation_vars}


def main():
    ...

    response = requests.post(url=API_URL, json=set_payload, headers=HEADER)
    response_json = response.json()
    print(json.dumps(response_json, indent=2))

    # # #  *Grabbing Events and Phases based on tournament slug
    # slug_input = ui.input(label='start.gg tournament slug',
    #                       placeholder='tournament/tournament-name/').props('size=80').props('rounded outlined dense')

    # slug_button = ui.button('Submit', on_click=lambda e: get_tourney_info(
    #     e.sender, slug_input, event_select, stream_select))

    # event_select = ui.select(label='Select Event',
    #                          options=['Insert Slug'],
    #                          on_change=lambda e: get_phases(e, phase_select),
    #                          value=[]).classes('w-60')

    # phase_select = ui.select(label='Select Phase',
    #                          options=['Insert Slug'],
    #                          on_change=lambda e: print(e.value),
    #                          value=[]).classes('w-60')
    # # # *Grabbing Stream based on tournament slug
    # stream_select = ui.select(label='Select Stream',
    #                          options=['Insert Slug'],
    #                          on_change=lambda e: print(e.value),
    #                          value=[]).classes('w-60')
    # event_select.disable()
    # phase_select.disable()
    # stream_select.disable()
if __name__ in {"__main__", "__mp_main__"}:
    main()
    # ui.run()
