from import_export import resources
from traits.models import Trait
from import_export.admin import ImportExportModelAdmin
from .forms import TraitForm

headers_to_print = []
expected_headers = ['id', 'genus', 'species', 'isi', 'fruit_type']

class TraitResource(resources.ModelResource):
    class Meta:
        model = Trait

    def before_import(self, dataset, using_transactions, dry_run=True, collect_failed_rows=True, **kwargs): #raise_errors=True

        if 'id' not in dataset.headers:
            dataset.insert_col(0, lambda row: "", header='id')  # this works! 

        # check if headers match sample headers...
        # if OUT OF ORDER, sort ?

        for i in dataset.headers:
            #headers_to_print.append(i)
            if i != expected_headers:
                print('expected different order')
            else: 
                pass

        # confirm button?

        print('Here are the columns you will import:' )
        print(dataset.headers)
        # include in print stmt: warn user about unrecognized / unexpected cols 

#        for key in kwargs:
#        	print("another keyword arg: %s: %s:" % (key, kwargs[key]))  # kwargs 

            # get columns in correct order if user imports incorrectly-formatted csv
            # easy python way to rearrange

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()  # i is not a trait object yet; so far it's a tuple with whole dataset
        print('done')
		# add additional cleaning functions in here (for_delete? etc.)

class TraitAdmin(ImportExportModelAdmin):
	list_display = ('genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource