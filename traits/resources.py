from import_export import resources
from traits.models import Trait
from import_export.admin import ImportExportModelAdmin
from .forms import TraitForm


class TraitResource(resources.ModelResource):
    class Meta:
        model = Trait

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        print('hello') #this works up to this point
        # no validation here

        print(dataset.headers) # add note "here are the cols you will import."  
        # come back and improve this later !! 
        # include in print stmt: warn user about unrecognized / unexpected cols 

#        for key in kwargs:
#        	print("another keyword arg: %s: %s:" % (key, kwargs[key]))  # kwargs 

# want to show expected headers here:

        if 'id' not in dataset.headers:
            #dataset.headers.append('id')
            dataset.insert_col(0, lambda row: "", header='id') # make sure this works; improve it if not

            # get columns in correct order if user imports incorrectly-formatted csv
            # print/check dataset.headers --> compare to 'correct' order of headers 
            # easy python way to rearrange
            # add in models.py capital options (CAPSULE, Capsule, capsule) <- all valid (etc.)

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()  # i is not a trait object yet; so far it's a tuple with whole dataset
        print('done') # stopping point with Emma

# add additional cleaning functions in here (for_delete? etc.)


class TraitAdmin(ImportExportModelAdmin):
	list_display = ('genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource