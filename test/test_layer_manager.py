import unittest
from unittest.mock import MagicMock

from src.layers.layer import Layer
from src.layers.layer_manager import LayerManager


class FakeLayer(Layer):
    def __init__(self, name: str = "layer") -> None:
        self.name = name
        self.update = MagicMock()
        self.render = MagicMock()
        self.process_event = MagicMock()

    def __repr__(self) -> str:
        return f"FakeLayer({self.name!r})"


class NotALayer:
    pass

class LayerManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.layer_manager = LayerManager()

    def test_init_creates_empty_stack(self) -> None:
        self.assertEqual(len(self.layer_manager), 0)
        self.assertEqual(self.layer_manager.layers, [])

    # -------------------------------------------------------------------
    # push_layer
    # -------------------------------------------------------------------

    def test_push_layer_adds_layer_to_stack(self) -> None:
        layer = FakeLayer("A")
        self.layer_manager.push_layer(layer)

        self.assertEqual(len(self.layer_manager), 1)
        self.assertIs(self.layer_manager.layers[-1], layer)

    def test_push_layer_multiple_layers_preserves_order(self) -> None:
        layer_a = FakeLayer("A")
        layer_b = FakeLayer("B")
        layer_c = FakeLayer("C")

        self.layer_manager.push_layer(layer_a)
        self.layer_manager.push_layer(layer_b)
        self.layer_manager.push_layer(layer_c)

        self.assertEqual(len(self.layer_manager), 3)
        self.assertEqual(self.layer_manager.layers, [layer_a, layer_b, layer_c])

    def test_push_layer_raises_type_error_for_invalid_type(self) -> None:
        with self.assertRaises(TypeError):
            self.layer_manager.push_layer(NotALayer())

    def test_push_layer_invalid_type_does_not_modify_stack(self) -> None:
        with self.assertRaises(TypeError):
            self.layer_manager.push_layer(NotALayer())
        self.assertEqual(len(self.layer_manager), 0)

    # -------------------------------------------------------------------
    # pop_layer
    # -------------------------------------------------------------------

    def test_pop_layer_removes_and_returns_top_layer(self) -> None:
        layer_a = FakeLayer("A")
        layer_b = FakeLayer("B")
        self.layer_manager.push_layer(layer_a)
        self.layer_manager.push_layer(layer_b)

        popped = self.layer_manager.pop_layer()

        self.assertIs(popped, layer_b)
        self.assertEqual(len(self.layer_manager), 1)
        self.assertIs(self.layer_manager.layers[-1], layer_a)

    def test_pop_layer_raises_runtime_error_when_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            self.layer_manager.pop_layer()

    def test_pop_layer_with_n_removes_multiple_layers(self) -> None:
        layers = [FakeLayer(str(i)) for i in range(5)]
        for layer in layers:
            self.layer_manager.push_layer(layer)

        popped = self.layer_manager.pop_layer(3)

        self.assertEqual(len(self.layer_manager), 2)
        self.assertIs(popped, layers[2])
        self.assertEqual(self.layer_manager.layers, layers[:2])

    def test_pop_layer_n_greater_than_stack_size_clamps_to_stack_size(self) -> None:
        layer_a = FakeLayer("A")
        layer_b = FakeLayer("B")
        self.layer_manager.push_layer(layer_a)
        self.layer_manager.push_layer(layer_b)

        popped = self.layer_manager.pop_layer(10)

        self.assertEqual(len(self.layer_manager), 0)
        self.assertIs(popped, layer_a)

    def test_pop_layer_default_n_is_one(self) -> None:
        layer_a = FakeLayer("A")
        layer_b = FakeLayer("B")
        self.layer_manager.push_layer(layer_a)
        self.layer_manager.push_layer(layer_b)

        self.layer_manager.pop_layer()

        self.assertEqual(len(self.layer_manager), 1)

    # -------------------------------------------------------------------
    # top
    # -------------------------------------------------------------------

    def test_top_returns_last_pushed_layer(self) -> None:
        layer = FakeLayer("A")
        self.layer_manager.push_layer(layer)

        self.assertIs(self.layer_manager.top(), layer)

    def test_top_does_not_remove_layer(self) -> None:
        layer = FakeLayer("A")
        self.layer_manager.push_layer(layer)
        self.layer_manager.top()

        self.assertEqual(len(self.layer_manager), 1)

    def test_top_raises_runtime_error_when_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            self.layer_manager.top()

    # -------------------------------------------------------------------
    # update / render / process_event
    # -------------------------------------------------------------------

    def test_update_delegates_to_top_layer(self) -> None:
        bottom = FakeLayer("bottom")
        top = FakeLayer("top")
        self.layer_manager.push_layer(bottom)
        self.layer_manager.push_layer(top)

        self.layer_manager.update(0.016)

        top.update.assert_called_once_with(0.016)
        bottom.update.assert_not_called()

    def test_render_delegates_to_top_layer(self) -> None:
        bottom = FakeLayer("bottom")
        top = FakeLayer("top")
        self.layer_manager.push_layer(bottom)
        self.layer_manager.push_layer(top)

        fake_screen = MagicMock(name="pygame.Surface")
        self.layer_manager.render(fake_screen)

        top.render.assert_called_once_with(fake_screen)
        bottom.render.assert_not_called()

    def test_process_event_delegates_to_top_layer(self) -> None:
        bottom = FakeLayer("bottom")
        top = FakeLayer("top")
        self.layer_manager.push_layer(bottom)
        self.layer_manager.push_layer(top)

        fake_event = MagicMock(name="pygame.event.Event")
        self.layer_manager.process_event(fake_event)

        top.process_event.assert_called_once_with(fake_event)
        bottom.process_event.assert_not_called()

    def test_update_raises_runtime_error_when_stack_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            self.layer_manager.update(0.016)

    def test_render_raises_runtime_error_when_stack_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            self.layer_manager.render(MagicMock())

    def test_process_event_raises_runtime_error_when_stack_empty(self) -> None:
        with self.assertRaises(RuntimeError):
            self.layer_manager.process_event(MagicMock())


if __name__ == '__main__':
    unittest.main()