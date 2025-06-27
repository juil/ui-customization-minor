{
    'name': 'Minor UI Fixes',
    'version': '17.0.1.0.0',
    'category': 'Technical',
    'summary': 'Minor UI fixes for Odoo v17.',
    'depends': ['web', 'hr_holidays'], # Ensure this depends on the modules whose styles you're affecting
    'data': [], # No XML data needed for this specific CSS override
    'assets': {
        'web.assets_backend': [ # This tells Odoo to load your SCSS file in the backend
            'ui-customization-minor/static/src/scss/custom_styles.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
