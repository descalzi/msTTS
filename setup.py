from distutils.core import setup
setup(
  name = 'msTTS',
  packages = ['msTTS'], # this must be the same as the name above
  version = '0.1',
  description = 'Generate audio files from text (TTS) using Microsoft Cognitive Services Speech API',
  author = 'Martin Descalzi ',
  author_email = 'martin.descalzi@gmail.com',
  url = 'https://github.com/descalzi/msTTS', # use the URL to the github repo
  download_url = 'https://github.com/descalzi/msTTS/tarball/0.1', # I'll explain this in a second
  keywords = ['microsoft', 'tts'], # arbitrary keywords
  classifiers = [],
)
