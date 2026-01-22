{
    'name': 'CRM Restriction and filter',
    'category': 'Sales/CRM',
    'sequence': 2,
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['crm'],
    'data': [

        "views/filter.xml",
    ],
    'demo': [
    ],
    'application': True,
    'license': 'LGPL-3',
}
