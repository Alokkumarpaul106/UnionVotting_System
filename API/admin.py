from django.contrib import admin
from .models import Candidate,Vote,EligibleVoter





# admin.site.register(Candidate)
# admin.site.register(Vote)

class CandidateAdmin(admin.ModelAdmin):
    list_display=('name','vote_count')

admin.site.register(Candidate, CandidateAdmin)
class VoteAdmin(admin.ModelAdmin):
    list_display=('id','name','n_id','created_at')
admin.site.register(Vote,VoteAdmin)

class EligibleVoterAdmin(admin.ModelAdmin):
    list_display=('name','has_votted')
    search_fields=('name','NID')
admin.site.register(EligibleVoter,EligibleVoterAdmin)



