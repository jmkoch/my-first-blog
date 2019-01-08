from import_export import resources
from traits.models import Trait

class TraitResource(resources.ModelResource):
    class Meta:
        model = Trait

#def before_import_row(self, row, **kwargs):
    #name = row.get('category')
    #(cat, _created) = Category.objects.get_or_create(name=name)
    #row['category'] = cat.id
    def before_import(self, dataset, dry_run, **kwargs):
        if 'id' not in dataset.headers:
            #dataset.headers.append('id')
            dataset.instert_col(0, lambda row: "", header='id')