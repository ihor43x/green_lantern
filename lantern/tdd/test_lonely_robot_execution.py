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

    @pytest.fixture(scope="module")
    def robot(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        return Robot(x, y, asteroid, "N")

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        [
            ("N", "W"),
            ("W", "S"),
            ("S", "E"),
            ("E", "N")
        ]
    )
    def test_turn_left(self, robot, current_direction, expected_direction):
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        [
            ("N", "E"),
            ("E", "S"),
            ("S", "W"),
            ("W", "N")
        ]
    )
    def test_turn_right(self, robot, current_direction, expected_direction):
        robot.turn_right()
        assert robot.direction == expected_direction


    @pytest.mark.parametrize(
        "direction,current_coordinates,new_coordinates",
        [
            ("N", (5, 10), (5, 11)),
            ("E", (5, 10), (6, 10)),
            ("S", (5, 10), (5, 9)),
            ("W", (5, 10), (4, 10)),
        ]
    )
    def test_move_forward(self, robot, direction, current_coordinates, new_coordinates):
        robot.move_forward()
        assert robot.direction == direction
        # with pytest.raises(robot.move_forward()):
        #     robot.x