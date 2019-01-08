from import_export import resources
from traits.models import Trait
from import_export.admin import ImportExportModelAdmin
from .forms import TraitForm


class TraitResource(resources.ModelResource):
    class Meta:
        model = Trait

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        print('hello') #this works up to this point
        # try printing imported objects --> figure out how to manipulate that
        #iterate thru rows of dataset (for i in rows:  --> call i.full_clean()
        #rows = dataset[]

        # no validation here
        # yes maniuplate csv imported here

        if 'id' not in dataset.headers:
            #dataset.headers.append('id')
            dataset.insert_col(0, lambda row: "", header='id') # make sure this works; improve it if not

            # get columns in correct order if user imports incorrectly-formatted csv
            # print/check dataset.headers --> compare to 'correct' order of headers 
            # (currently just the order in models.py); still need to make template csv w/ correct headers
            # rearrange --> bubble sort ? (sort headers correctly --> overwrite to produce correct header csv)
            # easy python way to rearrange

            # play around w/ what is done correctly (apparently the order!?!?!)
            # what still needs fixing --> determine manually thru messing up data, etc.

            # add in models.py capital options (CAPSULE, Capsule, capsule) <- all valid (etc.)

            # !!!!!!!! next big step: how to avoid admin interface altogether & allow users to do it 
            # !!!!!!!! (or, set up/see if there's an option for a junior-admin type of thing?)

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.full_clean()  # i is not a trait object yet; so far it's a tuple with whole dataset
        print('done') # stopping point with Emma

# add additional cleaning functions in here (for_delete? etc.)


class TraitAdmin(ImportExportModelAdmin):
	list_display = ('genus', 'species', 'isi', 'fruit_type')
	form = TraitForm
	resource_class = TraitResource