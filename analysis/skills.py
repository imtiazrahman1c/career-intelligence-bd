"""Versioned editorial vocabulary. Detects mentions, never proficiency or demand."""
import re
from html import unescape
from html.parser import HTMLParser

VERSION = 'editorial-mentions-v1'
SKILLS = {
    'sql': ('SQL',), 'python': ('Python',),
    'spreadsheets': ('Microsoft Excel', 'Excel', 'Google Sheets'),
    'power_bi': ('Power BI',), 'tableau': ('Tableau',),
    'seo': ('SEO', 'search engine optimization'),
    'google_ads': ('Google Ads', 'Google AdWords'),
    'meta_ads': ('Meta Ads', 'Facebook Ads'),
    'ga4': ('GA4', 'Google Analytics 4'),
    'copywriting': ('copywriting',),
    'photoshop': ('Photoshop',), 'illustrator': ('Adobe Illustrator',),
    'figma': ('Figma',), 'typography': ('typography',),
}
CAREERS = {
    'data_analyst': ('sql', 'python', 'spreadsheets', 'power_bi', 'tableau'),
    'digital_marketer': ('seo', 'google_ads', 'meta_ads', 'ga4', 'copywriting'),
    'graphic_designer': ('photoshop', 'illustrator', 'figma', 'typography'),
}


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        self.parts.append(' ')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def skill_mentions(description):
    """Unique IDs per description; negative/optional mentions still count."""
    if not isinstance(description, str):
        return []
    parser = VisibleText()
    parser.feed(description)
    text = ' '.join(unescape(''.join(parser.parts)).split())
    return sorted(key for key, aliases in SKILLS.items() if any(
        re.search(r'(?<!\w)' + re.escape(alias) + r'(?!\w)', text, re.I)
        for alias in aliases
    ))


def bangladesh_location_signal(value):
    """Only structured provider location metadata; not final eligibility.

    Empty locations, APAC and Remote are deliberately unknown. Even explicit
    Bangladesh/worldwide signals require work-authorisation/timezone review.
    """
    if isinstance(value, list):
        if any(not isinstance(item, str) for item in value):
            return 'unknown'
        tokens = value
    elif isinstance(value, str):
        tokens = re.split(r'[,;|]', value)
    else:
        return 'unknown'
    tokens = {token.strip().casefold() for token in tokens}
    if tokens & {'bangladesh', 'bd'}:
        return 'bangladesh_listed_review_required'
    if tokens & {'worldwide', 'anywhere', 'global'}:
        return 'worldwide_listed_review_required'
    return 'unknown'
