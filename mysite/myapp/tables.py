import django_tables2 as tables
from .models import plugins

class analysis_table_view(tables.Table):
    bug_id = tables.Column()
    description = tables.Column()
    recomendation = tables.Column()
    workaround = tables.Column()

class TableView(tables.Table):
    class Meta:
        model = plugins
        template_name = 'django_tables2/bootstrap.html'