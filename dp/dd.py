# Klasse als Data Dictionary
#
# AUTHOR Sven Schrodt
# SINCE 2025-09-26
class DD:
    """ Data Dictionary class matching names<->labels(@GUI) and vice versa
    """
    
    pages = {
        "Sessions": "Sitzungsanalyse",
        "Sales": "Umsätze n. Vertriebskan.",
        "Upload": "Admin Panel",
        "Products": "Produkte",
        "Test": "Lab page",
        "Ads": "Werbeerfolge",
        "Ml": "ML Stuff",
        "Kpi": "KPIs",
        "Funnel": "Funnel - (Sitzungstyp)",
        "Dailysale": "Tagesumsätze",
        "Home": "Start",
        "Geo": "Geodaten",
        "Lab": "DEV Labor(Spielwiese)",
    }

    col_transl = {
        "sess_ctry": "Land",
        "sess_loc": "Ort",
        "datum": "Datum",
        "sug_platform": "Empfehlungsplattform",
        "landing_uri": "URI Landing Page",
        "session_duration": "Sitzungsdauer",
        "pages_per_sess": "Seiten je Sitzung",
        "jump_offs": "Absprünge",
        "sess_cart_add": "Warenkorb",
        "sess_co": "Check-Out err.",
        "sess_co_done": "Check-Out abgeschl.",
        "sessions": "Sitzungen",
        "Sitzung_min": "Sitzungsdauer[min.]",
        "cr": "Conversion Rate",
    }
    
    prd_trans = {
        "prod_name": "Produktname",
        "invent_start": "Inventareinheiten zum Ende",
        "invent_end": "Inventareinheiten zum Ende",
        "sold_units": "Verkaufte Inventareinheiten",
        "sell_rate": "Verkaufsrate"
    }

    session_y = ["jump_offs", "sess_cart_add", "sess_co", "sess_co_done", "sessions", "Sitzung_min"]

    sales_chan_y = [
        "Vertriebskanal",
        "Bestellungen",
        "Bruttoumsatz",
        "Rabatte",
        "Rückgaben",
        "Nettoumsatz",
        "Versandgebühren",
        "Steuern",
        "Gesamtumsatz",
    ]

    sess_trans_orig = {
        "sess_ctry": "Sitzungsland",
        "sess_loc": "Sitzungsort",
        "date": "Monat",
        "sug_platform": "Empfehlungsplattform",
        "landing_uri": "Landing-Page-URL",
        "session_duration": "Durchschnittliche Sitzungsdauer",
        "pages_per_sess": "Seitenaufrufe pro Sitzung",
        "jump_offs": "Absprünge",
        "sess_cart_add": "Sitzungen, in denen Artikel zum Warenkorb hinzugefügt wurden",
        "sess_co": "Sitzungen, bei denen der Checkout erreicht wurde",
        "sess_co_done": "Sitzungen, bei denen der Checkout abgeschlossen wurde",
        "sessions": "Sitzungen",
    }
    
    proj = ['equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal']


# cloc --by-file --fullpath --match-d 'dash'
