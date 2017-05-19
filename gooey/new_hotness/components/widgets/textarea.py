from PyQt5.QtWidgets import QTextEdit

from gooey.new_hotness.components.widgets.textfield import TextField


class Textarea(TextField):
    widget_class = QTextEdit

    def setValue(self, value):
        self.value.document().setPlainText(value)

    def dispatchChange(self, *args, **kwargs):
        self.value.on_next({'value':  self.widget.toPlainText(), 'id': self._id})