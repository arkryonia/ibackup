# @Author: drxos
# @Date:   Saturday, May 14th 2016, 11:24:37 am
# @Email:  sounton@gmail.com
# @Project: Digisity -- University made simple.
# @Last modified by:   drxos
# @Last modified time: Saturday, May 14th 2016, 11:25:02 am
# @License: Copyright (c) Foton IT, All Right Reserved


from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BackendTemplateView(LoginRequiredMixin, TemplateView):
    redirect_field_name = 'next'
    template_name = 'theme/backend/base.html'

class Allianza(TemplateView):
    template_name = "theme/allianza.html"
