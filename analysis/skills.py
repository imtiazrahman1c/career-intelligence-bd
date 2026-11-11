"""Versioned editorial vocabulary. Detects mentions, never proficiency or demand."""
import re
import unicodedata
from html import unescape
from html.parser import HTMLParser

VERSION = 'editorial-mentions-v2'
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
    """Extract text without inventing spaces inside inline-formatted words.

    This is static HTML extraction, not a browser/CSS visibility engine.
    """
    BLOCKS = {'p', 'div', 'li', 'ul', 'ol', 'br', 'hr', 'section', 'article',
              'header', 'footer', 'table', 'tr', 'td', 'th', 'h1', 'h2', 'h3',
              'h4', 'h5', 'h6', 'blockquote', 'pre'}
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__()
        self.parts = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        hidden = (tag in {'script', 'style', 'template'} or 'hidden' in attrs)
        if tag in self.BLOCKS or hidden:
            self.parts.append(' ')
        if tag not in self.VOID:
            self.stack.append((tag, hidden))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                hidden = any(item[1] for item in self.stack[index:])
                del self.stack[index:]
                if hidden:
                    self.parts.append(' ')
                break
        if tag in self.BLOCKS:
            self.parts.append(' ')

    def handle_data(self, data):
        if not any(hidden for _, hidden in self.stack):
            self.parts.append(data)


def skill_mentions(description):
    """Unique IDs per description; negative/optional mentions still count."""
    if not isinstance(description, str):
        return []
    parser = VisibleText()
    parser.feed(description)
    text = ' '.join(unicodedata.normalize('NFKC', unescape(''.join(parser.parts))).split())
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

