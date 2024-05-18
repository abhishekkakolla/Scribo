filename = "gemini_api.config"
contents = open(filename).read()
config = eval(contents)
key = config['key']