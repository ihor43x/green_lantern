import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = "E"
        asteroid = Asteroid(x, y)
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot.direction == direction

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        [
            ((15, 25), (20, 20)),
            ((15, 25), (10, 30)),
            ((15, 25), (20, 30))
        ]
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestRobotMovement:
    def setup_module(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        return robot = Robot(x, y, asteroid, "N")

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        [
            ("N", "W"),
            ("W", "S"),
            ("S", "E"),
            ("E", "N")
        ]
    )
    def test_turn_left(self, current_direction, expected_direction):
        self.robot.turn_left()
        assert self.robot.direction == expected_direction
