{
    "name": "Troullides Website Theme",
    "version": "19.0.1.0.0",
    "category": "Website",
    "summary": "Troullides custom website styling",
    "depends": [
        "website",
        "website_sale",
    ],

    "data": [
        "views/homepage.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "theme_troullides/static/src/css/troullides.css",
        ],
    },

    "installable": True,
    "application": False,
}
