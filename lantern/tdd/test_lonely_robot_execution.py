import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


@pytest.fixture(scope="module")
def asteroid():
    x, y = 10, 20
    return Asteroid(x, y)


@pytest.fixture(scope="module")
def robot(asteroid):
    x, y = 5, 10
    return Robot(x, y, "N", asteroid)


class TestRobotCreation:
    def test_parameters(self, robot, asteroid):
        assert robot.x == 5
        assert robot.y == 10
        assert robot.asteroid == asteroid
        assert robot.direction == "N"

    @pytest.mark.parametrize("robot_coordinates", [(20, 10), (5, 25), (11, 21)])
    def test_check_if_robot_on_asteroid(self, asteroid, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            Robot(*robot_coordinates, "N", asteroid)


class TestRobotMovement:
    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        [("N", "W"),
         ("W", "S"),
         ("S", "E"),
         ("E", "N")])
    def test_turn_left(self, robot, current_direction, expected_direction):
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        [("N", "E"),
         ("E", "S"),
         ("S", "W"),
         ("W", "N")])
    def test_turn_right(self, robot, current_direction, expected_direction):
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "direction,current_coordinates,new_coordinates",
        [("N", (5, 10), (5, 11)),
         ("E", (5, 10), (6, 10)),
         ("S", (5, 10), (5, 9)),
         ("W", (5, 10), (4, 10))])
    def test_move_forward(self, robot, direction, current_coordinates, new_coordinates):
        pass
        # robot.move_forward()
        # assert robot.direction == direction
        # with pytest.raises(robot.move_forward()):
        #     robot.x
