from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='dashboard'),
    url(r'^auth/', include('django.contrib.auth.urls')),
    # Client
    url(r'^client/(?P<pk>\d+)$', views.client_view, name='client_view'),
    url(r'^client/(?P<pk>\d+)/edit$', views.client_edit, name='client_edit'),
    url(r'^client/add$', views.client_edit, name='client_edit'),
    url(r'^client$', views.client_index, name='client_index'),
    # Contact
    url(r'^contact/(?P<pk>\d+)$', views.contact_view, name='contact_view'),
    url(r'^contact/(?P<pk>\d+)/edit$', views.contact_edit,
        name='contact_edit'),
    url(r'^contact/add$', views.contact_edit, name='contact_edit'),
    url(r'^contact$', views.contact_index, name='contact_index'),
    # Contract
    url(r'^contract/(?P<pk>\d+)$', views.contract_view, name='contract_view'),
    url(r'^contract/(?P<pk>\d+)/edit$',
        views.contract_edit,
        name='contract_edit'),
    url(r'^contract/add$', views.contract_edit, name='contract_edit'),
    url(r'^contract$', views.contract_index, name='contract_index'),
    #    # Error (forced)
    #    url(r'^error$', views.error, name='error'),
    # Estimate
    url(r'^estimate/(?P<pk>\d+)$', views.estimate_view, name='estimate_view'),
    url(r'^estimate/(?P<pk>\d+)/edit$',
        views.estimate_edit,
        name='estimate_edit'),
    url(r'^estimate/add$', views.estimate_edit, name='estimate_edit'),
    url(r'^estimate$', views.estimate_index, name='estimate_index'),
    # Invoice
    url(r'^invoice/(?P<pk>\d+)$', views.invoice_view, name='invoice_view'),
    url(r'^invoice/(?P<pk>\d+)/edit$', views.invoice_edit,
        name='invoice_edit'),
    url(r'^invoice/add$', views.invoice_edit, name='invoice_edit'),
    url(r'^invoice$', views.invoice_index, name='invoice_index'),
    #    # Login
    url(r'^login$', views.login, name='login'),
    # Files
    url(r'^file/(?P<pk>\d+)$', views.file_view, name='file_view'),
    url(r'^file/(?P<pk>\d+)/edit$', views.file_edit, name='file_edit'),
    url(r'^file/add$', views.file_edit, name='file_edit'),
    url(r'^file$', views.file_index, name='file_index'),
    # Logs
    url(r'^log$', views.log_index, name='log_index'),
    # Newsletter
    url(r'^newsletter/(?P<pk>\d+)$',
        views.newsletter_view,
        name='newsletter_view'),
    url(r'^newsletter/(?P<pk>\d+)/edit$',
        views.newsletter_edit,
        name='newsletter_edit'),
    url(r'^newsletter/add$', views.newsletter_edit, name='newsletter_edit'),
    url(r'^newsletter$', views.newsletter_index, name='newsletter_index'),
    # Note
    url(r'^note/(?P<pk>\d+)$', views.note_view, name='note_view'),
    url(r'^note/(?P<pk>\d+)/edit$', views.note_edit, name='note_edit'),
    url(r'^note/add$', views.note_edit, name='note_edit'),
    url(r'^note$', views.note_index, name='note_index'),
    # Plot
    url(r'^plot$', views.plot, name='plot'),
    # Project
    url(r'^project/(?P<pk>\d+)$', views.project_view, name='project_view'),
    url(r'^project/(?P<pk>\d+)/edit$', views.project_edit,
        name='project_edit'),
    url(r'^project/add$', views.project_edit, name='project_edit'),
    url(r'^project$', views.project_index, name='project_index'),
    # Proposal
    url(r'^proposal/(?P<pk>\d+)$', views.proposal_view, name='proposal_view'),
    url(r'^proposal/(?P<pk>\d+)/edit$',
        views.proposal_edit,
        name='proposal_edit'),
    url(r'^proposal/add$', views.proposal_edit, name='proposal_edit'),
    url(r'^proposal$', views.proposal_index, name='proposal_index'),
    # Report
    url(r'^report/(?P<pk>\d+)$', views.report_view, name='report_view'),
    url(r'^report$', views.report_index, name='report_index'),
    url(r'^report/add$', views.report_edit, name='report_edit'),
    url(r'^report/(?P<pk>\d+)/edit$', views.report_edit, name='report_edit'),
    #    # Services
    #    url(r'^service/(?P<pk>\d+)/edit$', views.service_edit,
    #        name='service_edit'),
    # Settings
    url(r'^settings/app/edit$',
        views.settings_app_edit,
        name='settings_app_edit'),
    url(r'^settings/app$', views.settings_app, name='settings_app'),
    url(r'^settings/company/edit$',
        views.settings_company_edit,
        name='settings_company_edit'),
    url(r'^settings/company$', views.settings_company,
        name='settings_company'),
    url(r'^settings/contract/edit$',
        views.settings_contract_edit,
        name='settings_contract_edit'),
    url(r'^settings/contract$',
        views.settings_contract,
        name='settings_contract'),
    # Social
    url('', include('social_django.urls', namespace='social')),
    # Task
    url(r'^task/(?P<pk>\d+)$', views.task_view, name='task_view'),
    url(r'^task/(?P<pk>\d+)/edit$', views.task_edit, name='task_edit'),
    url(r'^task/add$', views.task_edit, name='task_edit'),
    url(r'^task$', views.task_index, name='task_index'),
    # Time
    url(r'^time/(?P<pk>\d+)$', views.time_view, name='time_view'),
    url(r'^time/(?P<pk>\d+)/edit$', views.time_edit, name='time_edit'),
    url(r'^time/add$', views.time_edit, name='time_edit'),
    url(r'^time$', views.time_index, name='time_index'),
    # User
    url(r'^user/(?P<pk>\d+)$', views.user_view, name='user_view'),
    url(r'^user/(?P<pk>\d+)/edit$', views.user_edit, name='user_edit'),
    url(r'^user/add$', views.user_edit, name='user_edit'),
    url(r'^user$', views.user_index, name='user_index'),
]
