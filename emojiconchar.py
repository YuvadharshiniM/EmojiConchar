import emoji

def emoji_to_description(emoji_input):
    description = emoji.demojize(emoji_input)
    description = description.replace(":", " ").replace("_", " ")
    description = description.title()
    return description
