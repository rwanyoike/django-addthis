from django.conf import settings

# Ref: http://support.addthis.com/customer/portal/articles/1337994-the-addthis_config-variable
ADDTHIS_SETTINGS = getattr(settings, "ADDTHIS_SETTINGS", {})


if "USERNAME" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"USERNAME": ""})

if "SERVICES_EXCLUDE" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"SERVICES_EXCLUDE": ""})
if "SERVICES_COMPACT" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"SERVICES_COMPACT": ""})
if "SERVICES_EXPANDED" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"SERVICES_EXPANDED": ""})
if "SERVICES_CUSTOM" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"SERVICES_CUSTOM": ""})

if "UI_CLICK" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_CLICK": False})
if "UI_DELAY" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_DELAY": 0})
if "UI_HOVER_DIRECTION" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_HOVER_DIRECTION": 0})
if "UI_LANGUAGE" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_LANGUAGE": ""})
if "UI_OFFSET_TOP" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_OFFSET_TOP": 0})
if "UI_OFFSET_LEFT" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_OFFSET_LEFT": 0})
if "UI_HEADER_COLOR" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_HEADER_COLOR": ""})
if "UI_HEADER_BACKGROUND" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_HEADER_BACKGROUND": ""})
if "UI_COBRAND" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_COBRAND": ""})
if "UI_USE_CSS" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_USE_CSS": True})
if "UI_USE_ADDRESSBOOK" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_USE_ADDRESSBOOK": False})
if "UI_508_COMPLIANT" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"UI_508_COMPLIANT": False})

if "DATA_TRACK_CLICKBACK" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"DATA_TRACK_CLICKBACK": True})
if "DATA_GA_TRACKER" not in ADDTHIS_SETTINGS:
    ADDTHIS_SETTINGS.update({"DATA_GA_TRACKER": ""})
