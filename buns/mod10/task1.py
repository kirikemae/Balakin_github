import dataclasses
import json
import requests


def get_response(url: str) -> dict:
    """Получить данные из API и вернуть в виде Dict."""
    return requests.get(url).json()


@dataclasses.dataclass
class Pilot:
    name: str
    height: int
    mass: int
    homeworld: str
    homeworld_url: str


@dataclasses.dataclass
class Ship:
    name: str
    max_atmosphering_speed: int
    starship_class: str
    pilots: list[Pilot]


def get_ship(ship_url: str) -> Ship:
    ship_dict = get_response(ship_url)
    pilots = []
    pilot_urls = ship_dict.get('pilots')
    if pilot_urls is not None:
        for pilot_url in pilot_urls:
            pilot_dict = get_response(pilot_url)

            pilot_homeworld_url = pilot_dict.get('homeworld')
            pilot_homeworld_name = get_response(pilot_homeworld_url).get('name')

            pilot = Pilot(
                name=pilot_dict.get('name'),
                height=pilot_dict.get('height'),
                mass=pilot_dict.get('mass'),
                homeworld=pilot_homeworld_name,
                homeworld_url=pilot_dict.get('homeworld'),
            )
            pilots.append(pilot)

    return Ship(
        name=ship_dict.get('name'),
        max_atmosphering_speed=ship_dict.get('max_atmosphering_speed'),
        starship_class=ship_dict.get('starship_class'),
        pilots=pilots,
    )


if __name__ == '__main__':
    ship = get_ship('https://swapi.dev/api/starships/10/')
    ship_json = json.dumps(ship, default=lambda dc: dc.__dict__, indent=4)

    with open('./ship.json', 'w') as ship_file:
        ship_file.write(ship_json)

    print(ship_json)