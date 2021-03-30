"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Card deck with image, text, and button"""

    title = blocks.CharBlock(required=False, help_text='Add your title')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="Button page will be first")),
                ("button_cta", blocks.TextBlock(required=False, max_length=20)),
            ]
        )
    )

    class Meta: # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""

    class Meta: # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext with limited features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta: # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock (blocks.StructBlock):
    """Call to action section"""

    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True, max_length=100)
    # can limit features if needed
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=20)

    class Meta: # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"
