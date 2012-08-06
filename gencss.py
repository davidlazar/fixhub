# generates css that fixes github's icons
import base64

# begin user customization
mini_icons = \
    { 'watchers': 'icons/gentleface/eye_icon_16.png'
    , 'watching': 'icons/gentleface/eye_icon_16.png'
    , 'star': 'icons/iconic/star_16x16.png'
    , 'public-repo': 'icons/famfamfam/emoticon_smile.png'
    , 'private-repo': 'icons/famfamfam/lock.png'
    , 'repo-forked': 'icons/iconic/fork_14x16.png'
    , 'feed': 'icons/famfamfam/feed.png'
    , 'push': 'icons/gentleface/arrow_right_icon_16.png'
    , 'fork': 'icons/iconic/fork_14x16.png'
    , 'create': 'icons/iconic/plus_16x16.png'
    , 'issue-opened': 'icons/gentleface/bug_icon_16.png'
    , 'issue-comment': 'icons/iconic/chat_16x16.png'
    , 'directory': 'icons/famfamfam/folder.png'
    , 'text-file': 'icons/famfamfam/page_white_text.png'
    , 'readme': 'icons/famfamfam/page_white_text.png'
    }

mega_icons = \
    { 'public-repo': 'icons/famfamfam/emoticon_smile.png'
    , 'private-repo': 'icons/famfamfam/lock.png'
    , 'repo-forked': 'icons/iconic/fork_14x16.png'
    }

context_icon = 'icons/famfamfam/cog.png'
# end user customization


def b64encode_file(filename):
    f = open(filename, 'rb')
    bs = f.read()
    return base64.b64encode(bs)

set_icon_css = """
{selector} {{
    content: url('data:image/png;base64,{icon}') !important;
}}
"""

def set_icon(selector, iconfile):
    icon = b64encode_file(iconfile).decode('ascii')
    print(set_icon_css.format(**locals()))

remove_bg_css = """
{selector} {{
    background: none !important;
}}
"""

def remove_bg(selector):
    print(remove_bg_css.format(**locals()))

valign_css = """
{selector} {{
    vertical-align: middle;
}}
"""

def valign(selector):
    print(valign_css.format(**locals()))

def fix_icon(style, ghname, iconfile):
    selector = ".{style}-icon-{name}".format(style=style, name=ghname)
    set_icon(selector + ":before", iconfile)
    valign(selector + ":before")
    remove_bg(selector)

def fix_icon_style(style, icon_map):
    for ghname, iconfile in icon_map.items():
        fix_icon(style, ghname, iconfile)

fix_icon_style('mini', mini_icons)
fix_icon_style('mega', mega_icons)

set_icon('.context-button .icon:before', context_icon)
