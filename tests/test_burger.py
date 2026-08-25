import pytest
from unittest.mock import Mock

class TestBurger:
    # проверяем инициализацию объекта - булочка пустая, список ингредиентов - пустой
    @pytest.mark.parametrize('attribute, value', [
            ('bun', None), 
            ('ingredients', [])
        ])
    def test_init_burger_empty_ingredient_bun_no(self, new_burger, attribute, value):
        assert getattr(new_burger, attribute) == value
        

    # проверяем успешную установку булочки
    def test_set_buns_option_bun_is_correct(self, new_burger, mock_bun):
        new_burger.set_buns(mock_bun)
        assert new_burger.bun == mock_bun

    # проверяем добавление ингредиентов в бургер (соус и начинка) и их расположение
    def test_add_ingredient_sauce_and_filling_add_to_list(self, new_burger, mock_filling, mock_sauce):
        new_burger.add_ingredient(mock_filling)
        new_burger.add_ingredient(mock_sauce)
        assert new_burger.ingredients == [mock_filling, mock_sauce]

    # проверяем удаление ингредиента по его индексу
    def test_remove_ingredient_removed_by_index(self, new_burger, mock_filling, mock_sauce):
        new_burger.ingredients = [mock_filling, mock_sauce]
        new_burger.remove_ingredient(0)
        assert new_burger.ingredients == [mock_sauce]

    # проверяем перемещение ингредиента в середину списка
    def test_move_ingredient_changes_place(self, new_burger, mock_filling, mock_sauce):
        mock_cutlet = Mock()
        new_burger.ingredients = [mock_filling, mock_sauce, mock_cutlet]
        new_burger.move_ingredient(1, 0)
        assert new_burger.ingredients == [mock_sauce, mock_filling, mock_cutlet]

    # проверяем правильность расчета стоимости бургера
    @pytest.mark.parametrize (
            'ingredients, total_price',
            [
                ([], 600),  # бургер только с булочками
                (['mock_filling'], 800),  # бургер с булочками и начинкой
                (['mock_sauce'], 900), # бургер с булочками и соусом
                (['mock_filling', 'mock_sauce'], 1100) # бургер с булочками, начинкой и соусом
            ],
            indirect = ['ingredients']
    )
    def test_get_price_correct_total_price(self, new_burger, mock_bun, ingredients, total_price):
        new_burger.bun = mock_bun
        new_burger.ingredients = ingredients
        assert new_burger.get_price() == total_price

    # проверяем корректность написания чека
    @pytest.mark.parametrize (
            'ingredients, check_body, price',
            [
                ([], [], 600), # чек на бургер только с булочками
                (['mock_filling'], ['= filling dinosaur ='], 800), # чек на бургер с булочками и начинкой
                (['mock_sauce'], ['= sauce chili sauce ='], 900), # чек на бургер с булочками и соусом
                # чек на бургер c булочками, начинкой и соусом
                (['mock_filling', 'mock_sauce'], ['= filling dinosaur =', '= sauce chili sauce ='], 1100) 
            ],
            indirect = ['ingredients']
    )
    def test_get_receipt_returns_correct_receipt(self, new_burger, mock_bun, ingredients, check_body, price):
        new_burger.bun = mock_bun
        new_burger.ingredients = ingredients

        # собираем текст чека
        check = '\n'.join(['(==== red bun ====)', *check_body, '(==== red bun ====)\n', f'Price: {price}'])
        assert new_burger.get_receipt() == check
        