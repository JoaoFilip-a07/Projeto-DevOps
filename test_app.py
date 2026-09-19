import unittest
import app


class TestTarefas(unittest.TestCase):

    def setUp(self):
        app.tarefas.clear()

    def test_adicionar_tarefa(self):
        app.adicionar_tarefa("Estudar")
        self.assertIn("Estudar", app.tarefas)

    def test_adicionar_duas_tarefas(self):
        app.adicionar_tarefa("Estudar")
        app.adicionar_tarefa("Treinar")
        self.assertEqual(len(app.tarefas), 2)

    def test_remover_tarefa(self):
        app.tarefas.append("Estudar")
        app.remover_tarefa("Estudar")
        self.assertNotIn("Estudar", app.tarefas)

    def test_remover_tarefa_inexistente(self):
        app.tarefas.append("Estudar")
        app.remover_tarefa("Treinar")
        self.assertEqual(app.tarefas, ["Estudar"])

    def test_concluir_tarefa(self):
        app.tarefas.append("Estudar")
        app.concluir_tarefa("Estudar")
        self.assertNotIn("Estudar", app.tarefas)


if __name__ == "__main__":
    unittest.main()
