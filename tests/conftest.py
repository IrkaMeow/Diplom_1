import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

# создает чистый объект бургера
@pytest.fixture
def new_burger():
    return Burger()

# создает мок булочки
@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'red bun'
    bun.get_price.return_value = 300
    return bun

# создает мок начинки
@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_price.return_value = 200
    filling.get_name.return_value = 'dinosaur'
    filling.get_type.return_value = 'FILLING'
    return filling

# создает мок соуса
@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_price.return_value = 300
    sauce.get_name.return_value = "chili sauce"
    sauce.get_type.return_value = 'SAUCE'
    return sauce

# фикстура для передачи мок-фикстур в параметризацию
@pytest.fixture
def ingredients(request):
    names = request.param
    return [request.getfixturevalue(name) for name in names]
