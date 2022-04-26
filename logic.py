class Transport:
    """Основной класс, представляющий ВЕСЬ транспорт."""


class WaterTransport(Transport):
    """Весь водный транспорт."""


class Boat(WaterTransport):
    """Собственно, лодка."""


class SpeedBoat(Boat):
    """По сути, катер - частный случай лодки."""


class MotorShip(SpeedBoat):
    """Аналогично и корабль - частный случай моторной лодки."""


class Submarine(MotorShip):
    """По-моему, корабль будет к подлодкам ближе всего остального."""


class SailingVessel(Boat):
    """Парусное судно (дословно)."""


class AviaTransport(Transport):
    """Воздушный транспорт."""


class Aviation(AviaTransport):
    """Авиация."""


class Plane(Aviation):
    """Самолет."""


class Helicopter(Aviation):
    """Вертолет."""


class AviaSailing(AviaTransport):
    """Воздухоплавание."""


class Airship(AviaSailing):
    """Дирижабль."""


class AirBalloon(AviaSailing):
    """Воздушный шар."""


class GroundTransport(Transport):
    """Наземный транспорт."""


class Railways(GroundTransport):
    """Железнодорожный транспорт."""


class RoadTransport(GroundTransport):
    """Автомобильный транспорт."""


class CycleTransport(GroundTransport):
    """Велосипедный транспорт."""


class AnimalTransport(GroundTransport):
    """Движимый животными транспорт."""


class SpaceTransport(Transport):
    """Космический транспорт."""


class Rocket(SpaceTransport):
    """Ракеты."""


class Shuttle(SpaceTransport):
    """Шаттл."""