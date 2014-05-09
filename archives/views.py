from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from archives.models import Presenter

# def presenter(request, grad_year, nickname):
# 	presenter_object = get_object_or_404(Presenter, nickname=nickname)
# 	context = RequestContext(request, {
# 		"presenter" : presenter_object,
# 	})
# 	return render(request, "archives/presenter.html", context)

class IndexView(generic.ListView):
	template_name = 'archives/index.html'
	context_object_name = 'archives_dict'

	def get_queryset(self):
		"""Return dict of presenters keyed on graduation year with presenter-list values."""
		archives_list = Presenter.objects.order_by('grad_year')
		grad_years = [presenter.grad_year for presenter in archives_list]
		archives_dict = {grad_year: [] for grad_year in grad_years}
		for presenter in archives_list:
			archives_dict[presenter.grad_year].append(presenter)
		return archives_dict


class YearView(generic.ListView):
	template_name = 'archives/grad_year.html'
	context_object_name = 'year_archives_list'

	def get_queryset(self):
		"""Return list of presenters from a given graduation year."""
		return get_list_or_404(Presenter, grad_year=2015)


class PresenterView(generic.DetailView):
	model = Presenter
	template_name = 'polls/results.html'

	# def get_presenter(self, id):
	# 	"""Return a presenter object."""
	# 	return